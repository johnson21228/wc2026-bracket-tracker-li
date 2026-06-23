import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";
import { WC2026_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js";

const CONFIG_PLACEHOLDER_PATTERN = /YOUR_PROJECT_REF|YOUR_PUBLISHABLE_KEY/i;

function safeDisplayLabel(user) {
  const metadata = user?.user_metadata || {};
  const preferred = metadata.display_name || metadata.full_name || metadata.name || metadata.user_name;
  if (preferred) return String(preferred);
  return "Signed in";
}

function publicUserSummary(session) {
  const user = session?.user || null;
  if (!user) return null;
  return {
    id: user.id,
    label: safeDisplayLabel(user),
    email: user.email || "",
  };
}

export function isSupabaseAuthConfigured(config = WC2026_SUPABASE_PUBLIC_CONFIG) {
  if (!config?.enabled) return false;
  if (!config.supabaseUrl || !config.supabasePublishableKey) return false;
  if (CONFIG_PLACEHOLDER_PATTERN.test(config.supabaseUrl)) return false;
  if (CONFIG_PLACEHOLDER_PATTERN.test(config.supabasePublishableKey)) return false;
  return true;
}

export function createSupabaseAuthService({ config = WC2026_SUPABASE_PUBLIC_CONFIG } = {}) {
  let client = null;
  let currentSession = null;
  let currentState = {
    configured: isSupabaseAuthConfigured(config),
    status: isSupabaseAuthConfigured(config) ? "checking" : "not-configured",
    user: null,
    message: isSupabaseAuthConfigured(config) ? "Checking Supabase session…" : "Supabase Auth is not configured yet. Local bracket remains active.",
  };
  const listeners = new Set();

  function emit(nextState = currentState) {
    currentState = nextState;
    for (const listener of listeners) listener(currentState);
  }

  function stateFromSession(session, message = "") {
    currentSession = session || null;
    const user = publicUserSummary(currentSession);
    return {
      configured: true,
      status: user ? "signed-in" : "signed-out",
      user,
      message: message || (user ? "Signed in. Local bracket for now." : "Signed out. Local bracket remains active."),
    };
  }

  function ensureClient() {
    if (!isSupabaseAuthConfigured(config)) return null;
    if (!client) {
      client = createClient(config.supabaseUrl, config.supabasePublishableKey, {
        auth: {
          persistSession: true,
          autoRefreshToken: true,
          detectSessionInUrl: true,
        },
      });
    }
    return client;
  }

  async function start() {
    const supabase = ensureClient();
    if (!supabase) {
      emit(currentState);
      return currentState;
    }

    try {
      const { data, error } = await supabase.auth.getSession();
      if (error) throw error;
      emit(stateFromSession(data?.session || null));

      supabase.auth.onAuthStateChange((_event, session) => {
        emit(stateFromSession(session, session ? "Signed in. Local bracket for now." : "Signed out. Local bracket remains active."));
      });
    } catch (error) {
      emit({
        configured: true,
        status: "error",
        user: null,
        message: `Supabase Auth error: ${error?.message || String(error)}`,
      });
    }
    return currentState;
  }

  async function signInWithEmail(email) {
    const supabase = ensureClient();
    if (!supabase) {
      emit({
        configured: false,
        status: "not-configured",
        user: null,
        message: "Supabase Auth is not configured yet. Add project URL and publishable key before sign-in.",
      });
      return currentState;
    }

    const cleanEmail = String(email || "").trim();
    if (!cleanEmail) {
      emit({ ...currentState, message: "Enter an email address to request a Supabase magic link." });
      return currentState;
    }

    emit({ ...currentState, status: currentState.status === "signed-in" ? "signed-in" : "sending", message: "Sending Supabase magic link…" });
    try {
      const redirectTo = window.location.href.split("#")[0];
      const { error } = await supabase.auth.signInWithOtp({
        email: cleanEmail,
        options: { emailRedirectTo: redirectTo },
      });
      if (error) throw error;
      emit({ ...currentState, status: "link-sent", message: "Check your email for the Supabase sign-in link. Local bracket remains active." });
    } catch (error) {
      emit({ ...currentState, status: "error", message: `Supabase sign-in failed: ${error?.message || String(error)}` });
    }
    return currentState;
  }

  async function signOut() {
    const supabase = ensureClient();
    if (!supabase) return currentState;
    try {
      const { error } = await supabase.auth.signOut();
      if (error) throw error;
      emit(stateFromSession(null, "Signed out. Local bracket remains active."));
    } catch (error) {
      emit({ ...currentState, status: "error", message: `Supabase sign-out failed: ${error?.message || String(error)}` });
    }
    return currentState;
  }

  function subscribe(listener) {
    listeners.add(listener);
    listener(currentState);
    return () => listeners.delete(listener);
  }

  return { start, subscribe, signInWithEmail, signOut, currentState: () => currentState };
}
