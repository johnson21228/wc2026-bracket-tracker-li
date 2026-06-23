import { WC2026_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js";
import { isSupabaseAuthConfigured } from "./SupabaseAuthService.js";

function normalizeDisplayName(displayName) {
  return String(displayName || "").trim().replace(/\s+/g, " ");
}

function validateDisplayName(displayName) {
  const normalized = normalizeDisplayName(displayName);
  if (normalized.length < 2) return { ok: false, value: normalized, message: "Player name must be at least 2 characters." };
  if (normalized.length > 40) return { ok: false, value: normalized, message: "Player name must be 40 characters or fewer." };
  if (/[\x00-\x1F\x7F]/.test(normalized)) return { ok: false, value: normalized, message: "Player name cannot contain control characters." };
  return { ok: true, value: normalized, message: "" };
}

export function createSupabaseProfileStore({ config = WC2026_SUPABASE_PUBLIC_CONFIG } = {}) {
  let client = null;

  function ensureClient() {
    if (!isSupabaseAuthConfigured(config)) {
      throw new Error("Supabase profile store is not configured.");
    }
    if (!window.supabase?.createClient) {
      throw new Error("Supabase browser client is not loaded.");
    }
    if (!client) {
      client = window.supabase.createClient(config.supabaseUrl, config.supabasePublishableKey);
    }
    return client;
  }

  async function getProfile(userId) {
    if (!userId) return { profile: null, error: new Error("Missing signed-in user id.") };

    try {
      const supabase = ensureClient();
      const { data, error } = await supabase
        .from("profiles")
        .select("id, display_name, created_at, updated_at")
        .eq("id", userId)
        .maybeSingle();

      if (error) return { profile: null, error };
      return { profile: data || null, error: null };
    } catch (error) {
      return { profile: null, error };
    }
  }

  async function saveProfile({ userId, displayName }) {
    if (!userId) return { profile: null, error: new Error("Missing signed-in user id.") };

    const validation = validateDisplayName(displayName);
    if (!validation.ok) return { profile: null, error: new Error(validation.message) };

    try {
      const supabase = ensureClient();
      const { data, error } = await supabase
        .from("profiles")
        .upsert(
          { id: userId, display_name: validation.value },
          { onConflict: "id" },
        )
        .select("id, display_name, created_at, updated_at")
        .single();

      if (error) return { profile: null, error };
      return { profile: data, error: null };
    } catch (error) {
      return { profile: null, error };
    }
  }

  return { getProfile, saveProfile };
}
