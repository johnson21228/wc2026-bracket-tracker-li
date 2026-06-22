#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    site_text = read("site/index.html")
    repo_text = read("site/js/services/BracketRepository.js")
    auth_text = read("site/js/services/SupabaseAuthService.js")
    identity_text = read("site/js/identity/SupabaseIdentitySurface.js")
    config_text = read("site/js/config/supabase.public.js")

    require(
        "WC2026_SUPABASE_PUBLIC_CONFIG" in config_text,
        "Supabase publishable config must remain captured before Postgres persistence.",
        errors,
    )
    require(
        "supabasePublishableKey" in config_text,
        "Supabase config must expose a publishable key field, not a service-role secret.",
        errors,
    )
    require(
        "service_role" not in config_text.lower(),
        "Supabase public config must not include a service-role key.",
        errors,
    )

    require(
        "SupabaseAuthService" in auth_text,
        "Supabase Auth service surface must remain present.",
        errors,
    )
    require(
        "SupabaseIdentitySurface" in identity_text,
        "Supabase identity UI surface must remain present.",
        errors,
    )

    require(
        "LocalStorageBracketStore" in repo_text,
        "BracketRepository must still keep localStorage as the active bracket persistence path.",
        errors,
    )
    require(
        "new LocalStorageBracketStore()" in repo_text,
        "BracketRepository must still default to LocalStorageBracketStore.",
        errors,
    )

    # Card 231 remains the auth-before-active-Postgres-persistence guard.
    # Later Supabase-prep CBs may add an inactive SupabaseBracketStore module.
    # That is allowed only if active public runtime still does not activate remote bracket persistence.
    active_runtime_text = "\n".join([
        site_text,
        repo_text,
        auth_text,
        identity_text,
    ])

    forbidden_active_runtime_tokens = [
        ".from(\"user_brackets\")",
        ".from('user_brackets')",
        "createSupabaseBracketStore(",
        "new SupabaseBracketStore(",
        "SupabaseBracketStore.js",
        "picks_json:",
        ".upsert(",
    ]

    for token in forbidden_active_runtime_tokens:
        require(
            token not in active_runtime_text,
            f"Card 231 auth surface must not activate Supabase/Postgres bracket persistence yet: found {token}",
            errors,
        )

    inactive_store_path = ROOT / "site/js/services/SupabaseBracketStore.js"
    if inactive_store_path.exists():
        inactive_store_text = inactive_store_path.read_text()
        require(
            "class SupabaseBracketStore" in inactive_store_text
            and "loadUserBracket(userId)" in inactive_store_text
            and "saveUserBracket(bracketDocument)" in inactive_store_text,
            "Inactive SupabaseBracketStore may exist only behind the remote store seam.",
            errors,
        )
        require(
            "SupabaseBracketStore" not in repo_text,
            "BracketRepository must not activate SupabaseBracketStore during Card 231 auth-only posture.",
            errors,
        )

    if errors:
        print("Card 231 verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Supabase Auth identity surface uses current publishable-key config before active Postgres persistence while localStorage remains active.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
