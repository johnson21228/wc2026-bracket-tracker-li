import { teamPickValue, unpickedPickValue } from "../model/PickValue.js";
import { setBracketPick } from "../model/UserBracketModel.js";
import { createStaticBracketRepository } from "../services/BracketRepository.js";
import { areGroupStagePicksLocked, groupStagePicksLockedMessage } from "../config/gameLocks.js";
const GAME1_R32_PICK_STORAGE_KEY = "wc2026.game1.r32ProjectionPicks.v1";

const GAME1_R32_PICKABLE_STATES = new Set([
  "GROUP_STAGE_OPEN",
  "R32_PROJECTION_LIVE",
]);

const DEFAULT_TEAM_SOURCES = Object.freeze([
  "data/model/teams.json",
  "data/teams_from_flags_images.json",
  "data/groups_from_flags_images.json",
  "data/teams.json",
]);

function normalizeGroup(value) {
  if (value === null || value === undefined) return null;
  return String(value).trim().toUpperCase();
}

function normalizeTeam(team, fallbackGroup = null) {
  const group = normalizeGroup(team.group || team.groupId || team.groupLetter || fallbackGroup);
  const abbr = String(team.abbr || team.teamId || team.id || team.code || "").trim().toUpperCase();
  const name = team.name || team.displayNameFromImage || team.displayName || abbr;
  if (!group || !abbr) return null;
  return {
    id: String(team.id || team.teamId || abbr).trim().toUpperCase(),
    abbr,
    name,
    group,
    flagEmoji: team.flagEmoji || "",
    source: team.source || "teams",
  };
}

function teamsFromPayload(payload) {
  if (!payload) return [];

  if (Array.isArray(payload)) {
    return payload.map((team) => normalizeTeam(team)).filter(Boolean);
  }

  if (Array.isArray(payload.teams)) {
    return payload.teams.map((team) => normalizeTeam(team)).filter(Boolean);
  }

  if (payload.groups && typeof payload.groups === "object") {
    const teams = [];
    for (const [group, groupTeams] of Object.entries(payload.groups)) {
      if (!Array.isArray(groupTeams)) continue;
      for (const team of groupTeams) {
        const normalized = normalizeTeam(team, group);
        if (normalized) teams.push(normalized);
      }
    }
    return teams;
  }

  return [];
}

async function fetchJson(path, { optional = false } = {}) {
  try {
    const response = await fetch(path, { cache: "no-cache" });
    if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
    return response.json();
  } catch (error) {
    if (optional) return null;
    throw error;
  }
}

function byKey(items, key) {
  return Object.fromEntries((items || []).map((item) => [item[key], item]));
}

function getBounds(slot) {
  const bounds = slot?.boundsPx || slot?.bounds || slot?.box || slot?.hitRegionPx || null;
  if (!bounds) return null;
  const x = Number(bounds.x ?? 0);
  const y = Number(bounds.y ?? 0);
  const width = Number(bounds.width ?? bounds.w ?? 0);
  const height = Number(bounds.height ?? bounds.h ?? 0);
  if (!Number.isFinite(x) || !Number.isFinite(y) || !Number.isFinite(width) || !Number.isFinite(height)) return null;
  return { x, y, width, height };
}

function normalizePicks(raw) {
  if (!raw || typeof raw !== "object") return {};
  const picks = {};
  for (const [fifaSlotId, pick] of Object.entries(raw)) {
    if (!pick || typeof pick !== "object") continue;
    picks[fifaSlotId] = pick;
  }
  return picks;
}

function readLocalPicks(storageKey = GAME1_R32_PICK_STORAGE_KEY) {
  try {
    const raw = window.localStorage.getItem(storageKey);
    return normalizePicks(raw ? JSON.parse(raw) : {});
  } catch {
    return {};
  }
}

function writeLocalPicks(picks, storageKey = GAME1_R32_PICK_STORAGE_KEY) {
  window.localStorage.setItem(storageKey, JSON.stringify(normalizePicks(picks), null, 2));
}

function lifecycleStateFrom(lifecycle) {
  return lifecycle?.currentState || lifecycle?.state || lifecycle?.lifecycleState || null;
}

function isPickableLifecycle(lifecycle) {
  const state = lifecycleStateFrom(lifecycle);
  if (!state) return true;
  return GAME1_R32_PICKABLE_STATES.has(state);
}

function isGroupStagePickOpen(lifecycle) {
  return isPickableLifecycle(lifecycle) && !areGroupStagePicksLocked();
}

function titleForSlot(logicSlot) {
  if (logicSlot.qualifierKind === "group-winner") return `Pick projected Group ${logicSlot.groups[0]} winner`;
  if (logicSlot.qualifierKind === "group-runner-up") return `Pick projected Group ${logicSlot.groups[0]} runner-up`;
  return `Pick projected third-place qualifier from ${logicSlot.groups.join("/")}`;
}

function teamSort(a, b) {
  if (a.group !== b.group) return String(a.group).localeCompare(String(b.group));
  return String(a.abbr).localeCompare(String(b.abbr));
}

function pickRecordFromTeam({ fifaSlot, team }) {
  return {
    kind: "projected-r32-slot-team",
    teamId: team.id,
    abbr: team.abbr,
    name: team.name,
    group: team.group,
    flagEmoji: team.flagEmoji,
    fifaSlotId: fifaSlot.fifaSlotId,
    fifaLabel: fifaSlot.fifaLabel,
    qualifierKind: fifaSlot.qualifierKind,
    eligibleGroups: fifaSlot.groups || [],
    pickedAt: new Date().toISOString(),
  };
}

class Game1R32PickController {
  constructor({
    logic,
    bridge,
    geometry,
    lifecycle,
    teams,
    storageKey = GAME1_R32_PICK_STORAGE_KEY,
    bracketRepository = createStaticBracketRepository(),
    userId = "anonymous",
    userBracket = null,
  }) {
    this.logic = logic;
    this.bridge = bridge;
    this.geometry = geometry;
    this.lifecycle = lifecycle;
    this.teams = teams;
    this.storageKey = storageKey;
    this.bracketRepository = bracketRepository;
    this.userId = userId;
    this.userBracket = userBracket;
    this.lastSavePromise = null;

    this.logicByFifaSlotId = byKey(logic.slots || [], "fifaSlotId");
    this.geometryBySlotId = byKey(geometry.slots || [], "slotId");
  }

  get lifecycleState() {
    return lifecycleStateFrom(this.lifecycle);
  }

  get isPickable() {
    return isGroupStagePickOpen(this.lifecycle);
  }

  readPicks() {
    return readLocalPicks(this.storageKey);
  }

  writePicks(picks) {
    writeLocalPicks(picks, this.storageKey);
  }

  candidateTeamsForSlot(logicSlot) {
    const eligibleGroups = new Set((logicSlot.groups || []).map(normalizeGroup));
    return this.teams
      .filter((team) => eligibleGroups.has(team.group))
      .sort(teamSort);
  }

  getSlotViewModels() {
    const picks = this.readPicks();
    return (this.bridge.slots || []).map((bridgeSlot) => {
      const logicSlot = this.logicByFifaSlotId[bridgeSlot.fifaSlotId] || null;
      const geometrySlot = this.geometryBySlotId[bridgeSlot.geometrySlotId] || null;
      const bounds = getBounds(geometrySlot);
      const candidates = logicSlot ? this.candidateTeamsForSlot(logicSlot) : [];
      const disabledReason = this.disabledReasonFor({ logicSlot, geometrySlot, bounds, candidates });
      const pick = logicSlot ? picks[logicSlot.fifaSlotId] || null : null;
      return {
        bridgeSlot,
        logicSlot,
        geometrySlot,
        bounds,
        candidates,
        disabledReason,
        enabled: !disabledReason,
        pick,
        title: logicSlot ? titleForSlot(logicSlot) : "Unavailable R32 slot",
      };
    });
  }

  disabledReasonFor({ logicSlot, geometrySlot, bounds, candidates }) {
    if (areGroupStagePicksLocked()) return groupStagePicksLockedMessage();
    if (!isPickableLifecycle(this.lifecycle)) return "Game 1 projection picking is not open.";
    if (!logicSlot) return "FIFA slot logic is missing.";
    if (!geometrySlot || !bounds) return "Board geometry is missing.";
    if (!Array.isArray(candidates) || candidates.length === 0) return "No candidate teams are available for this slot.";
    return "";
  }

  findSlot(fifaSlotId) {
    return this.getSlotViewModels().find((slot) => slot.logicSlot?.fifaSlotId === fifaSlotId) || null;
  }

  validatePick({ fifaSlotId, teamId }) {
    if (areGroupStagePicksLocked()) return { ok: false, reason: groupStagePicksLockedMessage() };
    const slot = this.findSlot(fifaSlotId);
    if (!slot) return { ok: false, reason: "R32 slot is not available." };
    if (!slot.enabled) return { ok: false, reason: slot.disabledReason };

    const normalizedTeamId = String(teamId || "").trim().toUpperCase();
    const team = slot.candidates.find((candidate) => candidate.id === normalizedTeamId || candidate.abbr === normalizedTeamId);
    if (!team) return { ok: false, reason: "Team is not a valid candidate for this FIFA R32 slot." };

    const picks = this.readPicks();
    const duplicateEntry = Object.entries(picks).find(([otherSlotId, pick]) => {
      if (otherSlotId === fifaSlotId) return false;
      return pick?.teamId === team.id || pick?.abbr === team.abbr;
    });
    if (duplicateEntry) {
      const [otherSlotId, pick] = duplicateEntry;
      return {
        ok: false,
        reason: `${pick.abbr || team.abbr} is already picked in ${pick.fifaLabel || otherSlotId}.`,
      };
    }

    return { ok: true, slot, team };
  }

  canonicalSitePickIdForFifaSlot(fifaSlotId) {
    const bridgeSlot = (this.bridge.slots || []).find((slot) => slot.fifaSlotId === fifaSlotId);
    return bridgeSlot?.geometrySlotId || fifaSlotId;
  }

  saveBracketDocumentFromProjectionPicks(picks) {
    if (!this.bracketRepository || !this.userBracket) return null;

    let nextBracket = this.userBracket;
    for (const bridgeSlot of this.bridge.slots || []) {
      const sitePickId = bridgeSlot.geometrySlotId || bridgeSlot.fifaSlotId;
      const pick = picks[bridgeSlot.fifaSlotId] || null;
      const teamId = pick?.teamId || pick?.abbr || null;
      nextBracket = setBracketPick({
        bracket: nextBracket,
        sitePickId,
        pickValue: teamId ? teamPickValue(teamId) : unpickedPickValue(),
      });
    }

    this.userBracket = nextBracket;
    this.lastSavePromise = this.bracketRepository
      .saveUserBracket(nextBracket)
      .then((savedBracket) => {
        this.userBracket = savedBracket || nextBracket;
        return this.userBracket;
      })
      .catch((error) => {
        window.dispatchEvent(new CustomEvent("wc2026:bracketDocumentSaveFailed", {
          detail: { error: String(error?.message || error) },
        }));
        return nextBracket;
      });

    return this.lastSavePromise;
  }

  setPick({ fifaSlotId, teamId }) {
    window.BracketeeringPickLockdownPolicy?.assertPickChangeAllowed?.({ slotId: fifaSlotId, teamId });
    const validation = this.validatePick({ fifaSlotId, teamId });
    if (!validation.ok) return validation;

    const picks = this.readPicks();
    const record = pickRecordFromTeam({ fifaSlot: validation.slot.logicSlot, team: validation.team });
    picks[fifaSlotId] = record;
    this.writePicks(picks);
    this.saveBracketDocumentFromProjectionPicks(picks);

    window.dispatchEvent(new CustomEvent("wc2026:game1R32ProjectionPickChanged", {
      detail: {
        action: "set",
        fifaSlotId,
        fifaLabel: validation.slot.logicSlot.fifaLabel,
        pick: record,
      },
    }));

    return { ok: true, slot: validation.slot, pick: record };
  }

  clearPick({ fifaSlotId }) {
    window.BracketeeringPickLockdownPolicy?.assertPickChangeAllowed?.({ slotId: fifaSlotId });
    if (areGroupStagePicksLocked()) return { ok: false, reason: groupStagePicksLockedMessage() };
    const picks = this.readPicks();
    const previous = picks[fifaSlotId] || null;
    delete picks[fifaSlotId];
    this.writePicks(picks);
    this.saveBracketDocumentFromProjectionPicks(picks);

    window.dispatchEvent(new CustomEvent("wc2026:game1R32ProjectionPickChanged", {
      detail: {
        action: "clear",
        fifaSlotId,
        fifaLabel: previous?.fifaLabel || null,
        pick: null,
      },
    }));

    return { ok: true, previous };
  }
}

async function loadTeams({ sources = DEFAULT_TEAM_SOURCES } = {}) {
  for (const path of sources) {
    const payload = await fetchJson(path, { optional: true });
    const teams = teamsFromPayload(payload);
    if (teams.length > 0) return teams;
  }
  return [];
}

async function createGame1R32PickController({
  logicSource = "data/model/fifa_r32_logical_slot_order.json",
  bridgeSource = "data/geometry/game1_fifa_slot_geometry_map.json",
  geometryManifest = "data/geometry/gameboard_manifest.json",
  lifecycleSource = "data/model/game1_lifecycle.json",
  teamSources = DEFAULT_TEAM_SOURCES,
  storageKey = GAME1_R32_PICK_STORAGE_KEY,
  bracketRepository = createStaticBracketRepository(),
  userId = "anonymous",
} = {}) {
  const [logic, bridge, geometry, lifecycle, teams, userBracket] = await Promise.all([
    fetchJson(logicSource),
    fetchJson(bridgeSource),
    fetchJson(geometryManifest),
    fetchJson(lifecycleSource, { optional: true }),
    loadTeams({ sources: teamSources }),
    bracketRepository.loadUserBracket(userId),
  ]);

  return new Game1R32PickController({
    logic,
    bridge,
    geometry,
    lifecycle,
    teams,
    storageKey,
    bracketRepository,
    userId,
    userBracket,
  });
}

export {
  DEFAULT_TEAM_SOURCES,
  GAME1_R32_PICK_STORAGE_KEY,
  GAME1_R32_PICKABLE_STATES,
  Game1R32PickController,
  createGame1R32PickController,
  getBounds,
  titleForSlot,
};
