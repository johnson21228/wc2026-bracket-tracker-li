import { getSharedSupabaseClient } from "../services/SupabaseClient.js";

const USER_BRACKETS_TABLE = "user_brackets";
const PROFILES_TABLE = "profiles";

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

function normalizeBracketRow(row, profileByUserId) {
  const userId = row?.user_id || "";
  const bracketJson = row?.bracket_json && typeof row.bracket_json === "object"
    ? row.bracket_json
    : {};
  const picksBySlot = picksBySlotFromBracket(bracketJson);
  const picksCount = Object.keys(picksBySlot).length;
  const profile = profileByUserId.get(userId) || null;

  return {
    userId,
    publicPlayerName: publicPlayerNameFor({ profile, userId }),
    picksBySlot,
    picksCount,
    groupPoints: 0,
    knockoutPoints: 0,
    tiebreakerScore: 0,
    total: 0,
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
      .eq("bracket_kind", "player")
      .order("updated_at", { ascending: false });

    if (error) throw error;

    const bracketRows = Array.isArray(data) ? data : [];
    const userIds = Array.from(new Set(
      bracketRows
        .map((row) => row?.user_id)
        .filter((userId) => typeof userId === "string" && userId.length > 0)
    ));

    const profileByUserId = await fetchProfilesByUserId(supabaseClient, userIds);

    return bracketRows.map((row) => normalizeBracketRow(row, profileByUserId));
  }

  return { listPlayerStandings, canReadStoredPicks };
}
