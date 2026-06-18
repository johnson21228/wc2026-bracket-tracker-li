const STORAGE_KEY = "wc2026.game1.cleanMvcPicks.v1";
const ROUND_ORDER = ["R32", "R16", "QF", "SF", "FINAL_FOUR"];
const BOARD_NATIVE_SIZE = Object.freeze({ width: 1536, height: 1024 });

const DATA_URLS = Object.freeze({
  geometry: "data/geometry/gameboard_manifest.json",
  r32Bridge: "data/geometry/game1_fifa_slot_geometry_map.json",
  r32Logic: "data/model/fifa_r32_logical_slot_order.json",
  teams: "data/model/teams.json",
  groups: "data/groups_from_flags_images.json",
  currentStandings: "data/current/group_standings.json",
  currentMatches: "data/current/group_matches.json",
  currentHighlights: "data/current/match_highlights.json",
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

  if (slotsById.has("CENTER-FINAL-FOUR")) {
    dependencies.set("CENTER-FINAL-FOUR", ["L-SF-01", "L-SF-02", "R-SF-01", "R-SF-02"].filter((slotId) => slotsById.has(slotId)));
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
  ] = await Promise.all([
    readJson(DATA_URLS.geometry),
    readJson(DATA_URLS.r32Bridge),
    readJson(DATA_URLS.r32Logic),
    readJson(DATA_URLS.teams),
    readJson(DATA_URLS.groups),
    readJson(DATA_URLS.currentStandings),
    readJson(DATA_URLS.currentMatches),
    readJson(DATA_URLS.currentHighlights),
  ]);

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
  const r32LogicByGeometryId = new Map();
  const r32LogicByFifaId = new Map((r32Logic.slots || []).map((slot) => [slot.fifaSlotId, slot]));
  for (const bridge of r32Bridge.slots || []) {
    const logic = r32LogicByFifaId.get(bridge.fifaSlotId);
    if (logic) {
      r32LogicByGeometryId.set(bridge.geometrySlotId, { ...logic, ...bridge });
    }
  }

  const dependencyMap = buildDependencyMap(slotsById, r32Bridge.slots || []);
  let picks = pickFromStorage();

  function getTeam(teamId) {
    return teamById.get(teamId) || null;
  }

  function selectedTeam(slotId) {
    return getTeam(picks[slotId]);
  }

  function getR32Choices(slotId) {
    const logic = r32LogicByGeometryId.get(slotId);
    if (!logic) return [];
    const groups = logic.groups || [];
    return uniqueTeams(groups.flatMap((groupId) => groupsById.get(groupId) || []));
  }

  function getKnockoutChoices(slotId) {
    const feeders = dependencyMap.get(slotId) || [];
    if (!feeders.length) return [];
    const feederTeams = feeders.map((feederId) => selectedTeam(feederId));
    if (feederTeams.some((team) => !team)) return [];
    return uniqueTeams(feederTeams);
  }

  function getChoices(slotId) {
    const slot = slotsById.get(slotId);
    if (!slot) return [];
    return slot.round === "R32" ? getR32Choices(slotId) : getKnockoutChoices(slotId);
  }

  function isPickable(slotId) {
    return getChoices(slotId).length > 0;
  }

  function validatePick(slotId, teamId) {
    if (!teamId) return { valid: true };
    const choices = getChoices(slotId);
    if (!choices.some((team) => team.id === teamId)) {
      return { valid: false, reason: "Team is not available from this slot's current feeder path." };
    }
    const slot = slotsById.get(slotId);
    if (slot?.round === "R32") {
      const duplicate = Object.entries(picks).find(([otherSlotId, otherTeamId]) => {
        return otherSlotId !== slotId && otherTeamId === teamId && slotsById.get(otherSlotId)?.round === "R32";
      });
      if (duplicate) {
        return { valid: false, reason: "That team is already assigned to another Round of 32 slot." };
      }
    }
    return { valid: true };
  }

  function cascadeClearInvalidDescendants() {
    const cleared = [];
    for (const round of ["R16", "QF", "SF", "FINAL_FOUR"]) {
      for (const slot of slots.filter((candidate) => candidate.round === round)) {
        const currentTeamId = picks[slot.slotId];
        if (!currentTeamId) continue;
        const choices = getChoices(slot.slotId);
        if (!choices.some((team) => team.id === currentTeamId)) {
          delete picks[slot.slotId];
          cleared.push(slot.slotId);
        }
      }
    }
    return cleared;
  }

  function setPick(slotId, teamId) {
    const validation = validatePick(slotId, teamId);
    if (!validation.valid) return { ok: false, ...validation, cleared: [] };
    if (teamId) picks[slotId] = teamId;
    else delete picks[slotId];
    const cleared = cascadeClearInvalidDescendants();
    saveToStorage(picks);
    return { ok: true, cleared };
  }

  function clearPick(slotId) {
    return setPick(slotId, null);
  }

  function clearAll() {
    picks = {};
    saveToStorage(picks);
    return { ok: true, cleared: slots.map((slot) => slot.slotId) };
  }

  function normalizeGroupId(groupId) {
    return String(groupId || "").trim().toUpperCase().replace(/^GROUP\s+/, "");
  }

  function getGroupStandings(groupId) {
    return currentStandingsById.get(normalizeGroupId(groupId)) || null;
  }

  function getGroupMatches(groupId) {
    return [...(currentMatchesByGroupId.get(normalizeGroupId(groupId)) || [])];
  }

  function getMatchHighlights(matchId) {
    return currentHighlightsByMatchId.get(String(matchId)) || null;
  }

  function getThirdPlaceTable() {
    return [...(currentStandingsPayload.thirdPlaceTable || [])];
  }

  function getGroupContext(groupId) {
    const normalizedGroupId = normalizeGroupId(groupId);
    const standings = getGroupStandings(normalizedGroupId);
    return {
      groupId: normalizedGroupId,
      standings,
      matches: getGroupMatches(normalizedGroupId),
      source: currentStandingsPayload.source || null,
    };
  }


  function sourceTitleForSlot(slotId) {
    const slot = slotsById.get(slotId);
    const logic = r32LogicByGeometryId.get(slotId);
    if (!slot) return slotId;

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
      return feeders.length ? `Winner from ${feeders.join(" / ")}` : "Feeder path winner";
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
        const groupChoices = (groupsById.get(groupId) || [])
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
      label: "Feeder choices",
      panelAvailable: false,
      sourceRole: "knockout-feeder",
      choices: choices.map((team) => choiceWithState(team, "projected")),
    }];
  }

  function getPickMenu(slotId) {
    const slot = slotsById.get(slotId);
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

  function getSlotViewModels() {
    return slots.map((slot) => {
      const team = selectedTeam(slot.slotId);
      const choices = getChoices(slot.slotId);
      const logic = r32LogicByGeometryId.get(slot.slotId);
      return {
        slotId: slot.slotId,
        round: slot.round,
        side: slot.side,
        boundsPx: slot.boundsPx,
        pickable: choices.length > 0,
        choices,
        selectedTeam: team,
        feederSlotIds: dependencyMap.get(slot.slotId) || [],
        label: logic?.fifaLabel || slot.slotId,
      };
    });
  }

  function getSummary() {
    const picked = Object.keys(picks).length;
    const pickable = getSlotViewModels().filter((slot) => slot.pickable).length;
    return { picked, pickable, totalSlots: slots.length };
  }

  cascadeClearInvalidDescendants();
  saveToStorage(picks);

  return {
    nativeSize,
    getSlotViewModels,
    getGroupStandings,
    getGroupMatches,
    getMatchHighlights,
    getGroupContext,
    getPickMenu,
    getThirdPlaceTable,
    getChoices,
    setPick,
    clearPick,
    clearAll,
    getSummary,
  };
}
