import { teamPickValue } from "../model/PickValue.js";
import { hydrateOfficialR32Occupants } from "../model/UserBracketModel.js";
const STORAGE_KEY = "wc2026.game1.cleanMvcPicks.v1";
const PICK_SNAPSHOT_APP_ID = "wc2026.braketeeringPub.picks";
const ROUND_ORDER = ["R32", "R16", "QF", "SF", "SF_WINNER", "CHAMPION", "FINAL_FOUR"];
const BOARD_NATIVE_SIZE = Object.freeze({ width: 1536, height: 1024 });
const GROUP_IDS = Object.freeze(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]);
const CENTER_FINAL_FOUR_SLOT_ID = "CENTER-FINAL-FOUR";
const FINAL_FOUR_PICK_SLOT_DEFS = Object.freeze([
  {
    slotId: "FINAL-LEFT",
    round: "SF_WINNER",
    kind: "winner",
    displayLabel: "Left SF Winner",
    sourceSlotIds: ["L-SF-01", "L-SF-02"],
  },
  {
    slotId: "FINAL-RIGHT",
    round: "SF_WINNER",
    kind: "winner",
    displayLabel: "Right SF Winner",
    sourceSlotIds: ["R-SF-01", "R-SF-02"],
  },
  {
    slotId: "CHAMPION",
    round: "CHAMPION",
    kind: "winner",
    displayLabel: "Final Winner",
    sourceSlotIds: ["FINAL-LEFT", "FINAL-RIGHT"],
  },
  {
    slotId: "THIRD-PLACE-WINNER",
    round: "THIRD_PLACE",
    kind: "winner",
    displayLabel: "3rd Place Winner",
    sourceSlotIds: ["L-SF-01", "L-SF-02", "R-SF-01", "R-SF-02"],
  },
]);
const GROUP_RAIL_LABEL_RANGE = "Group A through Group L";

const DATA_URLS = Object.freeze({
  geometry: "data/geometry/gameboard_manifest.json",
  r32Bridge: "data/geometry/game1_fifa_slot_geometry_map.json",
  r32Logic: "data/model/fifa_r32_logical_slot_order.json",
  teams: "data/model/teams.json",
  groups: "data/groups_from_flags_images.json",
  currentStandings: "data/current/group_standings.json",
  currentMatches: "data/current/group_matches.json",
  currentHighlights: "data/current/match_highlights.json",
  knockoutMatches: "data/current/knockout_matches.json",
  game2FifaFinalR32Assignments: "data/game2_fifa_final_r32_assignments.json",
  officialTruth: "data/current/official_truth.json",
  officialKnockoutResults: "data/official_knockout_results.json",
  knockoutMatchDisplayMetadata: "data/knockout_match_display_metadata.json",
});

async function readJson(url) {
  const response = await fetch(url, { cache: "no-cache" });
  if (!response.ok) {
    throw new Error(`Could not load ${url}: ${response.status}`);
  }
  return response.json();
}

function normalizeTeamRecord(team) {
  if (!team) return null;
  const id = team.id || team.abbr || team.code;
  if (!id) return null;
  return {
    id,
    abbr: team.abbr || id,
    name: team.name || team.displayName || id,
    flag: team.flag || team.flagEmoji || "",
  };
}

function groupTeamsFromPayload(groupsPayload, teamById) {
  const groups = groupsPayload?.groups || {};
  const result = new Map();
  for (const [groupId, entries] of Object.entries(groups)) {
    result.set(groupId, (entries || []).map((entry) => {
      const id = entry.abbr || entry.id || entry.code;
      return normalizeTeamRecord(teamById.get(id) || entry);
    }).filter(Boolean));
  }
  return result;
}

function normalizeGame2FifaFinalR32AssignmentsPayload(payload, teamById) {
  if (payload?.meta?.source !== "fifa_final_truth_target") return new Map();
  const assignments = Array.isArray(payload.assignments) ? payload.assignments : [];
  const result = new Map();
  for (const assignment of assignments) {
    const slotId = String(assignment.slotId || "").trim();
    const teamId = String(assignment.teamId || "").trim();
    if (!slotId || !teamId) continue;
    const team = normalizeTeamRecord(teamById.get(teamId) || {
      id: teamId,
      abbr: assignment.abbr || teamId,
      name: assignment.label || assignment.name || teamId,
      flag: assignment.flag || "",
    });
    if (team) result.set(slotId, team);
  }
  return result;
}

function isVisualOnlyGeometrySlot(slot) {
  return slot?.slotId === CENTER_FINAL_FOUR_SLOT_ID || slot?.round === "FINAL_FOUR";
}

function pickSurfaceSlots(slots) {
  return slots.filter((slot) => !isVisualOnlyGeometrySlot(slot));
}

function sortSlots(slots) {
  return [...slots].sort((a, b) => {
    const round = ROUND_ORDER.indexOf(a.round) - ROUND_ORDER.indexOf(b.round);
    if (round !== 0) return round;
    const side = String(a.side || "").localeCompare(String(b.side || ""));
    if (side !== 0) return side;
    return Number(a.roundIndex || 0) - Number(b.roundIndex || 0);
  });
}

function uniqueTeams(teams) {
  const seen = new Set();
  const result = [];
  for (const team of teams) {
    if (!team || seen.has(team.id)) continue;
    seen.add(team.id);
    result.push(team);
  }
  return result;
}

function sidePrefix(side) {
  return side === "right" ? "R" : "L";
}

function twoDigit(number) {
  return String(number).padStart(2, "0");
}

function slotIdFor(round, side, index) {
  return `${sidePrefix(side)}-${round}-${twoDigit(index)}`;
}

function buildDependencyMap(slotsById, r32BridgeSlots) {
  const dependencies = new Map();

  const bridgeByMatch = new Map();
  for (const bridge of r32BridgeSlots) {
    const list = bridgeByMatch.get(bridge.matchupId) || [];
    list.push(bridge.geometrySlotId);
    bridgeByMatch.set(bridge.matchupId, list);
  }

  for (const bridge of r32BridgeSlots) {
    if (bridge.matchupPosition !== "top") continue;
    const matchNumber = Number(String(bridge.matchupId || "").match(/(\d+)$/)?.[1]);
    if (!Number.isFinite(matchNumber)) continue;
    const r16Id = slotIdFor("R16", bridge.side, matchNumber);
    const feederIds = bridgeByMatch.get(bridge.matchupId) || [];
    if (slotsById.has(r16Id) && feederIds.length === 2) {
      dependencies.set(r16Id, feederIds);
    }
  }

  for (const side of ["left", "right"]) {
    for (let index = 1; index <= 4; index += 1) {
      const qfId = slotIdFor("QF", side, index);
      const feeders = [slotIdFor("R16", side, index * 2 - 1), slotIdFor("R16", side, index * 2)];
      if (slotsById.has(qfId) && feeders.every((slotId) => slotsById.has(slotId))) {
        dependencies.set(qfId, feeders);
      }
    }

    for (let index = 1; index <= 2; index += 1) {
      const sfId = slotIdFor("SF", side, index);
      const feeders = [slotIdFor("QF", side, index * 2 - 1), slotIdFor("QF", side, index * 2)];
      if (slotsById.has(sfId) && feeders.every((slotId) => slotsById.has(slotId))) {
        dependencies.set(sfId, feeders);
      }
    }
  }

  const FINAL_FOUR_PRECEDENT_CONSTRAINTS = Object.freeze({
    "FINAL-LEFT": Object.freeze(["L-SF-01", "L-SF-02"]),
    "FINAL-RIGHT": Object.freeze(["R-SF-01", "R-SF-02"]),
    "CHAMPION": Object.freeze(["FINAL-LEFT", "FINAL-RIGHT"]),
  });

  for (const [slotId, feederIds] of Object.entries(FINAL_FOUR_PRECEDENT_CONSTRAINTS)) {
    if (slotsById.has(slotId)) {
      dependencies.set(slotId, feederIds.filter((feederId) => slotsById.has(feederId)));
    }
  }

  return dependencies;
}

function pickFromStorage() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    const parsed = raw ? JSON.parse(raw) : {};
    return parsed && typeof parsed === "object" ? parsed : {};
  } catch {
    return {};
  }
}

function saveToStorage(picks) {
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(picks));
  } catch {
    // Local storage is a convenience, not model truth.
  }
}

function legacyPicksFromRemoteBracketDocument(bracket) {
  const picksBySlot = bracket?.picksBySlot && typeof bracket.picksBySlot === "object" ? bracket.picksBySlot : {};
  const result = {};

  for (const [slotId, record] of Object.entries(picksBySlot)) {
    const teamId = record?.pick?.kind === "team"
      ? record.pick.teamId
      : record?.teamId;
    if (teamId) result[slotId] = teamId;
  }

  return result;
}

function failClosedAdminOfficialR32TruthDocument(reason = "unavailable") {
  return {
    userId: "Admin_/official",
    bracketKind: "official",
    picksBySlot: {},
    officialR32AuthoritySource: "Supabase:Admin_/official",
    officialResultsTruthSource: "Supabase:Admin_/official",
    source: "Supabase:Admin_/official",
    authority: "Admin_/official",
    r32TruthUnavailable: true,
    failClosed: true,
    reason,
  };
}

function normalizeSiteOfficialTruthDocument(payload = {}) {
  const picksBySlot = payload?.picksBySlot && typeof payload.picksBySlot === "object" && !Array.isArray(payload.picksBySlot)
    ? payload.picksBySlot
    : {};

  return {
    schemaVersion: Number(payload?.schemaVersion || 1),
    userId: "site-owned-official-truth",
    tournamentId: payload?.tournamentId || "wc2026",
    gameId: payload?.gameId || "game1",
    bracketKind: "official",
    picksBySlot,
    officialR32AuthoritySource: "site/data/current/official_truth.json",
    officialResultsTruthSource: "site/data/current/official_truth.json",
    source: "site-owned-official-truth",
    authority: "site-owned-official-truth",
    partialOfficialTruthAllowed: true,
  };
}


function pickRecordFromOfficialKnockoutResult(result = {}) {
  const slotId = String(result.siteWinnerSlotId || "").trim();
  const winnerTeamId = String(result.winnerTeamId || "").trim();
  if (!slotId || !winnerTeamId) return null;

  return {
    slotId,
    teamId: winnerTeamId,
    teamCode: winnerTeamId,
    teamName: result.winnerTeamName || winnerTeamId,
    kind: "winner",
    round: "OFFICIAL_KNOCKOUT_RESULT",
    source: "site-owned-official-knockout-results",
    sourceLabel: result.resultLabel || `${result.winnerTeamName || winnerTeamId} advanced`,
    officialTruth: true,
    result,
    pick: {
      kind: "team",
      teamId: winnerTeamId,
    },
  };
}

function mergeOfficialKnockoutResultsIntoDocument(document, resultsPayload = {}) {
  const matches = Array.isArray(resultsPayload?.matches) ? resultsPayload.matches : [];
  const resultPicks = {};

  for (const result of matches) {
    const record = pickRecordFromOfficialKnockoutResult(result);
    if (record) resultPicks[record.slotId] = record;
  }

  return {
    ...document,
    picksBySlot: {
      ...(document?.picksBySlot || {}),
      ...resultPicks,
    },
    officialResultsTruthSource: "site/data/official_knockout_results.json",
  };
}

function normalizeKnockoutDisplayMetadata(payload = {}) {
  const byWinnerSlot = new Map();
  const matches = Array.isArray(payload?.matches) ? payload.matches : [];

  for (const match of matches) {
    const siteWinnerSlotId = String(match.siteWinnerSlotId || "").trim();
    if (!siteWinnerSlotId) continue;
    byWinnerSlot.set(siteWinnerSlotId, {
      matchId: String(match.matchId || match.matchNumber || "").trim(),
      matchNumber: Number(match.matchNumber || match.matchId || 0),
      round: match.round || "",
      siteWinnerSlotId,
      siteSlotPair: Array.isArray(match.siteSlotPair) ? match.siteSlotPair : [],
      fixtureLabel: match.fixtureLabel || "",
      homeSlot: match.homeSlot || "",
      awaySlot: match.awaySlot || "",
      date: match.date || "",
      kickoffEt: match.kickoffEt || "",
      kickoffIso: match.kickoffIso || "",
      venue: match.venue || "",
      city: match.city || "",
      extendedHighlightsUrl: typeof match.extendedHighlightsUrl === "string" ? match.extendedHighlightsUrl : "",
    });
  }

  return byWinnerSlot;
}

function normalizeOfficialKnockoutResultsByWinnerSlot(resultsPayload = {}) {
  const byWinnerSlot = new Map();
  const matches = Array.isArray(resultsPayload?.matches) ? resultsPayload.matches : [];

  for (const result of matches) {
    const siteWinnerSlotId = String(result.siteWinnerSlotId || "").trim();
    if (siteWinnerSlotId) byWinnerSlot.set(siteWinnerSlotId, result);
  }

  return byWinnerSlot;
}


export async function createBracketModel({
  bracketStore = null,
  officialBracketStore = bracketStore,
  userId = "local-player",
  persistenceMode = "local",
  adminOfficialR32Editor = false,
  adminOfficialEditor = adminOfficialR32Editor,
} = {}) {
  const [
    geometry,
    r32Bridge,
    r32Logic,
    teamsPayload,
    groupsPayload,
    currentStandingsPayload,
    currentMatchesPayload,
    currentHighlightsPayload,
    knockoutMatchesPayload,
    game2FifaFinalR32AssignmentsPayload,
    officialTruthPayload,
    officialKnockoutResultsPayload,
    knockoutMatchDisplayMetadataPayload,
  ] = await Promise.all([
    readJson(DATA_URLS.geometry),
    readJson(DATA_URLS.r32Bridge),
    readJson(DATA_URLS.r32Logic),
    readJson(DATA_URLS.teams),
    readJson(DATA_URLS.groups),
    readJson(DATA_URLS.currentStandings),
    readJson(DATA_URLS.currentMatches),
    readJson(DATA_URLS.currentHighlights),
    readJson(DATA_URLS.knockoutMatches),
    readJson(DATA_URLS.game2FifaFinalR32Assignments),
    readJson(DATA_URLS.officialTruth),
    readJson(DATA_URLS.officialKnockoutResults),
    readJson(DATA_URLS.knockoutMatchDisplayMetadata),
  ]);

const FINAL_FOUR_PRECEDENT_CONSTRAINTS = Object.freeze({
  "FINAL-LEFT": Object.freeze(["L-SF-01", "L-SF-02"]),
  "FINAL-RIGHT": Object.freeze(["R-SF-01", "R-SF-02"]),
  "CHAMPION": Object.freeze(["FINAL-LEFT", "FINAL-RIGHT"]),
});

  const nativeSize = geometry.nativeSizePx || BOARD_NATIVE_SIZE;
  const slots = sortSlots(geometry.slots || []);
  const slotsById = new Map(slots.map((slot) => [slot.slotId, slot]));
  const teamById = new Map(Object.values(teamsPayload.teams || {}).map((team) => {
    const normalized = normalizeTeamRecord(team);
    return [normalized.id, normalized];
  }));
  const groupsById = groupTeamsFromPayload(groupsPayload, teamById);
  const currentStandingsById = new Map(Object.entries(currentStandingsPayload.groups || {}));
  const currentMatchesByGroupId = new Map();
  for (const match of currentMatchesPayload.matches || []) {
    const groupId = String(match.groupId || "").toUpperCase();
    const list = currentMatchesByGroupId.get(groupId) || [];
    list.push(match);
    currentMatchesByGroupId.set(groupId, list);
  }
  const currentHighlightsByMatchId = new Map(Object.entries(currentHighlightsPayload.highlights || {}));
  const knockoutMatches = [...(knockoutMatchesPayload.matches || [])];
  const knockoutMatchesById = new Map(knockoutMatches.map((match) => [String(match.match_id || match.matchNumber || match.match_number), match]));
  const knockoutDisplayMetadataByWinnerSlotId = normalizeKnockoutDisplayMetadata(knockoutMatchDisplayMetadataPayload);
  const officialKnockoutResultsByWinnerSlotId = normalizeOfficialKnockoutResultsByWinnerSlot(officialKnockoutResultsPayload);
  const r32LogicByGeometryId = new Map();
  const r32LogicByFifaId = new Map((r32Logic.slots || []).map((slot) => [slot.fifaSlotId, slot]));
  for (const bridge of r32Bridge.slots || []) {
    const logic = r32LogicByFifaId.get(bridge.fifaSlotId);
    if (logic) {
      r32LogicByGeometryId.set(bridge.geometrySlotId, { ...logic, ...bridge });
    }
  }

  const dependencyMap = buildDependencyMap(slotsById, r32Bridge.slots || []);
  const game2FifaFinalR32AssignmentsBySlotId = normalizeGame2FifaFinalR32AssignmentsPayload(game2FifaFinalR32AssignmentsPayload, teamById);
  const centerFinalFourSlot = slotsById.get(CENTER_FINAL_FOUR_SLOT_ID) || null;
  const finalFourSlotsById = new Map(FINAL_FOUR_PICK_SLOT_DEFS.map((slot) => [
    slot.slotId,
    {
      ...slot,
      sitePickId: slot.slotId,
      boundsPx: centerFinalFourSlot?.boundsPx || null,
      side: "center",
      source: "canonical-bracket-document-runtime",
    },
  ]));
  const remotePersistenceActive = persistenceMode === "supabase" && bracketStore;
  let remoteBracketDocument = null;
  let officialBracketDocument = null;
  let remoteSavePromise = Promise.resolve();
  let officialSavePromise = Promise.resolve();
  let picks = {};
  let officialPicks = {};
  const urlParams = new URLSearchParams(window.location.search);
  const adminOfficialEditorFromUrl = Boolean(
    urlParams.get("adminOfficialEditor") === "1" ||
    urlParams.get("adminOfficial") === "1" ||
    urlParams.get("adminOfficialR32Editor") === "1"
  );

  // Admin mode is a runtime/UI authority flag. Do not make it depend on a specific store method.
  // Store method availability is checked only when saving.
  const adminOfficialEditorActive = false;
  const adminOfficialR32EditorActive = false;

  if (remotePersistenceActive) {
    try {
      remoteBracketDocument = await bracketStore.loadUserBracket(userId);
      picks = clearUnknownTeamPicks(legacyPicksFromRemoteBracketDocument(remoteBracketDocument), "player bracket");
      console.info("[WC2026 SupabaseBracketStore] loaded remote bracket picks", {
        userId,
        bracketKind: remoteBracketDocument?.bracketKind || "player",
        pickCount: Object.keys(picks).length,
      });
    } catch (error) {
      console.error("[WC2026 SupabaseBracketStore] remote bracket load failed", error);
      picks = {};
    }
  } else {
    // Join-required runtime: signed-out players must not see stale cached local picks.
    picks = {};
  }

  officialBracketDocument = mergeOfficialKnockoutResultsIntoDocument(
    normalizeSiteOfficialTruthDocument(officialTruthPayload),
    officialKnockoutResultsPayload
  );
  officialPicks = clearUnknownTeamPicks(
    legacyPicksFromRemoteBracketDocument(officialBracketDocument),
    "site-owned official truth"
  );
  console.info("[WC2026 OfficialResults] loaded site-owned official truth picks", {
    source: officialBracketDocument.officialResultsTruthSource,
    pickCount: Object.keys(officialPicks).length,
  });

  picks = hydrateOnlySupabaseAdminR32IntoPlayerPicks(picks);

  function getTeam(teamId) {
    return teamById.get(teamId) || null;
  }

  function teamObjectFromPickRecord(record) {
    const pick = record?.pick && typeof record.pick === "object" ? record.pick : {};
    const teamId = pick.kind === "team" ? pick.teamId : record?.teamId;
    const normalizedTeamId = String(teamId || "").trim();
    if (!normalizedTeamId) return null;

    const indexedTeam = getTeam(normalizedTeamId);
    if (indexedTeam) return indexedTeam;

    const label = pick.label
      || pick.name
      || record?.teamLabel
      || record?.label
      || record?.name
      || normalizedTeamId;

    const flag = pick.flag || record?.flag || record?.emoji || "";

    return {
      id: normalizedTeamId,
      teamId: normalizedTeamId,
      name: label,
      shortName: label,
      label,
      displayName: label,
      flag,
      emoji: flag,
      source: "remote-pick-record-fallback",
    };
  }

  function teamObjectFromDocumentPick(document, slotId) {
    return teamObjectFromPickRecord(document?.picksBySlot?.[slotId]);
  }


  function knownTeamForPersistedPick({ source, slotId, teamId }) {
    const normalizedTeamId = String(teamId || "").trim();
    if (!normalizedTeamId) return null;

    const team = getTeam(normalizedTeamId);
    if (team) return team;

    console.error(`[WC2026 LI FAIL] ${source} pick for ${slotId} references undefined team id "${normalizedTeamId}". Pick has been cleared; user must pick again.`, {
      source,
      slotId,
      teamId: normalizedTeamId,
      knownTeamIds: [...teamById.keys()].slice(0, 120),
    });
    return null;
  }


  function persistedOfficialTeam(slotId) {
    return knownTeamForPersistedPick({
      source: "Admin_/official R32 authority",
      slotId,
      teamId: officialPicks[slotId] || (teamObjectFromDocumentPick(officialBracketDocument, slotId)?.id || ""),
    });
  }

  function persistedPlayerTeam(slotId) {
    return knownTeamForPersistedPick({
      source: "player bracket",
      slotId,
      teamId: picks[slotId] || (teamObjectFromDocumentPick(remoteBracketDocument, slotId)?.id || ""),
    });
  }

  function clearUnknownTeamPicks(sourcePicks = {}, source = "persisted bracket") {
    const cleaned = {};
    const removed = [];

    for (const [slotId, teamId] of Object.entries(sourcePicks || {})) {
      const normalizedTeamId = String(teamId || "").trim();
      if (!normalizedTeamId) continue;

      if (getTeam(normalizedTeamId)) {
        cleaned[slotId] = normalizedTeamId;
      } else {
        removed.push({ slotId, teamId: normalizedTeamId });
      }
    }

    if (removed.length) {
      console.error(`[WC2026 LI FAIL] cleared ${removed.length} ${source} picks with undefined canonical team IDs`, {
        removed,
        knownTeamIds: [...teamById.keys()].slice(0, 120),
      });
    }

    return cleaned;
  }

  function isR32DisplaySlot(slotId) {
    return slotsById.get(slotId)?.round === "R32";
  }

  function stripR32OccupantsFromPlayerPicks(sourcePicks = {}) {
    return Object.fromEntries(
      Object.entries(sourcePicks || {}).filter(([slotId]) => !isR32DisplaySlot(slotId))
    );
  }

  function hydrateOnlySupabaseAdminR32IntoPlayerPicks(sourcePicks = {}) {
    const playerOwnedPicks = stripR32OccupantsFromPlayerPicks(sourcePicks);
    const canonicalPickSlots = allPickSlots();
    const picksBySlot = Object.fromEntries(
      canonicalPickSlots.map((slot) => [slot.slotId, pickRecordForRemoteSlot(slot, playerOwnedPicks[slot.slotId])])
    );
    const hydrated = hydrateOfficialR32Occupants({
      bracket: {
        schemaVersion: 1,
        userId,
        tournamentId: "wc2026",
        gameId: "game1",
        bracketKind: "player",
        picksBySlot,
      },
      bracketSlots: { canonicalPickSlots },
      teamsById: Object.fromEntries(teamById.entries()),
      officialR32: officialBracketDocument,
    });
    return legacyPicksFromRemoteBracketDocument(hydrated);
  }

  function selectedTeam(slotId) {
    const slot = slotsById.get(slotId);

    if (slot?.round === "R32") {
      return officialTeam(slotId) || persistedPlayerTeam(slotId);
    }

    if (adminOfficialEditorActive) {
      return persistedPlayerTeam(slotId) || officialTeam(slotId);
    }

    if (adminOfficialR32EditorActive && isR32DisplaySlot(slotId)) {
      return officialTeam(slotId) || persistedPlayerTeam(slotId);
    }

    return persistedPlayerTeam(slotId) || officialTeam(slotId);
  }

  function officialTeam(slotId) {
    const persisted = persistedOfficialTeam(slotId);
    if (persisted) return persisted;

    const result = officialKnockoutResultsByWinnerSlotId.get(String(slotId || "").trim());
    if (!result?.winnerTeamId) return null;

    return teamById.get(result.winnerTeamId) || null;
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

  function canTeamStillReachSlot(teamId, slotId, visiting = new Set()) {
    const candidateTeamId = String(teamId || "").trim();
    const currentSlotId = String(slotId || "").toUpperCase();

    if (!candidateTeamId || !currentSlotId) return false;
    if (visiting.has(currentSlotId)) return false;

    const truthTeam = officialTeam(currentSlotId);
    if (truthTeam) return truthTeam.id === candidateTeamId;

    const feederSlotIds = feederSlotIdsForSlot(currentSlotId);
    if (!feederSlotIds.length) return true;

    const nextVisiting = new Set(visiting);
    nextVisiting.add(currentSlotId);

    return feederSlotIds.some((feederSlotId) => canTeamStillReachSlot(candidateTeamId, feederSlotId, nextVisiting));
  }

  function officialPickComparisonForSlot(slotId, userTeam) {
    const truthTeam = officialTeam(slotId);
    if (!userTeam) return null;
    if (truthTeam) {
      return {
        state: userTeam.id === truthTeam.id ? "correct" : "incorrect",
        officialTeam: truthTeam,
      };
    }
    if (!canTeamStillReachSlot(userTeam.id, slotId)) {
      return {
        state: "unreachable",
        eliminated: true,
      };
    }
    return null;
  }

  function isEditingOfficialResults() {
    return adminOfficialEditorActive || remoteBracketDocument?.bracketKind === "official";
  }

  function fifaFinalR32Team(slotId) {
    return game2FifaFinalR32AssignmentsBySlotId.get(slotId) || null;
  }

  function game1R32FallbackTeam(slotId) {
    const slot = slotsById.get(slotId);
    if (slot?.round !== "R32") return null;
    return selectedTeam(slotId);
  }

  function resolvedGame2R32Team(slotId) {
    const fifaFinal = fifaFinalR32Team(slotId);
    if (fifaFinal) return { ...fifaFinal, game2R32Source: "fifa_final_assignment" };
    const fallback = game1R32FallbackTeam(slotId);
    if (fallback) return { ...fallback, game2R32Source: "game1_r32_fallback" };
    return null;
  }

  function getSlotDefinition(slotId) {
    return slotsById.get(slotId) || finalFourSlotsById.get(slotId) || null;
  }

  function allPickSlots() {
    return [...pickSurfaceSlots(slots), ...finalFourSlotsById.values()];
  }

  function pickRecordForRemoteSlot(slot, teamId) {
    const normalizedTeamId = String(teamId || "").trim();
    return {
      slotId: slot.slotId,
      kind: slot.kind || "winner",
      round: slot.round || "UNKNOWN",
      pick: normalizedTeamId ? teamPickValue(normalizedTeamId) : null,
      source: normalizedTeamId ? "user" : "empty",
    };
  }

  function pickRecordForOfficialR32Slot(slot, teamId) {
    const normalizedTeamId = String(teamId || "").trim();
    return {
      slotId: slot.slotId,
      kind: "entrant",
      round: "R32_ENTRANT",
      pick: normalizedTeamId ? teamPickValue(normalizedTeamId) : null,
      source: "Admin_/official",
      authority: "Admin_/official",
      playerAuthored: false,
      hydratedFrom: "Supabase:Admin_/official",
    };
  }

  function pickRecordForAdminOfficialSlot(slot, teamId) {
    if (slot.round === "R32") return pickRecordForOfficialR32Slot(slot, teamId);
    const normalizedTeamId = String(teamId || "").trim();
    return {
      slotId: slot.slotId,
      kind: slot.kind || "winner",
      round: slot.round || "UNKNOWN",
      pick: normalizedTeamId ? teamPickValue(normalizedTeamId) : null,
      source: "Admin_/official",
      authority: "Admin_/official",
      playerAuthored: false,
      officialTruth: true,
      hydratedFrom: "Supabase:Admin_/official",
    };
  }

  function buildAdminOfficialBracketDocument(reason = "admin-official-full-bracket-edit") {
    const now = new Date().toISOString();
    const previous = officialBracketDocument || {};
    const canonicalPickSlots = allPickSlots();
    const picksBySlot = Object.fromEntries(
      canonicalPickSlots.map((slot) => [slot.slotId, pickRecordForAdminOfficialSlot(slot, officialPicks[slot.slotId])])
    );

    return {
      ...previous,
      schemaVersion: Number(previous.schemaVersion || 1),
      userId: "Admin_/official",
      tournamentId: previous.tournamentId || "wc2026",
      gameId: previous.gameId || "game1",
      status: previous.status || "draft",
      lifecycleState: {
        ...(previous.lifecycleState || {}),
        source: "admin-official-full-bracket-editor-mode",
        lastSaveReason: reason,
      },
      phaseLocks: previous.phaseLocks || { r32LockedAt: null },
      picksBySlot,
      createdAt: previous.createdAt || now,
      updatedAt: now,
      submittedAt: previous.submittedAt || null,
      lockedAt: previous.lockedAt || null,
      visibility: "public",
      bracketKind: "official",
      officialR32AuthoritySource: "Supabase:Admin_/official",
      officialResultsTruthSource: "Supabase:Admin_/official",
      source: "Supabase:Admin_/official",
      authority: "Admin_/official",
    };
  }

  function buildAdminOfficialR32BracketDocument(reason = "admin-official-r32-edit") {
    return buildAdminOfficialBracketDocument(reason);
  }

  function persistAdminOfficialTruth(reason = "admin-official-full-bracket-edit") {
    if (!adminOfficialEditorActive) return;
    const bracketDocument = buildAdminOfficialBracketDocument(reason);
    officialBracketDocument = bracketDocument;
    officialSavePromise = officialSavePromise
      .catch(() => null)
      .then(() => officialBracketStore.saveAdminOfficialBracketTruth(bracketDocument))
      .then((saved) => {
        officialBracketDocument = saved || bracketDocument;
        officialPicks = legacyPicksFromRemoteBracketDocument(officialBracketDocument);
        console.info("[WC2026 AdminOfficialFullBracketEditor] saved Admin_/official full bracket truth", {
          userId: "Admin_/official",
          pickCount: Object.keys(officialPicks).length,
          reason,
        });
      })
      .catch((error) => {
        console.error("[WC2026 AdminOfficialFullBracketEditor] Admin_/official full bracket save failed", error);
      });
  }

  function persistAdminOfficialR32(reason = "admin-official-r32-edit") {
    if (adminOfficialEditorActive) {
      persistAdminOfficialTruth(reason);
      return;
    }
    if (!adminOfficialR32EditorActive) return;
    const bracketDocument = buildAdminOfficialR32BracketDocument(reason);
    officialBracketDocument = bracketDocument;
    officialSavePromise = officialSavePromise
      .catch(() => null)
      .then(() => officialBracketStore.saveOfficialR32BracketAuthority(bracketDocument))
      .then((saved) => {
        officialBracketDocument = saved || bracketDocument;
        officialPicks = legacyPicksFromRemoteBracketDocument(officialBracketDocument);
        console.info("[WC2026 AdminOfficialR32Editor] saved Admin_/official R32 truth", {
          userId: "Admin_/official",
          pickCount: Object.keys(officialPicks).length,
          reason,
        });
      })
      .catch((error) => {
        console.error("[WC2026 AdminOfficialR32Editor] Admin_/official R32 save failed", error);
      });
  }

  function buildRemoteBracketDocument(reason = "autosave") {
    const now = new Date().toISOString();
    const previous = remoteBracketDocument || {};
    picks = hydrateOnlySupabaseAdminR32IntoPlayerPicks(picks);
    const canonicalPickSlots = allPickSlots();
    const picksBySlot = Object.fromEntries(
      canonicalPickSlots.map((slot) => [slot.slotId, pickRecordForRemoteSlot(slot, picks[slot.slotId])])
    );

    const bracketDocument = {
      ...previous,
      schemaVersion: Number(previous.schemaVersion || 1),
      userId,
      tournamentId: previous.tournamentId || "wc2026",
      gameId: previous.gameId || "game1",
      status: previous.status || "draft",
      lifecycleState: {
        ...(previous.lifecycleState || {}),
        stage: "group",
        source: "dev-active-supabase-bracket-store",
        lastSaveReason: reason,
      },
      phaseLocks: previous.phaseLocks || { r32LockedAt: null },
      picksBySlot,
      createdAt: previous.createdAt || now,
      updatedAt: now,
      submittedAt: previous.submittedAt || null,
      lockedAt: previous.lockedAt || null,
      visibility: previous.visibility || "private",
      bracketKind: previous.bracketKind || "player",
    };

    return hydrateOfficialR32Occupants({
      bracket: bracketDocument,
      bracketSlots: { canonicalPickSlots },
      teamsById: Object.fromEntries(teamById.entries()),
      officialR32: officialBracketDocument,
    });
  }

  function persistPicks(reason = "autosave") {
    if (!remotePersistenceActive) {
      // Join-required runtime: player picks are not localStorage truth.
      return;
    }

    const bracketDocument = buildRemoteBracketDocument(reason);
    remoteBracketDocument = bracketDocument;
    remoteSavePromise = remoteSavePromise
      .catch(() => null)
      .then(() => bracketStore.saveUserBracket(bracketDocument))
      .then((saved) => {
        remoteBracketDocument = saved || bracketDocument;
        console.info("[WC2026 SupabaseBracketStore] saved remote bracket picks", {
          userId,
          pickCount: Object.keys(picks).length,
          reason,
        });
      })
      .catch((error) => {
        console.error("[WC2026 SupabaseBracketStore] remote bracket save failed", error);
      });
  }

  function teamsFromSlotIds(slotIds) {
    return uniqueTeams((slotIds || []).map((sourceSlotId) => selectedTeam(sourceSlotId)).filter(Boolean));
  }

  function loserFromSemifinal(finalSlotId, sourceSlotIds) {
    const winner = selectedTeam(finalSlotId);
    const teams = teamsFromSlotIds(sourceSlotIds);
    if (!winner || teams.length < 2) return null;
    return teams.find((team) => team.id !== winner.id) || null;
  }

  function getFinalFourChoices(slotId) {
    const finalFourSlot = finalFourSlotsById.get(slotId);
    if (!finalFourSlot) return [];

    if (slotId === "FINAL-LEFT" || slotId === "FINAL-RIGHT") {
      const teams = teamsFromSlotIds(finalFourSlot.sourceSlotIds);
      return teams.length === 2 ? teams : [];
    }

    if (slotId === "CHAMPION") {
      const teams = teamsFromSlotIds(["FINAL-LEFT", "FINAL-RIGHT"]);
      return teams.length === 2 ? teams : [];
    }

    if (slotId === "THIRD-PLACE-WINNER") {
      const leftLoser = loserFromSemifinal("FINAL-LEFT", ["L-SF-01", "L-SF-02"]);
      const rightLoser = loserFromSemifinal("FINAL-RIGHT", ["R-SF-01", "R-SF-02"]);
      return leftLoser && rightLoser ? uniqueTeams([leftLoser, rightLoser]) : [];
    }

    return [];
  }

  function resolvedGame2FeederTeam(slotId) {
    const slot = slotsById.get(slotId);
    if (slot?.round === "R32") return resolvedGame2R32Team(slotId);
    return selectedTeam(slotId);
  }

  function teamForFeederPath(slotId) {
    return resolvedGame2FeederTeam(slotId);
  }

  function getR32Choices(slotId) {
    // Normal players never get R32 choices; player-visible R32 mirrors Admin_/official only.
    // In Admin_/official editor mode, R32 choices reopen so the official truth document can be authored.
    if (officialBracketStore && !adminOfficialR32EditorActive) return [];
    const logic = r32LogicByGeometryId.get(slotId);
    if (!logic) return [];
    const groups = logic.groups || [];
    return uniqueTeams(groups.flatMap((groupId) => groupTeamsInCurrentOrder(groupId)));
  }

  function getKnockoutChoices(slotId) {
    // Final Four center-stack cells use the same dependency-map menu path as other knockout picks.
    const feeders = dependencyMap.get(slotId) || [];
    if (!feeders.length) return [];
    const feederTeams = feeders.map((feederId) => teamForFeederPath(feederId));
    if (feederTeams.some((team) => !team)) return [];
    return uniqueTeams(feederTeams);
  }

  function getChoices(slotId) {
    const finalFourSlot = finalFourSlotsById.get(slotId);
    if (finalFourSlot) return getFinalFourChoices(slotId);

    const slot = getSlotDefinition(slotId);
    if (!slot) return [];
    return slot.round === "R32" ? getR32Choices(slotId) : getKnockoutChoices(slotId);
  }

  function getFinalFourKnownFeederChoicesForValidity(slotId) {
    const finalFourSlot = finalFourSlotsById.get(slotId);
    if (!finalFourSlot) return [];

    if (slotId === "FINAL-LEFT" || slotId === "FINAL-RIGHT") {
      return teamsFromSlotIds(finalFourSlot.sourceSlotIds);
    }

    if (slotId === "CHAMPION") {
      return teamsFromSlotIds(["FINAL-LEFT", "FINAL-RIGHT"]);
    }

    if (slotId === "THIRD-PLACE-WINNER") {
      return uniqueTeams([
        loserFromSemifinal("FINAL-LEFT", ["L-SF-01", "L-SF-02"]),
        loserFromSemifinal("FINAL-RIGHT", ["R-SF-01", "R-SF-02"]),
      ].filter(Boolean));
    }

    return [];
  }

  function getKnownFeederChoicesForValidity(slot) {
    if (!slot || slot.round === "R32") return getChoices(slot?.slotId);

    if (finalFourSlotsById.has(slot.slotId)) {
      return getFinalFourKnownFeederChoicesForValidity(slot.slotId);
    }

    const feederSlotIds = dependencyMap.get(slot.slotId) || [];
    return uniqueTeams(feederSlotIds.map((feederId) => teamForFeederPath(feederId)).filter(Boolean));
  }

  function standingsEntryForTeam(groupId, teamId) {
    const standings = getGroupStandings(groupId);
    const targetId = String(teamId || "").toUpperCase();
    return (standings?.entries || []).find((entry) => {
      return [entry.teamId, entry.id, entry.abbr].some((value) => String(value || "").toUpperCase() === targetId);
    }) || null;
  }

  function ordinalRank(rank) {
    const numeric = Number(rank);
    if (!Number.isFinite(numeric)) return String(rank || "unknown rank");
    const suffix = numeric === 1 ? "st" : numeric === 2 ? "nd" : numeric === 3 ? "rd" : "th";
    return `${numeric}${suffix}`;
  }


  function duplicateR32Pick(slotId, teamId) {
    const sourcePicks = adminOfficialR32EditorActive ? officialPicks : picks;
    return Object.entries(sourcePicks).find(([otherSlotId, otherTeamId]) => {
      return otherSlotId !== slotId && otherTeamId === teamId && slotsById.get(otherSlotId)?.round === "R32";
    }) || null;
  }

  function pickValidityForSlot(slot, team) {
    if (!team) return { state: "empty", reason: "No pick has been made." };

    const choices = getChoices(slot.slotId);
    const knownFeederChoices = getKnownFeederChoicesForValidity(slot);
    const validityChoices = choices.length ? choices : knownFeederChoices;
    if (validityChoices.length && !validityChoices.some((choice) => choice.id === team.id)) {
      return {
        state: "invalid",
        reason: `${team.abbr || team.id} is not one of the current feeder teams for this winner slot.`,
      };
    }

    if (slot.round === "R32" && duplicateR32Pick(slot.slotId, team.id)) {
      return {
        state: "invalid",
        reason: `${team.abbr || team.id} is already assigned to another Round of 32 slot.`,
      };
    }


    return { state: "valid", reason: "Pick currently satisfies the slot rule." };
  }

  function isPickable(slotId) {
    return getChoices(slotId).length > 0;
  }

  function validatePick(slotId, teamId) {
    if (!teamId) return { valid: true };
    if (!slotsById.has(slotId)) {
      return { valid: false, reason: "Unknown bracket slot." };
    }
    if (!teamById.has(teamId)) {
      return { valid: false, reason: "Unknown team." };
    }
    const choices = getChoices(slotId);
    if (!choices.some((team) => team.id === teamId)) {
      return { valid: false, reason: "Team is outside this slot's source scope." };
    }
    return { valid: true };
  }

  function cascadeClearInvalidDescendants() {
    // Card 207: conflicts are rendered as warnings, not cleared as side effects.
    // Preserve downstream picks during import/refresh so user intent remains visible.
    return [];
  }

  function setPick(slotId, teamId) {
    window.BracketeeringPickLockdownPolicy?.assertPickChangeAllowed?.({ slotId, teamId });
    const slot = getSlotDefinition(slotId);
    if (!slot) {
      return { ok: false, reason: "Unknown bracket slot.", cleared: [] };
    }
    if (teamId && !teamById.has(teamId)) {
      return { ok: false, reason: "Unknown team.", cleared: [] };
    }
    if (adminOfficialEditorActive) {
      if (teamId) officialPicks[slotId] = teamId;
      else delete officialPicks[slotId];
      persistAdminOfficialTruth("set-admin-official-bracket-truth-pick");
      const official = selectedTeam(slotId);
      return {
        ok: true,
        cleared: [],
        pickValidity: pickValidityForSlot(slot, official),
        adminOfficialTruthEdited: true,
      };
    }
    if (isR32DisplaySlot(slotId)) {
      if (!adminOfficialR32EditorActive) {
        return { ok: false, reason: "R32 occupants are supplied by Admin_/official and cannot be edited by players.", cleared: [] };
      }
      if (teamId) officialPicks[slotId] = teamId;
      else delete officialPicks[slotId];
      persistAdminOfficialR32("set-admin-official-r32-pick");
      const official = selectedTeam(slotId);
      return { ok: true, cleared: [], pickValidity: pickValidityForSlot(slot, official), adminOfficialR32Edited: true };
    }
    if (teamId) picks[slotId] = teamId;
    else delete picks[slotId];
    persistPicks("setPick");
    const team = selectedTeam(slotId);
    return { ok: true, cleared: [], pickValidity: pickValidityForSlot(slot, team) };
  }

  function clearPick(slotId) {
    return setPick(slotId, null);
  }

  function clearAll() {
    if (adminOfficialEditorActive) {
      officialPicks = {};
      persistAdminOfficialTruth("clear-admin-official-bracket-truth");
      return { ok: true, cleared: allPickSlots().map((slot) => slot.slotId), adminOfficialTruthEdited: true };
    }
    picks = {};
    persistPicks("clearAll");
    return { ok: true, cleared: allPickSlots().map((slot) => slot.slotId) };
  }

  function exportPicksSnapshot() {
    return {
      app: PICK_SNAPSHOT_APP_ID,
      version: 1,
      exportedAt: new Date().toISOString(),
      picks: { ...picks },
    };
  }

  function importPicksSnapshot(snapshot) {
    const incoming = snapshot?.picks && typeof snapshot.picks === "object" ? snapshot.picks : snapshot;
    if (!incoming || typeof incoming !== "object" || Array.isArray(incoming)) {
      return { ok: false, reason: "Import file did not contain a picks object.", imported: 0, skipped: [] };
    }

    const previousPicks = { ...picks };
    const skipped = [];
    picks = {};

    for (const slot of allPickSlots()) {
      if (!Object.prototype.hasOwnProperty.call(incoming, slot.slotId)) continue;
      const teamId = String(incoming[slot.slotId] || "").trim();
      if (!teamId) continue;
      const validation = validatePick(slot.slotId, teamId);
      if (!validation.valid) {
        skipped.push({ slotId: slot.slotId, teamId, reason: validation.reason });
        continue;
      }
      picks[slot.slotId] = teamId;
      cascadeClearInvalidDescendants();
    }

    const cleared = cascadeClearInvalidDescendants();
    persistPicks("import");
    return {
      ok: true,
      imported: Object.keys(picks).length,
      skipped,
      cleared,
      previousPickCount: Object.keys(previousPicks).length,
    };
  }

  function normalizeGroupId(groupId) {
    return String(groupId || "").trim().toUpperCase().replace(/^GROUP\s+/, "");
  }

  function getGroupStandings(groupId) {
    return currentStandingsById.get(normalizeGroupId(groupId)) || null;
  }


  function groupTeamsInCurrentOrder(groupId) {
    const normalizedGroupId = normalizeGroupId(groupId);
    const fallbackTeams = [...(groupsById.get(normalizedGroupId) || [])];
    const standings = getGroupStandings(normalizedGroupId);
    const entries = standings?.entries || [];
    if (!entries.length) return fallbackTeams;

    const fallbackById = new Map(fallbackTeams.map((team) => [team.id, team]));
    const ordered = [];
    const seen = new Set();

    for (const entry of entries) {
      const teamId = entry.teamId || entry.id || entry.abbr;
      const team = fallbackById.get(teamId) || getTeam(teamId);
      if (!team || seen.has(team.id)) continue;
      ordered.push(team);
      seen.add(team.id);
    }

    for (const team of fallbackTeams) {
      if (!team || seen.has(team.id)) continue;
      ordered.push(team);
      seen.add(team.id);
    }

    return ordered;
  }

  function getGroupMatches(groupId) {
    return [...(currentMatchesByGroupId.get(normalizeGroupId(groupId)) || [])];
  }

  function getMatchHighlights(match) {
    if (!match) return null;

    return (
      currentHighlightsByMatchId.get(String(match.espnMatchId || "")) ||
      currentHighlightsByMatchId.get(String(match.matchId || "")) ||
      null
    );
  }

  function getKnockoutMatches() {
    return [...knockoutMatches];
  }

  function getKnockoutMatch(matchId) {
    return knockoutMatchesById.get(String(matchId)) || null;
  }

  function getThirdPlaceTable() {
    return [...(currentStandingsPayload.thirdPlaceTable || [])];
  }

  function getGroupContext(groupId) {
    const normalizedGroupId = normalizeGroupId(groupId);
    const standings = getGroupStandings(normalizedGroupId);
    const source = currentStandingsPayload.source || null;
    const matches = getGroupMatches(normalizedGroupId).map((match) => {
      const homeTeam = teamById.get(match.homeTeamId) || null;
      const awayTeam = teamById.get(match.awayTeamId) || null;
      const highlight = getMatchHighlights(match);
      const completed = match.status === "final" || match.status === "complete" || match.status === "completed";
      return {
        ...match,
        homeTeam,
        awayTeam,
        highlight,
        evidenceStatus: completed ? "completed" : "scheduled",
      };
    });
    const completedMatches = matches.filter((match) => match.evidenceStatus === "completed");
    const upcomingMatches = matches.filter((match) => match.evidenceStatus !== "completed");
    const sourceSummary = source
      ? `${source.provider || "Local snapshot"}${source.capturedAt ? ` captured ${source.capturedAt}` : ""}`
      : "Local checked-in standings snapshot.";
    return {
      groupId: normalizedGroupId,
      label: standings?.label || `Group ${normalizedGroupId}`,
      standings,
      entries: standings?.entries || [],
      matches,
      completedMatches,
      upcomingMatches,
      source,
      sourceSummary,
      thirdPlaceTable: getThirdPlaceTable(),
    };
  }

  function sourceTitleForSlot(slotId) {
    const slot = getSlotDefinition(slotId);
    const logic = r32LogicByGeometryId.get(slotId);
    if (!slot) return slotId;
    if (finalFourSlotsById.has(slotId)) return slot.displayLabel || slotId;

    if (logic?.qualifierKind === "group-winner" && logic.groups?.length === 1) {
      return `Group ${logic.groups[0]} winner`;
    }
    if (logic?.qualifierKind === "group-runner-up" && logic.groups?.length === 1) {
      return `Group ${logic.groups[0]} runner-up`;
    }
    if (logic?.qualifierKind === "third-place-candidate-set" && logic.groups?.length) {
      return `Third-place team from Group ${logic.groups.join("/")}`;
    }
    if (slot.round !== "R32") {
      const feeders = dependencyMap.get(slotId) || [];
      return "Projected winner choices";
    }
    return logic?.fifaLabel ? `${logic.fifaLabel} choices` : `${slotId} choices`;
  }

  function choiceWithState(team, source = "projected") {
    return {
      ...team,
      state: source,
    };
  }

  function getGroupedPickChoices(slotId) {
    const slot = slotsById.get(slotId);
    if (!slot) return [];
    const choices = getChoices(slotId);
    const choiceIds = new Set(choices.map((team) => team.id));
    const logic = r32LogicByGeometryId.get(slotId);

    if (slot.round === "R32" && logic?.groups?.length) {
      return logic.groups.map((groupId) => {
        const groupChoices = groupTeamsInCurrentOrder(groupId)
          .filter((team) => choiceIds.has(team.id))
          .map((team) => choiceWithState(team, "projected"));
        return {
          groupId,
          label: `Group ${groupId}`,
          panelAvailable: Boolean(getGroupStandings(groupId)),
          sourceRole: logic.qualifierKind || "group-source",
          choices: groupChoices,
        };
      }).filter((group) => group.choices.length > 0);
    }

    return [{
      groupId: null,
      label: "Winner choices",
      panelAvailable: false,
      sourceRole: "projected winners",
      choices: choices.map((team) => choiceWithState(team, "projected")),
    }];
  }

  function teamNameForKnockoutSourceSlot(sourceSlotId) {
    const id = String(sourceSlotId || "").trim();
    if (!id) return "";

    const directResult = officialKnockoutResultsByWinnerSlotId.get(id);
    if (directResult?.winnerTeamName) return directResult.winnerTeamName;

    const pick = selectedTeam(id);
    if (pick?.name) return pick.name;
    if (pick?.abbr) return pick.abbr;

    return id;
  }

  function fixtureLabelForKnockoutDisplay(metadata) {
    if (!metadata) return "";

    const sourceSlots = Array.isArray(metadata.siteSlotPair) ? metadata.siteSlotPair : [];
    if (sourceSlots.length === 2) {
      const home = teamNameForKnockoutSourceSlot(sourceSlots[0]);
      const away = teamNameForKnockoutSourceSlot(sourceSlots[1]);
      if (home && away && home !== sourceSlots[0] && away !== sourceSlots[1]) {
        return `${home} vs ${away}`;
      }
    }

    return metadata.fixtureLabel || "";
  }

  function knockoutMatchDisplayForSlot(slotId) {
    const metadata = knockoutDisplayMetadataByWinnerSlotId.get(slotId) || null;
    const result = officialKnockoutResultsByWinnerSlotId.get(slotId) || null;
    if (!metadata && !result) return null;

    return {
      ...(metadata || {}),
      siteWinnerSlotId: slotId,
      completed: Boolean(result),
      result: result || null,
      fixtureLabel: result?.resultLabel || fixtureLabelForKnockoutDisplay(metadata),
      resultLabel: result?.resultLabel || "",
      winnerTeamId: result?.winnerTeamId || "",
      winnerTeamName: result?.winnerTeamName || "",
      homeTeamId: result?.homeTeamId || "",
      homeTeamName: result?.homeTeamName || "",
      homeScore: result?.homeScore,
      awayTeamId: result?.awayTeamId || "",
      awayTeamName: result?.awayTeamName || "",
      awayScore: result?.awayScore,
      extendedHighlightsUrl: metadata?.extendedHighlightsUrl || result?.extendedHighlightsUrl || "",
    };
  }

  function getPickMenu(slotId) {
    const slot = getSlotDefinition(slotId);
    if (!slot) return null;
    const choices = getChoices(slotId);
    const currentPick = selectedTeam(slotId);
    const logic = r32LogicByGeometryId.get(slotId);
    const matchDisplay = knockoutMatchDisplayForSlot(slotId);

    return {
      slotId,
      title: sourceTitleForSlot(slotId),
      sourceLabel: logic?.fifaLabel || slotId,
      currentPick,
      canClear: Boolean(currentPick) && !matchDisplay,
      anchorBoundsPx: slot.boundsPx,
      groups: matchDisplay ? [] : getGroupedPickChoices(slotId),
      choices: matchDisplay ? [] : choices,
      pickable: choices.length > 0 || Boolean(matchDisplay),
      matchDisplay,
    };
  }


  function getGroupRail() {
    return GROUP_IDS.map((groupId) => {
      const teams = groupTeamsInCurrentOrder(groupId).slice(0, 4).map((team) => ({
        id: team.id,
        abbr: team.abbr || team.id,
        name: team.name || team.abbr || team.id,
        flag: team.flag || "",
      }));
      const teamNames = teams.map((team) => team.name || team.abbr || team.id).join(", ");
      return {
        groupId,
        label: `Group ${groupId}`,
        teams,
        accessibleLabel: `Open Group ${groupId} panel: ${teamNames}`,
      };
    });
  }

  function getFinalFourSlotViewModel(slotId) {
    const slot = finalFourSlotsById.get(slotId);
    if (!slot) return null;
    const team = selectedTeam(slotId);
    const choices = getChoices(slotId);
    return {
      slotId,
      round: slot.round,
      side: slot.side,
      boundsPx: slot.boundsPx,
      pickable: choices.length > 0,
      editableByAdminOfficial: adminOfficialEditorActive && choices.length > 0,
      choices,
      selectedTeam: team,
      pickValidity: pickValidityForSlot(slot, team),
      officialPickComparison: officialPickComparisonForSlot(slotId, team),
      officialTruthTeam: officialTeam(slotId),
      feederSlotIds: [...(slot.sourceSlotIds || [])],
      label: slot.displayLabel || slotId,
      finalFourRole: slotId,
    };
  }

  function getFinalFourViewModel() {
    if (!centerFinalFourSlot?.boundsPx) return null;
    const picks = ["FINAL-LEFT", "FINAL-RIGHT", "CHAMPION", "THIRD-PLACE-WINNER"]
      .map(getFinalFourSlotViewModel)
      .filter(Boolean);

    return {
      slotId: CENTER_FINAL_FOUR_SLOT_ID,
      title: "Final Four",
      boundsPx: centerFinalFourSlot.boundsPx,
      semifinalRows: [
        {
          label: "Left SF",
          teams: teamsFromSlotIds(["L-SF-01", "L-SF-02"]),
          winner: selectedTeam("FINAL-LEFT"),
          loser: loserFromSemifinal("FINAL-LEFT", ["L-SF-01", "L-SF-02"]),
          matchDisplay: knockoutMatchDisplayForSlot("FINAL-LEFT"),
        },
        {
          label: "Right SF",
          teams: teamsFromSlotIds(["R-SF-01", "R-SF-02"]),
          winner: selectedTeam("FINAL-RIGHT"),
          loser: loserFromSemifinal("FINAL-RIGHT", ["R-SF-01", "R-SF-02"]),
          matchDisplay: knockoutMatchDisplayForSlot("FINAL-RIGHT"),
        },
      ],
      picks,
    };
  }

  function getSlotViewModels() {
    return pickSurfaceSlots(slots).map((slot) => {
      const team = selectedTeam(slot.slotId);
      const choices = getChoices(slot.slotId);
      const logic = r32LogicByGeometryId.get(slot.slotId);
      const game2ResolvedTeam = slot.round === "R32" ? resolvedGame2R32Team(slot.slotId) : null;
      return {
        slotId: slot.slotId,
        round: slot.round,
        side: slot.side,
        boundsPx: slot.boundsPx,
        pickable: choices.length > 0,
        editableByAdminOfficial: adminOfficialEditorActive && choices.length > 0,
        r32EditableByAdminOfficial: slot.round === "R32" && adminOfficialR32EditorActive,
        r32ReadOnlyForPlayer: slot.round === "R32" && !adminOfficialR32EditorActive,
        choices,
        selectedTeam: team,
        game2ResolvedTeam,
        game2ResolvedSource: game2ResolvedTeam?.game2R32Source || null,
        pickValidity: pickValidityForSlot(slot, team),
        officialPickComparison: officialPickComparisonForSlot(slot.slotId, team),
        officialTruthTeam: officialTeam(slot.slotId),
        feederSlotIds: dependencyMap.get(slot.slotId) || [],
        label: logic?.fifaLabel || slot.slotId,
      };
    });
  }

  function importAccountBracketDocument(bracketDocument) {
    const picksBySlot = bracketDocument?.picksBySlot || {};
    const incomingPicks = {};

    for (const [slotId, record] of Object.entries(picksBySlot)) {
      if (record?.kind === "entrant" || record?.round === "R32_ENTRANT") continue;
      const teamId = record?.pick?.kind === "team" ? record.pick.teamId : record?.teamId;
      if (teamId) incomingPicks[slotId] = teamId;
    }

    return importPicksSnapshot({ picks: hydrateOnlySupabaseAdminR32IntoPlayerPicks(incomingPicks) });
  }

  function getAccountSaveBracketDocument({ userId: accountUserId = userId } = {}) {
    const bracketDocument = buildRemoteBracketDocument("account-save-button");
    return {
      ...bracketDocument,
      userId: accountUserId || bracketDocument.userId || userId,
      status: bracketDocument.status || "draft",
      visibility: bracketDocument.visibility || "private",
      bracketKind: bracketDocument.bracketKind || "player",
      updatedAt: new Date().toISOString(),
    };
  }

  function getSummary() {
    const picked = Object.keys(picks).length;
    const pickable = [
      ...getSlotViewModels(),
      ...(getFinalFourViewModel()?.picks || []),
    ].filter((slot) => slot.pickable).length;
    return {
      picked,
      pickable,
      totalSlots: allPickSlots().length,
      bracketKind: remoteBracketDocument?.bracketKind || "player",
      editingOfficialResults: isEditingOfficialResults(),
      officialResultsTruthSource: officialBracketDocument?.officialResultsTruthSource || officialBracketDocument?.officialR32AuthoritySource || "",
      officialResultsTruthUserId: officialBracketDocument?.userId || "",
      officialResultsTruthPickCount: Object.keys(officialPicks).length,
      playerVisibleR32Source: officialBracketDocument?.officialR32AuthoritySource || "",
      playerVisibleR32MatchesAdminOfficial: Boolean(officialBracketDocument),
      adminOfficialR32FailClosed: Boolean(officialBracketDocument?.r32TruthUnavailable || officialBracketDocument?.failClosed),
      adminOfficialR32EditorActive,
      adminOfficialEditorActive,
      adminOfficialFullBracketEditorActive: adminOfficialEditorActive,
    };
  }

  function clearAccountPicksForSignedOut() {
    const previousPickCount = Object.keys(picks).length;
    picks = hydrateOnlySupabaseAdminR32IntoPlayerPicks({});
    remoteBracketDocument = null;
    return { ok: true, cleared: previousPickCount };
  }

  // Card 205: preserve invalid picks; render pick validity instead of auto-clearing.
  // Join-required runtime: do not write local fallback picks on startup.

  return {
    nativeSize,
    getAccountSaveBracketDocument,
    importAccountBracketDocument,
    clearAccountPicksForSignedOut,
    getGroupRail,
    getFinalFourViewModel,
    getSlotViewModels,
    getGroupStandings,
    getGroupMatches,
    getMatchHighlights,
    getKnockoutMatches,
    getKnockoutMatch,
    getGroupContext,
    getPickMenu,
    getThirdPlaceTable,
    getChoices,
    setPick,
    clearPick,
    clearAll,
    exportPicksSnapshot,
    importPicksSnapshot,
    getSummary,
  };
}
