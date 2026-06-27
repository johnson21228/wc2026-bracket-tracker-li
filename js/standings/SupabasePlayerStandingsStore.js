import { getSharedSupabaseClient } from "../services/SupabaseClient.js";

const USER_BRACKETS_TABLE = "user_brackets";
const PROFILES_TABLE = "profiles";
const ADMIN_OFFICIAL_USER_ID = "Admin_/official";
const ADMIN_OFFICIAL_TRUTH_SOURCE = "Supabase:Admin_/official";

function safeText(value, fallback = "") {
  const text = String(value || "").trim().replace(/\s+/g, " ");
  return text || fallback;
}

function publicPlayerNameFor({ profile, userId }) {
  return safeText(profile?.display_name, "") || `Player ${String(userId || "").slice(0, 6)}`;
}

function picksBySlotFromBracket(bracketJson) {
  const picksBySlot = bracketJson?.picksBySlot;
  return picksBySlot && typeof picksBySlot === "object" && !Array.isArray(picksBySlot)
    ? picksBySlot
    : {};
}

function pickTeamIdFromRecord(record) {
  if (typeof record === "string") return record;
  if (!record || typeof record !== "object") return "";
  return record?.pick?.kind === "team"
    ? String(record.pick.teamId || "")
    : String(record?.teamId || record?.team_id || "");
}

function isR32EntrantRecord(slotId, record) {
  const round = String(record?.round || "").toUpperCase();
  const kind = String(record?.kind || "").toLowerCase();
  return round === "R32" || round === "R32_ENTRANT" || kind === "entrant" || /^L-R32-|^R-R32-/i.test(String(slotId || ""));
}

function paddedSlotNumber(value) {
  return String(value).padStart(2, "0");
}

function feederSlotIdsForSlot(slotId) {
  const id = String(slotId || "").toUpperCase();

  let match = id.match(/^([LR])-R16-(\d{2})$/);
  if (match) {
    const side = match[1];
    const index = Number(match[2]);
    return [
      `${side}-R32-${paddedSlotNumber(index * 2 - 1)}`,
      `${side}-R32-${paddedSlotNumber(index * 2)}`,
    ];
  }

  match = id.match(/^([LR])-QF-(\d{2})$/);
  if (match) {
    const side = match[1];
    const index = Number(match[2]);
    return [
      `${side}-R16-${paddedSlotNumber(index * 2 - 1)}`,
      `${side}-R16-${paddedSlotNumber(index * 2)}`,
    ];
  }

  match = id.match(/^([LR])-SF-(\d{2})$/);
  if (match) {
    const side = match[1];
    const index = Number(match[2]);
    return [
      `${side}-QF-${paddedSlotNumber(index * 2 - 1)}`,
      `${side}-QF-${paddedSlotNumber(index * 2)}`,
    ];
  }

  if (id === "FINAL-LEFT") return ["L-SF-01", "L-SF-02"];
  if (id === "FINAL-RIGHT") return ["R-SF-01", "R-SF-02"];
  if (id === "CHAMPION") return ["FINAL-LEFT", "FINAL-RIGHT"];

  return [];
}

function scoreWeightForSlot(slotId) {
  const id = String(slotId || "").toUpperCase();

  if (/^[LR]-R16-\d{2}$/.test(id)) return 1;
  if (/^[LR]-QF-\d{2}$/.test(id)) return 2;
  if (/^[LR]-SF-\d{2}$/.test(id)) return 4;
  if (id === "FINAL-LEFT" || id === "FINAL-RIGHT") return 8;
  if (id === "CHAMPION") return 16;

  return 0;
}

function scoringSlotIds(playerPicksBySlot, officialTruthPicksBySlot) {
  return Array.from(new Set([
    ...Object.keys(playerPicksBySlot || {}),
    ...Object.keys(officialTruthPicksBySlot || {}),
  ])).filter((slotId) => scoreWeightForSlot(slotId) > 0);
}

function canTeamStillReachSlot(teamId, slotId, officialTruthPicksBySlot, visiting = new Set()) {
  const candidateTeamId = String(teamId || "").trim();
  const currentSlotId = String(slotId || "").toUpperCase();

  if (!candidateTeamId || !currentSlotId) return false;
  if (visiting.has(currentSlotId)) return false;

  const officialTeamId = pickTeamIdFromRecord(officialTruthPicksBySlot?.[currentSlotId]);
  if (officialTeamId) return officialTeamId === candidateTeamId;

  const feederSlotIds = feederSlotIdsForSlot(currentSlotId);
  if (!feederSlotIds.length) return true;

  const nextVisiting = new Set(visiting);
  nextVisiting.add(currentSlotId);

  return feederSlotIds.some((feederSlotId) => (
    canTeamStillReachSlot(candidateTeamId, feederSlotId, officialTruthPicksBySlot, nextVisiting)
  ));
}

function scoreAgainstAdminOfficialTruth(playerPicksBySlot, officialTruthPicksBySlot) {
  let score = 0;
  let maxPossible = 0;
  let scoredOfficialSlots = 0;

  for (const slotId of scoringSlotIds(playerPicksBySlot, officialTruthPicksBySlot)) {
    const officialRecord = officialTruthPicksBySlot?.[slotId];
    if (isR32EntrantRecord(slotId, officialRecord)) continue;

    const weight = scoreWeightForSlot(slotId);
    const officialTeamId = pickTeamIdFromRecord(officialRecord);
    const playerTeamId = pickTeamIdFromRecord(playerPicksBySlot?.[slotId]);

    if (officialTeamId) scoredOfficialSlots += 1;
    if (!playerTeamId) continue;

    if (officialTeamId) {
      if (playerTeamId === officialTeamId) {
        score += weight;
        maxPossible += weight;
      }
      continue;
    }

    if (canTeamStillReachSlot(playerTeamId, slotId, officialTruthPicksBySlot)) {
      maxPossible += weight;
    }
  }

  return {
    score,
    maxPossible,
    groupPoints: score,
    knockoutPoints: maxPossible,
    scoredOfficialSlots,
    total: score,
  };
}

function isAdminOfficialTruthRow(row) {
  const bracketJson = row?.bracket_json && typeof row.bracket_json === "object" ? row.bracket_json : {};
  return row?.user_id === ADMIN_OFFICIAL_USER_ID
    || row?.bracket_kind === "official"
    || bracketJson.userId === ADMIN_OFFICIAL_USER_ID
    || bracketJson.bracketKind === "official";
}

function normalizeAdminOfficialTruth(row) {
  const bracketJson = row?.bracket_json && typeof row.bracket_json === "object" ? row.bracket_json : {};
  const picksBySlot = picksBySlotFromBracket(bracketJson);
  return {
    userId: ADMIN_OFFICIAL_USER_ID,
    bracketKind: "official",
    picksBySlot,
    source: ADMIN_OFFICIAL_TRUTH_SOURCE,
    officialResultsTruthSource: ADMIN_OFFICIAL_TRUTH_SOURCE,
    partialOfficialTruthAllowed: true,
  };
}

function normalizeBracketRow(row, profileByUserId, officialTruth = null) {
  const userId = row?.user_id || "";
  const bracketJson = row?.bracket_json && typeof row.bracket_json === "object"
    ? row.bracket_json
    : {};
  const picksBySlot = picksBySlotFromBracket(bracketJson);
  const picksCount = Object.keys(picksBySlot).length;
  const profile = profileByUserId.get(userId) || null;
  const officialTruthPicksBySlot = officialTruth?.picksBySlot || {};
  const score = scoreAgainstAdminOfficialTruth(picksBySlot, officialTruthPicksBySlot);

  return {
    userId,
    publicPlayerName: publicPlayerNameFor({ profile, userId }),
    picksBySlot,
    picksCount,
    score: score.score,
    maxPossible: score.maxPossible,
    groupPoints: score.groupPoints,
    knockoutPoints: score.knockoutPoints,
    tiebreakerScore: score.scoredOfficialSlots,
    total: score.total,
    officialTruthPicksBySlot,
    officialResultsTruthSource: officialTruth?.officialResultsTruthSource || "",
    officialResultsTruthUserId: officialTruth?.userId || "",
    status: row?.status || bracketJson?.status || "draft",
    visibility: row?.visibility || bracketJson?.visibility || "private",
    bracketKind: row?.bracket_kind || bracketJson?.bracketKind || "player",
    updatedAt: row?.updated_at || bracketJson?.updatedAt || "",
  };
}

async function fetchProfilesByUserId(supabase, userIds) {
  if (!userIds.length) return new Map();

  const { data, error } = await supabase
    .from(PROFILES_TABLE)
    .select("id, display_name")
    .in("id", userIds);

  if (error) {
    console.warn("[SupabasePlayerStandingsStore] profiles unavailable", error);
    return new Map();
  }

  return new Map((data || []).map((profile) => [profile.id, profile]));
}

export function createSupabasePlayerStandingsStore({
  supabaseClient = getSharedSupabaseClient(),
  tournamentId = "wc2026",
  gameId = "game1",
} = {}) {
  async function canReadStoredPicks() {
    if (!supabaseClient) return false;

    const { error } = await supabaseClient
      .from(USER_BRACKETS_TABLE)
      .select("user_id", { count: "exact", head: true })
      .eq("tournament_id", tournamentId)
      .eq("game_id", gameId);

    return !error;
  }

  async function listPlayerStandings() {
    if (!supabaseClient) return [];

    const { data, error } = await supabaseClient
      .from(USER_BRACKETS_TABLE)
      .select("user_id, tournament_id, game_id, status, visibility, bracket_kind, bracket_json, updated_at")
      .eq("tournament_id", tournamentId)
      .eq("game_id", gameId)
      .in("bracket_kind", ["player", "official"])
      .order("updated_at", { ascending: false });

    if (error) throw error;

    const allRows = Array.isArray(data) ? data : [];
    const officialTruth = normalizeAdminOfficialTruth(allRows.find(isAdminOfficialTruthRow) || null);
    const bracketRows = allRows.filter((row) => !isAdminOfficialTruthRow(row));
    const userIds = Array.from(new Set(
      bracketRows
        .map((row) => row?.user_id)
        .filter((userId) => typeof userId === "string" && userId.length > 0)
    ));

    const profileByUserId = await fetchProfilesByUserId(supabaseClient, userIds);

    return bracketRows.map((row) => normalizeBracketRow(row, profileByUserId, officialTruth));
  }

  return { listPlayerStandings, canReadStoredPicks };
}
