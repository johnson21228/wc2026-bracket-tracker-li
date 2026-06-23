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

    auth = read("site/js/services/SupabaseAuthService.js")
    surface = read("site/js/identity/SupabaseIdentitySurface.js")
    profile_store = read("site/js/services/SupabaseProfileStore.js")

    require("createSupabaseAuthService" in auth, "Supabase Auth service must remain the identity boundary.", errors)
    require("createSupabaseIdentitySurface" in surface, "Identity surface must remain site-owned.", errors)
    require("[data-supabase-identity-surface]" in surface, "Identity surface must render into the existing sign-in mount.", errors)
    require("Bracket persistence:" in surface, "Identity surface should state local bracket status before remote bracket persistence.", errors)
    require("Supabase bracket writes are not enabled yet" in surface, "Identity surface must clearly say bracket writes are not enabled yet.", errors)
    require("Bracket saving:" in surface and "not enabled yet" in surface, "Signed-in panel must still say bracket saving is not enabled yet.", errors)

    # Profile persistence is now allowed after the Supabase profiles SQL was applied.
    require('.from("profiles")' in profile_store, "Profile persistence must live in SupabaseProfileStore.", errors)
    require(".upsert(" in profile_store, "SupabaseProfileStore should upsert public player names.", errors)
    require("display_name" in profile_store, "SupabaseProfileStore must persist display_name.", errors)

    # Bracket persistence is still intentionally blocked in this step.
    combined_identity_surface = "\n".join([auth, surface, profile_store])
    forbidden_tokens = [
        '.from("user_brackets")',
        ".from('user_brackets')",
        ".from(`user_brackets`)",
        "SupabaseBracketStore",
        "bracket_json",
        "picks_json",
    ]
    for token in forbidden_tokens:
        require(
            token.lower() not in combined_identity_surface.lower(),
            f"Card 231 must not introduce Supabase/Postgres bracket persistence yet: found {token}",
            errors,
        )

    if errors:
        print("Card 231 verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Supabase Auth identity surface allows profile-only public player names while remote bracket persistence remains disabled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
