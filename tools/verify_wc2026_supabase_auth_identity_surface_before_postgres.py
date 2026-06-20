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

    config = read("site/js/config/supabase.public.js")
    service = read("site/js/services/SupabaseAuthService.js")
    surface = read("site/js/identity/SupabaseIdentitySurface.js")
    app = read("site/js/app.js")
    index = read("site/index.html")
    css = read("site/css/app.css")

    optional_text = ""
    for rel in [
        "cards/231_implement_supabase_auth_identity_surface_before_postgres_card.md",
        "docs/architecture/bracketeering_supabase_auth_identity_surface.md",
        "li/world_cup/supabase_auth_identity_surface_before_postgres_rule.md",
    ]:
        path = ROOT / rel
        if path.exists():
            optional_text += "\n" + path.read_text(encoding="utf-8", errors="ignore")

    combined_site_js = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in (ROOT / "site/js").rglob("*.js")
    )

    require("WC2026_SUPABASE_PUBLIC_CONFIG" in config, "public Supabase config export missing", errors)
    require("enabled: true" in config, "Supabase Auth public config should be enabled", errors)
    require("https://tkjqsegszveugdvoeits.supabase.co" in config, "Supabase project URL is not configured", errors)
    require("supabasePublishableKey" in config, "config should use supabasePublishableKey", errors)
    require("sb_publishable_wWTMppX8T5nOplM4s_HA7A_bgUn337M" in config, "publishable key is not configured", errors)
    require("supabaseAnonKey" not in config, "legacy supabaseAnonKey should not remain in config", errors)

    require("createClient" in service, "Auth service should initialize Supabase client", errors)
    require("supabasePublishableKey" in service, "Auth service should read supabasePublishableKey", errors)
    require("getSession" in service, "Auth service should read current session", errors)
    require("onAuthStateChange" in service, "Auth service should listen for auth state changes", errors)
    require("signInWithOtp" in service, "Auth service should support magic-link/OTP sign-in", errors)
    require("signOut" in service, "Auth service should support sign out", errors)

    require("SupabaseIdentitySurface" in surface, "identity surface module missing", errors)
    require("Sign in to save" in surface, "identity surface should show sign-in copy", errors)
    require("Local bracket for now" in surface, "identity surface should state local bracket status before Postgres persistence", errors)

    require("SupabaseIdentitySurface" in app, "app should mount identity surface", errors)
    require("identity" in index.lower(), "index should contain an identity surface mount/slot", errors)
    require("identity" in css.lower(), "CSS should style identity surface", errors)

    require("publishable key" in optional_text.lower(), "Card/docs/LI should mention publishable key terminology", errors)

    forbidden_secret_tokens = [
        "service_role",
        "database password",
        "jwt secret",
    ]
    for token in forbidden_secret_tokens:
        require(token not in combined_site_js.lower(), f"site JS must not contain server-only secret wording: {token}", errors)

    forbidden_persistence_patterns = [
        ".from(\"user_brackets\")",
        ".from('user_brackets')",
        ".from(`user_brackets`)",
        "picks_json",
        "SupabaseBracketStore",
        ".upsert(",
        ".insert(",
    ]
    for token in forbidden_persistence_patterns:
        require(
            token.lower() not in combined_site_js.lower(),
            f"Card 231 must not introduce Supabase/Postgres bracket persistence yet: found {token}",
            errors,
        )

    if errors:
        print("Card 231 verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Supabase Auth identity surface uses current publishable-key config before Postgres persistence while localStorage remains active.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
