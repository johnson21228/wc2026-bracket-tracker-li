import { normalizePickValue, unpickedPickValue, validatePickValue } from "./PickValue.js";

function sitePickIdsFromSlots(bracketSlots) {
  const slots = Array.isArray(bracketSlots) ? bracketSlots : bracketSlots?.slots || [];
  return slots.map((slot) => slot.sitePickId).filter(Boolean);
}

function createEmptyUserBracket({ userId, bracketId, tournamentId = "wc2026", bracketSlots }) {
  const picks = Object.fromEntries(
    sitePickIdsFromSlots(bracketSlots).map((sitePickId) => [sitePickId, unpickedPickValue()])
  );

  return {
    id: bracketId,
    userId,
    tournamentId,
    updatedAt: null,
    picks,
  };
}

function normalizeUserBracket({ bracket, bracketSlots, teamsById }) {
  const sitePickIds = sitePickIdsFromSlots(bracketSlots);
  const normalizedPicks = {};

  for (const sitePickId of sitePickIds) {
    normalizedPicks[sitePickId] = validatePickValue(
      bracket?.picks?.[sitePickId] || unpickedPickValue(),
      teamsById
    );
  }

  return {
    id: String(bracket?.id || `${bracket?.userId || "user"}-wc2026`),
    userId: String(bracket?.userId || ""),
    tournamentId: String(bracket?.tournamentId || "wc2026"),
    updatedAt: bracket?.updatedAt || null,
    picks: normalizedPicks,
  };
}

function setBracketPick({ bracket, sitePickId, pickValue }) {
  return {
    ...bracket,
    updatedAt: new Date().toISOString(),
    picks: {
      ...bracket.picks,
      [sitePickId]: normalizePickValue(pickValue),
    },
  };
}

export {
  createEmptyUserBracket,
  normalizeUserBracket,
  setBracketPick,
  sitePickIdsFromSlots,
};
