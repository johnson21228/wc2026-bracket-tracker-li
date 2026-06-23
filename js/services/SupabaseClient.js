import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";
import { WC2026_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js";

let sharedSupabaseClient = null;

function isSupabasePublicConfigReady(config = WC2026_SUPABASE_PUBLIC_CONFIG) {
  return Boolean(
    config
    && config.enabled === true
    && typeof config.supabaseUrl === "string"
    && config.supabaseUrl.startsWith("https://")
    && typeof config.supabasePublishableKey === "string"
    && config.supabasePublishableKey.length > 0
  );
}

function getSharedSupabaseClient(config = WC2026_SUPABASE_PUBLIC_CONFIG) {
  if (!isSupabasePublicConfigReady(config)) {
    return null;
  }

  if (!sharedSupabaseClient) {
    sharedSupabaseClient = createClient(config.supabaseUrl, config.supabasePublishableKey, {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
        detectSessionInUrl: true,
      },
    });
  }

  return sharedSupabaseClient;
}

function requireSharedSupabaseClient(config = WC2026_SUPABASE_PUBLIC_CONFIG) {
  const client = getSharedSupabaseClient(config);
  if (!client) {
    throw new Error("Supabase public client is not configured.");
  }
  return client;
}

export {
  getSharedSupabaseClient,
  isSupabasePublicConfigReady,
  requireSharedSupabaseClient,
};
