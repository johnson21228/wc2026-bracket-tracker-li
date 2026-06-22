#!/usr/bin/env node
// Boundary sentinel: RemoteStoreActivationGuard is intentionally not imported by this offline harness.
// The harness proves SupabaseBracketStore adapter shape without activating remote mode.
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";

const ROOT = process.cwd();
const storePath = path.join(ROOT, "site/js/services/SupabaseBracketStore.js");
const source = fs.readFileSync(storePath, "utf8");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

assert(source.includes("class SupabaseBracketStore"), "SupabaseBracketStore class is missing");
assert(source.includes("loadUserBracket(userId)"), "loadUserBracket(userId) contract is missing");
assert(source.includes("saveUserBracket(bracketDocument)"), "saveUserBracket(bracketDocument) contract is missing");
assert(source.includes("picks_json"), "SupabaseBracketStore must map BracketDocument to picks_json");
assert(source.includes(".upsert("), "SupabaseBracketStore must use upsert for owner/game save contract");

class FakeSupabaseQuery {
  constructor(client, tableName) {
    this.client = client;
    this.tableName = tableName;
    this.filters = {};
    this.payload = null;
    this.upsertOptions = null;
  }

  select(columns = "*") {
    this.selectedColumns = columns;
    return this;
  }

  eq(column, value) {
    this.filters[column] = value;
    return this;
  }

  upsert(payload, options = {}) {
    this.payload = Array.isArray(payload) ? payload[0] : payload;
    this.upsertOptions = options;
    return this;
  }

  async maybeSingle() {
    return this.resolveSingle({ maybe: true });
  }

  async single() {
    return this.resolveSingle({ maybe: false });
  }

  async resolveSingle() {
    if (this.payload) {
      assert(this.tableName === "user_brackets", "save must target user_brackets table");
      assert(this.payload.user_id, "save payload must include user_id");
      assert(this.payload.game_id, "save payload must include game_id");
      assert(this.payload.picks_json, "save payload must include picks_json");
      assert(this.upsertOptions && String(this.upsertOptions.onConflict || "").includes("user_id"), "upsert must conflict on owner/game identity");
      assert(this.upsertOptions && String(this.upsertOptions.onConflict || "").includes("game_id"), "upsert must conflict on owner/game identity");

      const key = this.client.keyFor(this.payload.user_id, this.payload.game_id);
      this.client.rows.set(key, { ...this.payload });
      this.client.calls.push({ kind: "upsert", tableName: this.tableName, payload: { ...this.payload } });
      return { data: { ...this.payload }, error: null };
    }

    assert(this.tableName === "user_brackets", "load must target user_brackets table");
    assert(this.filters.user_id, "load must filter by user_id");
    assert(this.filters.game_id, "load must filter by game_id");

    const key = this.client.keyFor(this.filters.user_id, this.filters.game_id);
    const row = this.client.rows.get(key) || null;
    this.client.calls.push({ kind: "select", tableName: this.tableName, filters: { ...this.filters } });
    return { data: row ? { ...row } : null, error: null };
  }
}

class FakeSupabaseClient {
  constructor() {
    this.rows = new Map();
    this.calls = [];
  }

  keyFor(userId, gameId) {
    return `${userId}::${gameId}`;
  }

  from(tableName) {
    this.calls.push({ kind: "from", tableName });
    return new FakeSupabaseQuery(this, tableName);
  }
}

const fakeClient = new FakeSupabaseClient();

const sandbox = {
  console,
  Error,
  Object,
  String,
  Date,
  Array,
  Promise,
  URL,
  globalThis: {},
};

sandbox.createClient = function createClient() {
  return fakeClient;
};

sandbox.WC2026_SUPABASE_PUBLIC_CONFIG = Object.freeze({
  enabled: true,
  supabaseUrl: "https://offline-harness.supabase.invalid",
  supabasePublishableKey: "sb_publishable_offline_harness",
  authFlow: "magic_link",
});

sandbox.normalizeBracketDocument = function normalizeBracketDocument({ bracket }) {
  return {
    ...bracket,
    normalizedByOfflineHarness: true,
  };
};

const transformed = source
  .replace(/^import .*$/gm, "")
  .replace(/export\s*\{[\s\S]*?\};\s*$/m, "")
  + "\nglobalThis.__WC2026_SUPABASE_HARNESS__ = { SupabaseBracketStore, createSupabaseBracketStore };\n";

vm.createContext(sandbox);
vm.runInContext(transformed, sandbox, { filename: "SupabaseBracketStore.offline-harness.js" });

const harnessExports = sandbox.globalThis.__WC2026_SUPABASE_HARNESS__;
assert(harnessExports, "offline harness could not access SupabaseBracketStore exports");
assert(typeof harnessExports.SupabaseBracketStore === "function", "SupabaseBracketStore export is not a class/function");
assert(typeof harnessExports.createSupabaseBracketStore === "function", "createSupabaseBracketStore export is not a function");

const { SupabaseBracketStore, createSupabaseBracketStore } = harnessExports;

const store = new SupabaseBracketStore({
  client: fakeClient,
  tableName: "user_brackets",
  gameId: "game1",
  visibility: "private",
});

const userId = "00000000-0000-4000-8000-000000000001";

const emptyLoad = await store.loadUserBracket(userId);
assert(emptyLoad === null || emptyLoad === undefined, "empty load should return null/undefined before a save");

const document = {
  schemaVersion: 2,
  userId,
  gameId: "game1",
  status: "draft",
  expectedPickCount: 63,
  updatedAt: "2026-06-22T00:00:00.000Z",
  picksBySlot: {
    "R32-LEFT-01": {
      slotId: "R32-LEFT-01",
      teamId: "USA",
      source: "offline-contract-harness",
    },
  },
  phaseLocks: {
    r32LockedAt: null,
  },
};

const saved = await store.saveUserBracket(document);
assert(saved, "saveUserBracket should return a saved document");
assert(saved.picksBySlot, "saved document must preserve picksBySlot");
assert(saved.picksBySlot["R32-LEFT-01"].teamId === "USA", "saved document must preserve pick identity");

const storedRow = fakeClient.rows.get(`${userId}::game1`);
assert(storedRow, "fake client should contain saved user/game row");
assert(storedRow.user_id === userId, "stored row must preserve user_id");
assert(storedRow.game_id === "game1", "stored row must preserve game_id");
assert(storedRow.visibility === "private", "stored row must default to private visibility");
assert(storedRow.picks_json, "stored row must contain picks_json");
assert(storedRow.picks_json.picksBySlot["R32-LEFT-01"].teamId === "USA", "stored picks_json must preserve picksBySlot");

const loaded = await store.loadUserBracket(userId);
assert(loaded, "loadUserBracket should load after save");
assert(loaded.picksBySlot, "loaded document must preserve picksBySlot");
assert(loaded.picksBySlot["R32-LEFT-01"].teamId === "USA", "loaded document must preserve pick identity");

let missingUserRejected = false;
try {
  await store.loadUserBracket("");
} catch {
  missingUserRejected = true;
}
assert(missingUserRejected, "loadUserBracket should reject a missing user id");

const factoryStore = createSupabaseBracketStore({ client: fakeClient, gameId: "game1" });
assert(factoryStore, "createSupabaseBracketStore should return a store instance");
assert(typeof factoryStore.loadUserBracket === "function", "factory store must expose loadUserBracket");
assert(typeof factoryStore.saveUserBracket === "function", "factory store must expose saveUserBracket");

const upserts = fakeClient.calls.filter((call) => call.kind === "upsert");
const selects = fakeClient.calls.filter((call) => call.kind === "select");
assert(upserts.length >= 1, "offline harness should exercise save/upsert path");
assert(selects.length >= 1, "offline harness should exercise load/select path");

console.log("OK: SupabaseBracketStore offline contract harness loads/saves canonical BracketDocument shape without real Supabase or remote activation.");
