#!/usr/bin/env node
// Guarded Supabase remote smoke harness.
// Developer-only. Not imported by the public site runtime.

import { WC2026_SUPABASE_PUBLIC_CONFIG } from "../site/js/config/supabase.public.js";
import { SupabaseBracketStore } from "../site/js/services/SupabaseBracketStore.js";
import { assertRemoteStoreActivationAllowed } from "../site/js/services/RemoteStoreActivationGuard.js";
import { createEmptyBracketDocument } from "../site/js/model/UserBracketModel.js";

function fail(message) {
  console.error(`WC2026 Supabase remote smoke blocked: ${message}`);
  process.exit(1);
}

if (process.env.WC2026_SUPABASE_REMOTE_SMOKE !== "1") {
  fail("set WC2026_SUPABASE_REMOTE_SMOKE=1 to run this explicit developer-only smoke harness");
}

const userId = process.env.WC2026_SUPABASE_SMOKE_USER_ID;
if (!userId) {
  fail("set WC2026_SUPABASE_SMOKE_USER_ID to an existing auth.users UUID before running");
}

assertRemoteStoreActivationAllowed({
  requestedMode: "remote",
  explicitDeveloperSmoke: true,
  publicRuntime: false,
});

if (!WC2026_SUPABASE_PUBLIC_CONFIG?.supabaseUrl || !WC2026_SUPABASE_PUBLIC_CONFIG?.supabasePublishableKey) {
  fail("Supabase public URL or publishable key is missing");
}

const { createClient } = await import("https://esm.sh/@supabase/supabase-js@2");

const client = createClient(
  WC2026_SUPABASE_PUBLIC_CONFIG.supabaseUrl,
  WC2026_SUPABASE_PUBLIC_CONFIG.supabasePublishableKey,
  {
    auth: {
      persistSession: false,
      autoRefreshToken: false,
      detectSessionInUrl: false,
    },
  }
);

const store = new SupabaseBracketStore({ supabaseClient: client });

const bracket = createEmptyBracketDocument({
  userId,
  gameId: "game1",
  expectedPickCount: 63,
});

bracket.status = "draft";
bracket.visibility = "private";
bracket.updatedAt = new Date().toISOString();

await store.saveUserBracket(bracket);
const loaded = await store.loadUserBracket(userId, "game1");

if (!loaded) {
  fail("saved bracket did not load back");
}

if (loaded.userId !== userId || loaded.gameId !== "game1") {
  fail("loaded bracket identity mismatch");
}

if (!loaded.picksBySlot || typeof loaded.picksBySlot !== "object") {
  fail("loaded bracket missing picksBySlot object");
}

console.log("OK: guarded Supabase remote smoke path can save/load one private draft BracketDocument when explicitly enabled.");
