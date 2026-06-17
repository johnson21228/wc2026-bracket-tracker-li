import { unpickedPickValue, validatePickValue } from "./PickValue.js";

const GAME1_LIFECYCLE_STATES = Object.freeze({
  GROUP_STAGE_OPEN: "GROUP_STAGE_OPEN",
  R32_PROJECTION_LIVE: "R32_PROJECTION_LIVE",
  FIFA_R32_LOCKED: "FIFA_R32_LOCKED",
  KNOCKOUT_PICKING_OPEN: "KNOCKOUT_PICKING_OPEN",
  KNOCKOUT_LIVE: "KNOCKOUT_LIVE",
  COMPLETE: "COMPLETE",
});

function assertGame1LifecycleState(state) {
  if (!Object.values(GAME1_LIFECYCLE_STATES).includes(state)) {
    throw new Error(`Invalid Game 1 lifecycle state: ${state}`);
  }
  return state;
}

function r32SitePickIdsFromMap(fifaR32SlotMap) {
  return (fifaR32SlotMap?.mappings || [])
    .map((mapping) => mapping.sitePickId)
    .filter(Boolean);
}

function sitePickIdsFromSlots(bracketSlots) {
  return (bracketSlots?.slots || bracketSlots || [])
    .map((slot) => slot.sitePickId)
    .filter(Boolean);
}

function createUnpickedLayer(sitePickIds) {
  return Object.fromEntries(sitePickIds.map((sitePickId) => [sitePickId, unpickedPickValue()]));
}

function createGame1LifecycleRecord({
  userId,
  bracketId = `${userId}-wc2026-game1`,
  tournamentId = "wc2026",
  bracketSlots,
  fifaR32SlotMap,
}) {
  const allSitePickIds = sitePickIdsFromSlots(bracketSlots);
  const r32SitePickIds = r32SitePickIdsFromMap(fifaR32SlotMap);
  const knockoutSitePickIds = allSitePickIds.filter((sitePickId) => !r32SitePickIds.includes(sitePickId));

  return {
    schemaVersion: 1,
    id: bracketId,
    userId,
    tournamentId,
    gameId: "game1",
    lifecycleState: GAME1_LIFECYCLE_STATES.GROUP_STAGE_OPEN,
    lockedAt: null,
    layers: {
      playerProjection: createUnpickedLayer(r32SitePickIds),
      curatedProjection: createUnpickedLayer(r32SitePickIds),
      officialLockedR32: createUnpickedLayer(r32SitePickIds),
      knockoutWinnerPicks: createUnpickedLayer(knockoutSitePickIds),
    },
    history: [
      {
        kind: "game1-lifecycle-record-created",
        at: null,
      },
    ],
  };
}

function normalizeGame1LifecycleRecord({ record, bracketSlots, fifaR32SlotMap, teamsById }) {
  const fallback = createGame1LifecycleRecord({
    userId: record?.userId || "steve",
    bracketId: record?.id,
    tournamentId: record?.tournamentId || "wc2026",
    bracketSlots,
    fifaR32SlotMap,
  });

  const allSitePickIds = sitePickIdsFromSlots(bracketSlots);
  const r32SitePickIds = r32SitePickIdsFromMap(fifaR32SlotMap);
  const knockoutSitePickIds = allSitePickIds.filter((sitePickId) => !r32SitePickIds.includes(sitePickId));

  const normalizeLayer = (layer, sitePickIds) => Object.fromEntries(
    sitePickIds.map((sitePickId) => [
      sitePickId,
      validatePickValue(layer?.[sitePickId] || unpickedPickValue(), teamsById),
    ])
  );

  return {
    ...fallback,
    ...record,
    lifecycleState: assertGame1LifecycleState(record?.lifecycleState || fallback.lifecycleState),
    layers: {
      playerProjection: normalizeLayer(record?.layers?.playerProjection, r32SitePickIds),
      curatedProjection: normalizeLayer(record?.layers?.curatedProjection, r32SitePickIds),
      officialLockedR32: normalizeLayer(record?.layers?.officialLockedR32, r32SitePickIds),
      knockoutWinnerPicks: normalizeLayer(record?.layers?.knockoutWinnerPicks, knockoutSitePickIds),
    },
    history: Array.isArray(record?.history) ? record.history : fallback.history,
  };
}

function transitionGame1Lifecycle(record, nextState, event = {}) {
  return {
    ...record,
    lifecycleState: assertGame1LifecycleState(nextState),
    history: [
      ...(record.history || []),
      {
        kind: "game1-lifecycle-transition",
        from: record.lifecycleState,
        to: nextState,
        at: event.at || new Date().toISOString(),
        note: event.note || "",
      },
    ],
  };
}

export {
  GAME1_LIFECYCLE_STATES,
  assertGame1LifecycleState,
  createGame1LifecycleRecord,
  normalizeGame1LifecycleRecord,
  r32SitePickIdsFromMap,
  sitePickIdsFromSlots,
  transitionGame1Lifecycle,
};
