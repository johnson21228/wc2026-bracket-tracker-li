import { normalizePickValue, unpickedPickValue, validatePickValue } from "./PickValue.js";

const CURRENT_BRACKET_DOCUMENT_SCHEMA_VERSION = 2;
const DEFAULT_BRACKET_LIFECYCLE_STATE = "GROUP_STAGE_OPEN";

function normalizePhaseLocks(phaseLocks = {}) {
  return {
    r32LockedAt: phaseLocks?.r32LockedAt || null,
  };
}

function r32LockedAtForBracket(bracket) {
  return normalizePhaseLocks(bracket?.phaseLocks).r32LockedAt;
}

function isR32BracketSlot(slotOrRecord) {
  const round = String(slotOrRecord?.round || "").toUpperCase();
  return round === "R32" || round === "R32_ENTRANT";
}

function pickValuesEquivalent(left, right) {
  return JSON.stringify(normalizePickValue(left)) === JSON.stringify(normalizePickValue(right));
}

function canEditBracketSlot(slotOrRecord, bracket) {
  const status = String(bracket?.status || "draft").toLowerCase();
  if (status === "locked") return false;
  if (isR32BracketSlot(slotOrRecord)) return !r32LockedAtForBracket(bracket);
  return true;
}

function canMutateBracketPick({ bracket, sitePickId, pickValue }) {
  const record = bracket?.picksBySlot?.[sitePickId] || null;
  const slot = record || { slotId: sitePickId, round: roundForLegacySlot(sitePickId, null) };
  if (canEditBracketSlot(slot, bracket)) return true;
  const currentPick = pickValueFromSlotRecord(record);
  return pickValuesEquivalent(currentPick, pickValue);
}


function slotsFromModel(bracketSlots) {
  if (Array.isArray(bracketSlots)) return bracketSlots;
  return bracketSlots?.slots || [];
}

function canonicalPickSlotsFromModel(bracketSlots, gameId = "game1") {
  const canonicalSlots = Array.isArray(bracketSlots?.canonicalPickSlots)
    ? bracketSlots.canonicalPickSlots
    : null;

  const slots = canonicalSlots || slotsFromModel(bracketSlots).filter((slot) => slot?.kind !== "FINAL_FOUR");
  return slots
    .map((slot) => {
      const slotId = slot.slotId || slot.sitePickId;
      if (!slotId) return null;
      const round = slot.round || roundForLegacySlot(slotId, slot.kind);
      return {
        slotId,
        sitePickId: slot.sitePickId || slotId,
        kind: slot.kind === "entrant" || round === "R32_ENTRANT" ? "entrant" : "winner",
        round,
        gameId,
      };
    })
    .filter(Boolean);
}

function sitePickIdsFromSlots(bracketSlots) {
  return canonicalPickSlotsFromModel(bracketSlots).map((slot) => slot.slotId);
}

function roundForLegacySlot(slotId, kind) {
  if (kind === "R32") return "R32_ENTRANT";
  if (kind === "R16") return "R32_WINNER";
  if (kind === "QF") return "R16_WINNER";
  if (kind === "SF") return "QF_WINNER";
  if (slotId === "FINAL-LEFT" || slotId === "FINAL-RIGHT") return "SF_WINNER";
  if (slotId === "CHAMPION") return "CHAMPION";
  if (slotId === "THIRD-PLACE-WINNER") return "THIRD_PLACE";
  return String(kind || "UNKNOWN");
}

function pickValueFromSlotRecord(record) {
  if (!record || record.pick === null || record.pick === undefined) return unpickedPickValue();
  return normalizePickValue(record.pick);
}

function slotRecordFromPickValue(slot, pickValue, source = null) {
  const normalized = normalizePickValue(pickValue);
  const picked = normalized.kind === "unpicked" ? null : normalized;
  return {
    slotId: slot.slotId,
    kind: slot.kind,
    round: slot.round,
    pick: picked,
    source: source || (picked ? "user" : "empty"),
  };
}

function legacyPicksFromPicksBySlot(picksBySlot) {
  const entries = Object.entries(picksBySlot || {}).map(([slotId, record]) => [
    slotId,
    pickValueFromSlotRecord(record),
  ]);
  return Object.fromEntries(entries);
}

function createEmptyBracketDocument({
  userId = "",
  bracketId = null,
  tournamentId = "wc2026",
  gameId = "game1",
  bracketSlots,
} = {}) {
  const canonicalSlots = canonicalPickSlotsFromModel(bracketSlots, gameId);
  const picksBySlot = Object.fromEntries(
    canonicalSlots.map((slot) => [slot.slotId, slotRecordFromPickValue(slot, unpickedPickValue(), "empty")])
  );

  return {
    schemaVersion: CURRENT_BRACKET_DOCUMENT_SCHEMA_VERSION,
    id: bracketId || `${userId || "user"}-${tournamentId}`,
    userId,
    tournamentId,
    gameId,
    status: "draft",
    lifecycleState: DEFAULT_BRACKET_LIFECYCLE_STATE,
    phaseLocks: normalizePhaseLocks(),
    expectedPickCount: canonicalSlots.length,
    createdAt: null,
    updatedAt: null,
    picksBySlot,
    // Transitional compatibility for existing render code. Durable authority is picksBySlot.
    picks: legacyPicksFromPicksBySlot(picksBySlot),
  };
}

function createEmptyUserBracket(args) {
  return createEmptyBracketDocument(args);
}

function normalizeBracketDocument({ bracket, bracketSlots, teamsById, userId = "", gameId = "game1" }) {
  const canonicalSlots = canonicalPickSlotsFromModel(bracketSlots, bracket?.gameId || gameId);
  const incomingBySlot = bracket?.picksBySlot && typeof bracket.picksBySlot === "object" ? bracket.picksBySlot : {};
  const incomingLegacyPicks = bracket?.picks && typeof bracket.picks === "object" ? bracket.picks : {};
  const picksBySlot = {};

  for (const slot of canonicalSlots) {
    const incomingRecord = incomingBySlot[slot.slotId];
    const incomingPick = incomingRecord && "pick" in incomingRecord
      ? incomingRecord.pick
      : incomingLegacyPicks[slot.slotId] || unpickedPickValue();

    const pickValue = validatePickValue(
      incomingPick === null || incomingPick === undefined ? unpickedPickValue() : incomingPick,
      teamsById
    );

    picksBySlot[slot.slotId] = slotRecordFromPickValue(
      slot,
      pickValue,
      incomingRecord?.source || (pickValue.kind === "unpicked" ? "empty" : "user")
    );
  }

  const documentUserId = String(bracket?.userId || userId || "");
  const documentTournamentId = String(bracket?.tournamentId || "wc2026");

  return {
    schemaVersion: Math.max(Number(bracket?.schemaVersion || 1), CURRENT_BRACKET_DOCUMENT_SCHEMA_VERSION),
    id: String(bracket?.id || `${documentUserId || "user"}-${documentTournamentId}`),
    userId: documentUserId,
    tournamentId: documentTournamentId,
    gameId: String(bracket?.gameId || gameId),
    status: String(bracket?.status || "draft"),
    lifecycleState: String(bracket?.lifecycleState || DEFAULT_BRACKET_LIFECYCLE_STATE),
    phaseLocks: normalizePhaseLocks(bracket?.phaseLocks),
    expectedPickCount: canonicalSlots.length,
    createdAt: bracket?.createdAt || null,
    updatedAt: bracket?.updatedAt || null,
    picksBySlot,
    // Transitional compatibility for existing render code. Durable authority is picksBySlot.
    picks: legacyPicksFromPicksBySlot(picksBySlot),
  };
}

function normalizeUserBracket(args) {
  return normalizeBracketDocument(args);
}

function setBracketPick({ bracket, sitePickId, pickValue }) {
  const normalizedPick = normalizePickValue(pickValue);
  if (!canMutateBracketPick({ bracket, sitePickId, pickValue: normalizedPick })) {
    throw new Error("R32 picks are locked and cannot be changed after R32 lock-in.");
  }
  const existingRecord = bracket?.picksBySlot?.[sitePickId] || {
    slotId: sitePickId,
    kind: sitePickId === "CHAMPION" || sitePickId === "THIRD-PLACE-WINNER" ? "winner" : "winner",
    round: roundForLegacySlot(sitePickId, null),
  };
  const slot = {
    slotId: sitePickId,
    kind: existingRecord.kind || "winner",
    round: existingRecord.round || roundForLegacySlot(sitePickId, null),
  };
  const record = slotRecordFromPickValue(slot, normalizedPick, normalizedPick.kind === "unpicked" ? "empty" : "user");
  const picksBySlot = {
    ...(bracket.picksBySlot || {}),
    [sitePickId]: record,
  };

  return {
    ...bracket,
    schemaVersion: Math.max(Number(bracket?.schemaVersion || 1), CURRENT_BRACKET_DOCUMENT_SCHEMA_VERSION),
    lifecycleState: bracket?.lifecycleState || DEFAULT_BRACKET_LIFECYCLE_STATE,
    phaseLocks: normalizePhaseLocks(bracket?.phaseLocks),
    updatedAt: new Date().toISOString(),
    picksBySlot,
    picks: legacyPicksFromPicksBySlot(picksBySlot),
  };
}

export {
  CURRENT_BRACKET_DOCUMENT_SCHEMA_VERSION,
  DEFAULT_BRACKET_LIFECYCLE_STATE,
  canEditBracketSlot,
  canMutateBracketPick,
  canonicalPickSlotsFromModel,
  createEmptyBracketDocument,
  createEmptyUserBracket,
  legacyPicksFromPicksBySlot,
  normalizeBracketDocument,
  normalizeUserBracket,
  setBracketPick,
  sitePickIdsFromSlots,
};
