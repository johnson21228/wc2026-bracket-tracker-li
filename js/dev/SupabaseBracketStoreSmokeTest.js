import { SupabaseBracketStore } from "../services/SupabaseBracketStore.js";

const DEV_SMOKE_QUERY_FLAG = "devSupabaseBracketSmoke";
const SMOKE_TOURNAMENT_ID = "wc2026";
const SMOKE_GAME_ID = "game1-dev-smoke";

const REQUIRED_BRACKET_DOCUMENT_KEYS = Object.freeze([
  "schemaVersion",
  "userId",
  "tournamentId",
  "gameId",
  "status",
  "lifecycleState",
  "phaseLocks",
  "picksBySlot",
  "createdAt",
  "updatedAt",
  "submittedAt",
  "lockedAt",
  "visibility",
]);

function shouldRunSupabaseBracketStoreSmokeTest(locationSearch = window.location.search) {
  const params = new URLSearchParams(locationSearch);
  return params.get(DEV_SMOKE_QUERY_FLAG) === "1";
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function buildSmokeBracketDocument(userId) {
  const now = new Date().toISOString();

  return {
    schemaVersion: 1,
    userId,
    tournamentId: SMOKE_TOURNAMENT_ID,
    gameId: SMOKE_GAME_ID,
    status: "draft",
    lifecycleState: {
      stage: "group",
      source: "dev-supabase-bracket-smoke-test",
    },
    phaseLocks: {
      r32LockedAt: null,
    },
    picksBySlot: {
      "SMOKE-R32-1": {
        slotId: "SMOKE-R32-1",
        pick: { kind: "team", teamId: "FRA" },
        teamId: "FRA",
        teamName: "France",
        teamAbbr: "FRA",
        round: "R32",
        kind: "winner",
        pickedAt: now,
        source: "dev-supabase-bracket-smoke-test",
      },
    },
    createdAt: now,
    updatedAt: now,
    submittedAt: null,
    lockedAt: null,
    visibility: "private",
  };
}

function verifyCanonicalBracketDocument(document) {
  for (const key of REQUIRED_BRACKET_DOCUMENT_KEYS) {
    assert(Object.prototype.hasOwnProperty.call(document, key), `missing canonical BracketDocument field: ${key}`);
  }
}

function verifyRoundTrip({ userId, saved, loaded }) {
  verifyCanonicalBracketDocument(saved);
  verifyCanonicalBracketDocument(loaded);

  assert(saved.userId === userId, "saved document userId does not match signed-in user");
  assert(loaded.userId === userId, "loaded document userId does not match signed-in user");
  assert(loaded.tournamentId === SMOKE_TOURNAMENT_ID, "loaded tournamentId mismatch");
  assert(loaded.gameId === SMOKE_GAME_ID, "loaded gameId mismatch");
  assert(loaded.visibility === "private", "loaded visibility must remain private");
  assert(loaded.status === "draft", "loaded status must remain draft");

  const savedPick = saved.picksBySlot?.["SMOKE-R32-1"];
  const loadedPick = loaded.picksBySlot?.["SMOKE-R32-1"];

  assert(savedPick, "saved smoke pick is missing");
  assert(loadedPick, "loaded smoke pick is missing");
  const savedTeamId = savedPick.pick?.teamId || savedPick.teamId;
  const loadedTeamId = loadedPick.pick?.teamId || loadedPick.teamId;

  assert(savedTeamId === "FRA", "saved smoke pick teamId mismatch");
  assert(loadedTeamId === "FRA", "loaded smoke pick teamId mismatch");
  assert(savedTeamId === loadedTeamId, "round-trip picksBySlot teamId mismatch");
  assert(savedPick.slotId === loadedPick.slotId, "round-trip picksBySlot slotId mismatch");
}

async function runSupabaseBracketStoreSmokeTest() {
  if (!shouldRunSupabaseBracketStoreSmokeTest()) {
    return { skipped: true };
  }

  console.info("[SupabaseBracketStoreSmokeTest] starting dev-only smoke test");

  const store = new SupabaseBracketStore({
    tournamentId: SMOKE_TOURNAMENT_ID,
    gameId: SMOKE_GAME_ID,
  });

  const user = await store.requireSignedInUser();
  const smokeBracket = buildSmokeBracketDocument(user.id);
  const saved = await store.saveUserBracket(smokeBracket);
  const loaded = await store.loadUserBracket(user.id, {
    tournamentId: SMOKE_TOURNAMENT_ID,
    gameId: SMOKE_GAME_ID,
  });

  verifyRoundTrip({ userId: user.id, saved, loaded });

  console.info("[SupabaseBracketStoreSmokeTest] PASS", {
    userId: user.id,
    tournamentId: loaded.tournamentId,
    gameId: loaded.gameId,
    pickCount: Object.keys(loaded.picksBySlot || {}).length,
  });

  return {
    skipped: false,
    passed: true,
    userId: user.id,
    tournamentId: loaded.tournamentId,
    gameId: loaded.gameId,
  };
}

function installSupabaseBracketStoreSmokeTest() {
  if (!shouldRunSupabaseBracketStoreSmokeTest()) {
    return;
  }

  runSupabaseBracketStoreSmokeTest().catch((error) => {
    console.error("[SupabaseBracketStoreSmokeTest] FAIL", error);
  });
}

export {
  DEV_SMOKE_QUERY_FLAG,
  buildSmokeBracketDocument,
  installSupabaseBracketStoreSmokeTest,
  runSupabaseBracketStoreSmokeTest,
  shouldRunSupabaseBracketStoreSmokeTest,
};
