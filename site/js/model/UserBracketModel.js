import { normalizePickValue, unpickedPickValue, validatePickValue } from "./PickValue.js";

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

function isR32EntrantSlot(slot) {
  return slot?.kind === "entrant" || slot?.round === "R32_ENTRANT";
}

function teamIdFromOfficialRecord(record) {
  if (!record || typeof record !== "object") return null;
  const direct = record.teamId || record.id || record.abbr || record.code || record.team_id;
  const nested = record.team?.id || record.team?.teamId || record.team?.abbr || record.pick?.teamId || record.pick?.abbr;
  const teamId = direct || nested;
  return teamId ? String(teamId).trim().toUpperCase() : null;
}

function slotIdFromOfficialRecord(record) {
  if (!record || typeof record !== "object") return null;
  const slotId = record.slotId || record.sitePickId || record.geometrySlotId || record.fifaSlotId || record.r32SlotId;
  return slotId ? String(slotId).trim() : null;
}

function officialR32AuthoritySource(officialR32 = null) {
  if (officialR32?.officialR32AuthoritySource) return String(officialR32.officialR32AuthoritySource);
  if (officialR32?.hydratedFrom) return String(officialR32.hydratedFrom);
  if (officialR32?.source === "site-owned-official-truth") return "site/data/current/official_truth.json";
  if (officialR32?.officialR32AuthoritySource === "site/data/current/official_truth.json") return "site/data/current/official_truth.json";
  if (officialR32?.source === "Supabase:Admin_/official") return "Supabase:Admin_/official";
  if (officialR32?.userId === "Admin_/official" && officialR32?.bracketKind === "official") return "Supabase:Admin_/official";
  return "";
}

function officialR32OccupantsBySlot(officialR32 = null) {
  const occupants = {};
  const hydratedFrom = officialR32AuthoritySource(officialR32);

  const addRecord = (slotId, record) => {
    const normalizedSlotId = String(slotId || slotIdFromOfficialRecord(record) || "").trim();
    const teamId = teamIdFromOfficialRecord(record);
    if (!normalizedSlotId || !teamId) return;
    occupants[normalizedSlotId] = {
      slotId: normalizedSlotId,
      teamId,
      source: "site-owned-official-truth",
      hydratedFrom,
    };
  };

  if (Array.isArray(officialR32?.slots)) {
    for (const record of officialR32.slots) addRecord(null, record);
  }

  if (officialR32?.picksBySlot && typeof officialR32.picksBySlot === "object") {
    for (const [slotId, record] of Object.entries(officialR32.picksBySlot)) {
      if (record?.round === "R32_ENTRANT" || record?.kind === "entrant") addRecord(slotId, record);
    }
  }

  if (officialR32?.r32OccupantsBySlot && typeof officialR32.r32OccupantsBySlot === "object") {
    for (const [slotId, record] of Object.entries(officialR32.r32OccupantsBySlot)) addRecord(slotId, record);
  }

  return occupants;
}

function hasOfficialR32Occupants(officialR32 = null) {
  return Object.keys(officialR32OccupantsBySlot(officialR32)).length > 0;
}

function officialR32SlotRecord(slot, occupant, teamsById = {}) {
  const pickValue = validatePickValue({ kind: "team", teamId: occupant.teamId }, teamsById);
  return {
    slotId: slot.slotId,
    kind: "entrant",
    round: "R32_ENTRANT",
    pick: pickValue.kind === "unpicked" ? null : pickValue,
    source: "site-owned-official-truth",
    authority: "site-owned-official-truth",
    playerAuthored: false,
    hydratedFrom: occupant.hydratedFrom || "site/data/current/official_truth.json",
  };
}

function officialR32UnsetSlotRecord(slot, officialR32 = null) {
  return {
    slotId: slot.slotId,
    kind: "entrant",
    round: "R32_ENTRANT",
    pick: null,
    source: "site-owned-official-truth",
    authority: "site-owned-official-truth",
    playerAuthored: false,
    officialUnset: true,
    hydratedFrom: officialR32AuthoritySource(officialR32),
  };
}

function shouldReconcileR32FromOfficial(officialR32 = null) {
  if (!officialR32) return false;
  const source = officialR32AuthoritySource(officialR32);
  return source === "site/data/current/official_truth.json" || source === "Supabase:Admin_/official";
}

function hydrateOfficialR32Occupants({ bracket, bracketSlots, teamsById = {}, officialR32 = null } = {}) {
  const canonicalSlots = canonicalPickSlotsFromModel(bracketSlots, bracket?.gameId || "game1");
  const occupants = officialR32OccupantsBySlot(officialR32);
  if (bracket?.bracketKind === "official" || !shouldReconcileR32FromOfficial(officialR32)) return bracket;

  const picksBySlot = { ...(bracket?.picksBySlot || {}) };
  for (const slot of canonicalSlots) {
    if (!isR32EntrantSlot(slot)) continue;
    const occupant = occupants[slot.slotId] || occupants[slot.sitePickId];
    picksBySlot[slot.slotId] = occupant
      ? officialR32SlotRecord(slot, occupant, teamsById)
      : officialR32UnsetSlotRecord(slot, officialR32);
  }

  return {
    ...bracket,
    officialR32Hydration: {
      source: "site-owned-official-truth",
      appliesAt: ["creation", "load", "import", "save", "render"],
      playerAuthored: false,
      mirrorsSiteOfficialTruthExactly: true,
      failClosed: Boolean(officialR32?.r32TruthUnavailable || officialR32?.failClosed),
      hydratedFrom: officialR32AuthoritySource(officialR32),
    },
    picksBySlot,
    picks: legacyPicksFromPicksBySlot(picksBySlot),
  };
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
  teamsById = {},
  officialR32 = null,
} = {}) {
  const canonicalSlots = canonicalPickSlotsFromModel(bracketSlots, gameId);
  const picksBySlot = Object.fromEntries(
    canonicalSlots.map((slot) => [slot.slotId, slotRecordFromPickValue(slot, unpickedPickValue(), "empty")])
  );

  const document = {
    schemaVersion: 1,
    id: bracketId || `${userId || "user"}-${tournamentId}`,
    userId,
    tournamentId,
    gameId,
    status: "draft",
    expectedPickCount: canonicalSlots.length,
    createdAt: null,
    updatedAt: null,
    picksBySlot,
    // Transitional compatibility for existing render code. Durable authority is picksBySlot.
    picks: legacyPicksFromPicksBySlot(picksBySlot),
  };

  return hydrateOfficialR32Occupants({
    bracket: document,
    bracketSlots,
    teamsById,
    officialR32,
  });
}

function createEmptyUserBracket(args) {
  return createEmptyBracketDocument(args);
}

function normalizeBracketDocument({ bracket, bracketSlots, teamsById, officialR32 = null, userId = "", gameId = "game1" }) {
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

    const slotRecord = slotRecordFromPickValue(
      slot,
      pickValue,
      incomingRecord?.source || (pickValue.kind === "unpicked" ? "empty" : "user")
    );

    if (incomingRecord?.source === "Admin_/official" || incomingRecord?.authority === "Admin_/official") {
      slotRecord.source = "Admin_/official";
      slotRecord.authority = "Admin_/official";
      slotRecord.playerAuthored = false;
      slotRecord.hydratedFrom = incomingRecord?.hydratedFrom || "Supabase:Admin_/official";
    }

    picksBySlot[slot.slotId] = slotRecord;
  }

  const documentUserId = String(bracket?.userId || userId || "");
  const documentTournamentId = String(bracket?.tournamentId || "wc2026");

  const document = {
    schemaVersion: Number(bracket?.schemaVersion || 1),
    id: String(bracket?.id || `${documentUserId || "user"}-${documentTournamentId}`),
    userId: documentUserId,
    tournamentId: documentTournamentId,
    gameId: String(bracket?.gameId || gameId),
    status: String(bracket?.status || "draft"),
    expectedPickCount: canonicalSlots.length,
    createdAt: bracket?.createdAt || null,
    updatedAt: bracket?.updatedAt || null,
    picksBySlot,
    // Transitional compatibility for existing render code. Durable authority is picksBySlot.
    picks: legacyPicksFromPicksBySlot(picksBySlot),
  };

  return hydrateOfficialR32Occupants({
    bracket: document,
    bracketSlots,
    teamsById,
    officialR32,
  });
}

function normalizeUserBracket(args) {
  return normalizeBracketDocument(args);
}

function setBracketPick({ bracket, sitePickId, pickValue }) {
  const normalizedPick = normalizePickValue(pickValue);
  const existingRecord = bracket?.picksBySlot?.[sitePickId] || {
    slotId: sitePickId,
    kind: sitePickId === "CHAMPION" || sitePickId === "THIRD-PLACE-WINNER" ? "winner" : "winner",
    round: roundForLegacySlot(sitePickId, null),
  };

  if (isR32EntrantSlot(existingRecord) && bracket?.bracketKind !== "official") {
    return {
      ...bracket,
      officialR32Hydration: {
        ...(bracket?.officialR32Hydration || {}),
        source: "site-owned-official-truth",
        playerAuthored: false,
        blockedPlayerR32Authoring: true,
      },
    };
  }

  const slot = {
    slotId: sitePickId,
    kind: existingRecord.kind || "winner",
    round: existingRecord.round || roundForLegacySlot(sitePickId, null),
  };
  const officialEdit = bracket?.bracketKind === "official";
  const record = slotRecordFromPickValue(
    slot,
    normalizedPick,
    officialEdit ? "Admin_/official" : (normalizedPick.kind === "unpicked" ? "empty" : "user")
  );
  if (officialEdit) {
    record.authority = "Admin_/official";
    record.playerAuthored = false;
    record.officialTruth = true;
    record.hydratedFrom = "Supabase:Admin_/official";
  }
  const picksBySlot = {
    ...(bracket.picksBySlot || {}),
    [sitePickId]: record,
  };

  return {
    ...bracket,
    schemaVersion: Number(bracket?.schemaVersion || 1),
    updatedAt: new Date().toISOString(),
    picksBySlot,
    picks: legacyPicksFromPicksBySlot(picksBySlot),
  };
}

export {
  canonicalPickSlotsFromModel,
  createEmptyBracketDocument,
  createEmptyUserBracket,
  hasOfficialR32Occupants,
  hydrateOfficialR32Occupants,
  officialR32AuthoritySource,
  legacyPicksFromPicksBySlot,
  normalizeBracketDocument,
  normalizeUserBracket,
  setBracketPick,
  sitePickIdsFromSlots,
};
