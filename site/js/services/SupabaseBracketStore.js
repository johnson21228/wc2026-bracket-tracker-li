import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";
import { WC2026_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js";
import { normalizeBracketDocument } from "../model/UserBracketModel.js";

const DEFAULT_TABLE_NAME = "user_brackets";
const DEFAULT_GAME_ID = "game1";
const DEFAULT_VISIBILITY = "private";

function cleanUserId(userId) {
  const value = String(userId || "").trim();
  if (!value) {
    throw new Error("SupabaseBracketStore requires a signed-in user id.");
  }
  return value;
}

function assertCanonicalBracketDocument(bracketDocument) {
  if (!bracketDocument || typeof bracketDocument !== "object") {
    throw new Error("SupabaseBracketStore requires a canonical BracketDocument object.");
  }
  if (!bracketDocument.picksBySlot || typeof bracketDocument.picksBySlot !== "object") {
    throw new Error("SupabaseBracketStore.saveUserBracket requires canonical BracketDocument picksBySlot.");
  }
  if (!bracketDocument.userId) {
    throw new Error("SupabaseBracketStore.saveUserBracket requires BracketDocument.userId.");
  }
  if (!bracketDocument.gameId) {
    throw new Error("SupabaseBracketStore.saveUserBracket requires BracketDocument.gameId.");
  }
}

const LOAD_USER_BRACKET_FAILED_PREFIX = "SupabaseBracketStore loadUserBracket failed";
const SAVE_USER_BRACKET_FAILED_PREFIX = "SupabaseBracketStore saveUserBracket failed";

function supabaseErrorMessage(operation, error) {
  const detail = error?.message || error?.details || error?.hint || String(error);
  const prefix = operation === "loadUserBracket"
    ? LOAD_USER_BRACKET_FAILED_PREFIX
    : SAVE_USER_BRACKET_FAILED_PREFIX;
  return `${prefix}: ${detail}`;
}

class SupabaseBracketStore {
  constructor({
    supabaseClient = null,
    config = WC2026_SUPABASE_PUBLIC_CONFIG,
    tableName = DEFAULT_TABLE_NAME,
    gameId = DEFAULT_GAME_ID,
    visibility = DEFAULT_VISIBILITY,
    bracketSlots = null,
    teamsById = {},
  } = {}) {
    this.supabaseClient = supabaseClient;
    this.config = config;
    this.tableName = tableName;
    this.gameId = gameId;
    this.visibility = visibility;
    this.bracketSlots = bracketSlots;
    this.teamsById = teamsById;
  }

  setModelContext({ bracketSlots = this.bracketSlots, teamsById = this.teamsById } = {}) {
    this.bracketSlots = bracketSlots;
    this.teamsById = teamsById || {};
    return this;
  }

  ensureClient() {
    if (this.supabaseClient) return this.supabaseClient;

    if (!this.config?.supabaseUrl || !this.config?.supabasePublishableKey) {
      throw new Error("SupabaseBracketStore requires a Supabase URL and publishable key.");
    }

    this.supabaseClient = createClient(
      this.config.supabaseUrl,
      this.config.supabasePublishableKey,
      {
        auth: {
          persistSession: true,
          autoRefreshToken: true,
          detectSessionInUrl: true,
        },
      }
    );

    return this.supabaseClient;
  }

  normalizeForRuntime(bracketDocument, userId = bracketDocument?.userId) {
    if (!bracketDocument) return null;

    const bracket = {
      ...bracketDocument,
      userId: String(bracketDocument.userId || userId || ""),
      gameId: String(bracketDocument.gameId || this.gameId),
    };

    if (!this.bracketSlots) {
      return {
        ...bracket,
        updatedAt: bracket.updatedAt || null,
      };
    }

    return normalizeBracketDocument({
      bracket,
      bracketSlots: this.bracketSlots,
      teamsById: this.teamsById || {},
      userId: bracket.userId,
      gameId: bracket.gameId || this.gameId,
    });
  }

  async loadUserBracket(userId) {
    const cleanId = cleanUserId(userId);
    const supabase = this.ensureClient();

    const { data, error } = await supabase
      .from(this.tableName)
      .select("picks_json")
      .eq("user_id", cleanId)
      .eq("game_id", this.gameId)
      .maybeSingle();

    if (error) {
      throw new Error(supabaseErrorMessage("loadUserBracket", error));
    }

    return this.normalizeForRuntime(data?.picks_json || null, cleanId);
  }

  async saveUserBracket(bracketDocument) {
    assertCanonicalBracketDocument(bracketDocument);

    const canonical = this.normalizeForRuntime(bracketDocument, bracketDocument.userId);
    assertCanonicalBracketDocument(canonical);

    const now = new Date().toISOString();
    const documentToSave = {
      ...canonical,
      updatedAt: now,
    };

    const supabase = this.ensureClient();

    const row = {
      user_id: cleanUserId(documentToSave.userId),
      game_id: documentToSave.gameId || this.gameId,
      picks_json: documentToSave,
      visibility: this.visibility,
    };

    const { data, error } = await supabase
      .from(this.tableName)
      .upsert(row, { onConflict: "user_id,game_id" })
      .select("picks_json")
      .single();

    if (error) {
      throw new Error(supabaseErrorMessage("saveUserBracket", error));
    }

    return this.normalizeForRuntime(data?.picks_json || documentToSave, documentToSave.userId);
  }
}

function createSupabaseBracketStore(options = {}) {
  return new SupabaseBracketStore(options);
}

export {
  DEFAULT_TABLE_NAME,
  SupabaseBracketStore,
  createSupabaseBracketStore,
};
