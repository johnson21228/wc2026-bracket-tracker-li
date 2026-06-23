#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"Missing required file: {rel}")
    return path.read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    client = read("site/js/services/SupabaseClient.js")
    auth = read("site/js/services/SupabaseAuthService.js")
    profile = read("site/js/services/SupabaseProfileStore.js")
    bracket = read("site/js/services/SupabaseBracketStore.js")
    smoke = read("site/js/dev/SupabaseBracketStoreSmokeTest.js")

    require("let sharedSupabaseClient = null" in client, "SupabaseClient must cache one shared browser client.", errors)
    require("function getSharedSupabaseClient" in client, "SupabaseClient must expose getSharedSupabaseClient.", errors)
    require("function requireSharedSupabaseClient" in client, "SupabaseClient must expose requireSharedSupabaseClient.", errors)
    require("createClient(config.supabaseUrl, config.supabasePublishableKey" in client, "SupabaseClient must use canonical public config names.", errors)
    require("persistSession: true" in client and "autoRefreshToken: true" in client and "detectSessionInUrl: true" in client, "SupabaseClient must own shared auth session options.", errors)

    for rel, text in {
        "site/js/services/SupabaseAuthService.js": auth,
        "site/js/services/SupabaseProfileStore.js": profile,
        "site/js/services/SupabaseBracketStore.js": bracket,
    }.items():
        require("@supabase/supabase-js" not in text, f"{rel} must not import Supabase createClient directly.", errors)
        require("window.supabase.createClient" not in text and "createClient(" not in text, f"{rel} must not create a separate Supabase client.", errors)

    require("getSharedSupabaseClient" in auth, "SupabaseAuthService must use the shared browser client.", errors)
    require("isSupabasePublicConfigReady" in auth, "SupabaseAuthService must share public config readiness logic.", errors)
    require("requireSharedSupabaseClient" in profile, "SupabaseProfileStore must use the shared browser client.", errors)
    require("requireSharedSupabaseClient" in bracket, "SupabaseBracketStore must use the shared browser client.", errors)

    require("new SupabaseBracketStore" in smoke, "Smoke test must still exercise SupabaseBracketStore.", errors)
    require("devSupabaseBracketSmoke" in read("site/js/app.js"), "Smoke test must remain dev-query gated from app startup.", errors)
    require("createSupabaseBracketRepository" not in read("site/js/app.js"), "Normal app startup must still not enable remote gameplay persistence.", errors)

    if errors:
        print("Shared Supabase browser client verification failed: " + "; ".join(errors))
        return 1

    print("OK: Auth, ProfileStore, BracketStore, and smoke test share one Supabase browser client boundary.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
