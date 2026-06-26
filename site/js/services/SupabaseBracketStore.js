import { WC2026_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js";
import { requireSharedSupabaseClient } from "./SupabaseClient.js";
import { normalizeBracketDocument } from "../model/UserBracketModel.js";
import { BracketStorageAdapter } from "./BracketStorageAdapter.js";
import { isSupabaseAuthConfigured } from "./SupabaseAuthService.js";

const DEFAULT_TOURNAMENT_ID = "wc2026";
const DEFAULT_GAME_ID = "game1";
const DEFAULT_VISIBILITY = "private";
const ADMIN_OFFICIAL_USER_ID = "Admin_/official";
const ADMIN_OFFICIAL_AUTHORITY_SOURCE = "Supabase:Admin_/official";
const TABLE_NAME = "user_brackets";

const REQUIRED_BRACKET_DOCUMENT_KEYS = Object.freeze([
  "schemaVersion",
  "userId",
  "tournamentId",
  "gameId",
  "status",
  "lifecycleState",
  "phaseLocks",
  "picksBySlot",
  "createdAt",
  "updatedAt",
  "submittedAt",
  "lockedAt",
  "visibility",
]);

function assertPlainObject(value, message) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new Error(message);
  }
}

function canonicalSlotsFromPicksBySlot(picksBySlot, gameId) {
  return Object.values(picksBySlot || {}).map((record) => ({
    slotId: record?.slotId,
    sitePickId: record?.slotId,
    kind: record?.kind || "winner",
    round: record?.round || "UNKNOWN",
    gameId,
  })).filter((slot) => slot.slotId);
}

function teamsByIdFromPicksBySlot(picksBySlot) {
  const teamsById = {};
  for (const record of Object.values(picksBySlot || {})) {
    const teamId = record?.pick?.kind === "team" ? record.pick.teamId : record?.teamId;
    if (teamId) teamsById[teamId] = { id: teamId };
  }
  return teamsById;
}

function normalizeVisibility(value) {
  return value === "public" ? "public" : DEFAULT_VISIBILITY;
}

function normalizeStatus(value) {
  if (["draft", "submitted", "locked", "archived"].includes(value)) return value;
  return "draft";
}

function normalizeRemoteBracketDocument({ bracket, userId }) {
  assertPlainObject(bracket, "SupabaseBracketStore requires a canonical BracketDocument object.");
  assertPlainObject(bracket.picksBySlot, "SupabaseBracketStore requires BracketDocument.picksBySlot.");

  const now = new Date().toISOString();
  const gameId = String(bracket.gameId || DEFAULT_GAME_ID);
  const tournamentId = String(bracket.tournamentId || DEFAULT_TOURNAMENT_ID);

  const normalizedCore = normalizeBracketDocument({
    bracket: {
      ...bracket,
      userId,
      tournamentId,
      gameId,
      status: normalizeStatus(bracket.status),
    },
    bracketSlots: {
      canonicalPickSlots: canonicalSlotsFromPicksBySlot(bracket.picksBySlot, gameId),
    },
    teamsById: teamsByIdFromPicksBySlot(bracket.picksBySlot),
    userId,
    gameId,
  });

  const canonicalBracketDocument = {
    ...normalizedCore,
    schemaVersion: Number(bracket.schemaVersion || normalizedCore.schemaVersion || 1),
    userId,
    tournamentId,
    gameId,
    status: normalizeStatus(bracket.status || normalizedCore.status),
    lifecycleState: bracket.lifecycleState || {},
    phaseLocks: bracket.phaseLocks || {},
    picksBySlot: normalizedCore.picksBySlot,
    createdAt: bracket.createdAt || now,
    updatedAt: now,
    submittedAt: bracket.submittedAt || null,
    lockedAt: bracket.lockedAt || null,
    visibility: normalizeVisibility(gameId === "game1" ? "public" : bracket.visibility),
  };

  for (const key of REQUIRED_BRACKET_DOCUMENT_KEYS) {
    if (!(key in canonicalBracketDocument)) {
      throw new Error(`SupabaseBracketStore refused to save incomplete BracketDocument; missing ${key}.`);
    }
  }

  return canonicalBracketDocument;
}

class SupabaseBracketStore extends BracketStorageAdapter {
  constructor({
    config = WC2026_SUPABASE_PUBLIC_CONFIG,
    tournamentId = DEFAULT_TOURNAMENT_ID,
    gameId = DEFAULT_GAME_ID,
  } = {}) {
    super();
    this.config = config;
    this.tournamentId = tournamentId;
    this.gameId = gameId;
    this.client = null;
  }

  ensureClient() {
    if (!isSupabaseAuthConfigured(this.config)) {
      throw new Error("SupabaseBracketStore is not configured.");
    }

    if (!this.client) {
      this.client = requireSharedSupabaseClient(this.config);
    }

    return this.client;
  }

  async requireSignedInUser() {
    const supabase = this.ensureClient();
    const { data, error } = await supabase.auth.getUser();

    if (error) throw error;

    const user = data?.user || null;
    if (!user?.id) {
      throw new Error("SupabaseBracketStore requires a signed-in Supabase user.");
    }

    return user;
  }

  async loadUserBracket(userId, { tournamentId = this.tournamentId, gameId = this.gameId } = {}) {
    const user = await this.requireSignedInUser();
    const requestedUserId = String(userId || "");

    if (requestedUserId && requestedUserId !== user.id) {
      throw new Error("SupabaseBracketStore can only load the signed-in user's bracket.");
    }

    const supabase = this.ensureClient();
    const { data, error } = await supabase
      .from(TABLE_NAME)
      .select("bracket_json, bracket_kind")
      .eq("user_id", user.id)
      .eq("tournament_id", tournamentId)
      .eq("game_id", gameId)
      .maybeSingle();

    if (error) throw error;
    return data?.bracket_json
      ? { ...data.bracket_json, bracketKind: data.bracket_kind || data.bracket_json.bracketKind || "player" }
      : null;
  }

  async loadOfficialR32BracketAuthority({ tournamentId = this.tournamentId, gameId = this.gameId } = {}) {
    const supabase = this.ensureClient();
    const { data, error } = await supabase
      .from(TABLE_NAME)
      .select("bracket_json, bracket_kind, user_id, status, visibility")
      .eq("user_id", ADMIN_OFFICIAL_USER_ID)
      .eq("tournament_id", tournamentId)
      .eq("game_id", gameId)
      .eq("bracket_kind", "official")
      .maybeSingle();

    if (error) throw error;
    if (!data?.bracket_json) return null;

    return {
      ...data.bracket_json,
      userId: ADMIN_OFFICIAL_USER_ID,
      bracketKind: data.bracket_kind || data.bracket_json.bracketKind || "official",
      status: data.status || data.bracket_json.status || "locked",
      visibility: data.visibility || data.bracket_json.visibility || "public",
      officialR32AuthoritySource: ADMIN_OFFICIAL_AUTHORITY_SOURCE,
      source: ADMIN_OFFICIAL_AUTHORITY_SOURCE,
      authority: "Admin_/official",
    };
  }

  async loadOfficialBracket(options = {}) {
    return this.loadOfficialR32BracketAuthority(options);
  }

  async saveOfficialR32BracketAuthority(bracket, { tournamentId = this.tournamentId, gameId = this.gameId } = {}) {
    await this.requireSignedInUser();

    assertPlainObject(bracket, "SupabaseBracketStore requires an Admin_/official BracketDocument object.");
    assertPlainObject(bracket.picksBySlot, "SupabaseBracketStore requires Admin_/official picksBySlot.");

    const now = new Date().toISOString();
    const canonicalBracketDocument = {
      ...bracket,
      schemaVersion: Number(bracket.schemaVersion || 1),
      userId: ADMIN_OFFICIAL_USER_ID,
      tournamentId,
      gameId,
      status: bracket.status || "draft",
      lifecycleState: {
        ...(bracket.lifecycleState || {}),
        source: bracket.lifecycleState?.source || "admin-official-r32-editor-mode",
        lastSaveReason: bracket.lifecycleState?.lastSaveReason || "admin-official-r32-edit",
      },
      phaseLocks: bracket.phaseLocks || { r32LockedAt: null },
      picksBySlot: bracket.picksBySlot,
      createdAt: bracket.createdAt || now,
      updatedAt: now,
      submittedAt: bracket.submittedAt || null,
      lockedAt: bracket.lockedAt || null,
      visibility: "public",
      bracketKind: "official",
      officialR32AuthoritySource: ADMIN_OFFICIAL_AUTHORITY_SOURCE,
      officialResultsTruthSource: ADMIN_OFFICIAL_AUTHORITY_SOURCE,
      source: ADMIN_OFFICIAL_AUTHORITY_SOURCE,
      authority: "Admin_/official",
    };

    for (const key of REQUIRED_BRACKET_DOCUMENT_KEYS) {
      if (!(key in canonicalBracketDocument)) {
        throw new Error(`SupabaseBracketStore refused to save incomplete Admin_/official BracketDocument; missing ${key}.`);
      }
    }

    const supabase = this.ensureClient();
    const { data, error } = await supabase
      .from(TABLE_NAME)
      .upsert(
        {
          user_id: ADMIN_OFFICIAL_USER_ID,
          tournament_id: canonicalBracketDocument.tournamentId,
          game_id: canonicalBracketDocument.gameId,
          status: canonicalBracketDocument.status,
          visibility: canonicalBracketDocument.visibility,
          bracket_kind: "official",
          bracket_json: canonicalBracketDocument,
        },
        { onConflict: "user_id,tournament_id,game_id" },
      )
      .select("bracket_json, bracket_kind, user_id, status, visibility")
      .single();

    if (error) throw error;

    return {
      ...(data?.bracket_json || canonicalBracketDocument),
      userId: ADMIN_OFFICIAL_USER_ID,
      bracketKind: data?.bracket_kind || "official",
      status: data?.status || canonicalBracketDocument.status,
      visibility: data?.visibility || "public",
      officialR32AuthoritySource: ADMIN_OFFICIAL_AUTHORITY_SOURCE,
      source: ADMIN_OFFICIAL_AUTHORITY_SOURCE,
      authority: "Admin_/official",
    };
  }

  async saveAdminOfficialBracketTruth(bracket, options = {}) {
    return this.saveOfficialR32BracketAuthority({
      ...bracket,
      lifecycleState: {
        ...(bracket?.lifecycleState || {}),
        source: "admin-official-full-bracket-editor-mode",
        lastSaveReason: bracket?.lifecycleState?.lastSaveReason || "admin-official-full-bracket-edit",
      },
    }, options);
  }

  async saveUserBracket(bracket) {
    const user = await this.requireSignedInUser();
    const bracketUserId = String(bracket?.userId || user.id);

    if (bracketUserId !== user.id) {
      throw new Error("SupabaseBracketStore can only save the signed-in user's bracket.");
    }

    const canonicalBracketDocument = normalizeRemoteBracketDocument({
      bracket: {
        ...bracket,
        userId: user.id,
        tournamentId: bracket?.tournamentId || this.tournamentId,
        gameId: bracket?.gameId || this.gameId,
      },
      userId: user.id,
    });

    const supabase = this.ensureClient();
    const { data, error } = await supabase
      .from(TABLE_NAME)
      .upsert(
        {
          user_id: user.id,
          tournament_id: canonicalBracketDocument.tournamentId,
          game_id: canonicalBracketDocument.gameId,
          status: canonicalBracketDocument.status,
          visibility: canonicalBracketDocument.visibility,
          bracket_kind: canonicalBracketDocument.bracketKind === "official" ? "official" : "player",
          bracket_json: canonicalBracketDocument,
        },
        { onConflict: "user_id,tournament_id,game_id" },
      )
      .select("bracket_json")
      .single();

    if (error) throw error;
    return data?.bracket_json || canonicalBracketDocument;
  }

  async listUsers() {
    const user = await this.requireSignedInUser();
    return [user.id];
  }
}

function createSupabaseBracketStore(options = {}) {
  return new SupabaseBracketStore(options);
}

export {
  ADMIN_OFFICIAL_USER_ID,
  ADMIN_OFFICIAL_AUTHORITY_SOURCE,
  SupabaseBracketStore,
  createSupabaseBracketStore,
};
