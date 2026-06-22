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

export async function createBracketModel() {
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
  let picks = pickFromStorage();

  function getTeam(teamId) {
    return teamById.get(teamId) || null;
  }

  function selectedTeam(slotId) {
    return getTeam(picks[slotId]);
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
    return Object.entries(picks).find(([otherSlotId, otherTeamId]) => {
      return otherSlotId !== slotId && otherTeamId === teamId && slotsById.get(otherSlotId)?.round === "R32";
    }) || null;
  }

  function pickValidityForSlot(slot, team) {
    if (!team) return { state: "empty", reason: "No pick has been made." };

    const choices = getChoices(slot.slotId);
    if (choices.length && !choices.some((choice) => choice.id === team.id)) {
      return {
        state: "invalid",
        reason: `${team.abbr || team.id} is not available from this slot's current source or feeder path.`,
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
    const slot = getSlotDefinition(slotId);
    if (!slot) {
      return { ok: false, reason: "Unknown bracket slot.", cleared: [] };
    }
    if (teamId && !teamById.has(teamId)) {
      return { ok: false, reason: "Unknown team.", cleared: [] };
    }
    if (teamId) picks[slotId] = teamId;
    else delete picks[slotId];
    saveToStorage(picks);
    const team = selectedTeam(slotId);
    return { ok: true, cleared: [], pickValidity: pickValidityForSlot(slot, team) };
  }

  function clearPick(slotId) {
    return setPick(slotId, null);
  }

  function clearAll() {
    picks = {};
    saveToStorage(picks);
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
    saveToStorage(picks);
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

  function getPickMenu(slotId) {
    const slot = getSlotDefinition(slotId);
    if (!slot) return null;
    const choices = getChoices(slotId);
    const currentPick = selectedTeam(slotId);
    const logic = r32LogicByGeometryId.get(slotId);
    return {
      slotId,
      title: sourceTitleForSlot(slotId),
      sourceLabel: logic?.fifaLabel || slotId,
      currentPick,
      canClear: Boolean(currentPick),
      anchorBoundsPx: slot.boundsPx,
      groups: getGroupedPickChoices(slotId),
      choices,
      pickable: choices.length > 0,
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
      choices,
      selectedTeam: team,
      pickValidity: pickValidityForSlot(slot, team),
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
        },
        {
          label: "Right SF",
          teams: teamsFromSlotIds(["R-SF-01", "R-SF-02"]),
          winner: selectedTeam("FINAL-RIGHT"),
          loser: loserFromSemifinal("FINAL-RIGHT", ["R-SF-01", "R-SF-02"]),
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
        choices,
        selectedTeam: team,
        game2ResolvedTeam,
        game2ResolvedSource: game2ResolvedTeam?.game2R32Source || null,
        pickValidity: pickValidityForSlot(slot, team),
        feederSlotIds: dependencyMap.get(slot.slotId) || [],
        label: logic?.fifaLabel || slot.slotId,
      };
    });
  }

  function getSummary() {
    const picked = Object.keys(picks).length;
    const pickable = [
      ...getSlotViewModels(),
      ...(getFinalFourViewModel()?.picks || []),
    ].filter((slot) => slot.pickable).length;
    return { picked, pickable, totalSlots: allPickSlots().length };
  }

  // Card 205: preserve invalid picks; render pick validity instead of auto-clearing.
  saveToStorage(picks);

  return {
    nativeSize,
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
