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

    store = read("site/js/services/SupabaseProfileStore.js")
    identity = read("site/js/identity/SupabaseIdentitySurface.js")
    app = read("site/js/app.js")
    makefile = read("Makefile")

    require("createSupabaseProfileStore" in store, "SupabaseProfileStore factory must exist.", errors)
    require('.from("profiles")' in store, "Profile store must use public.profiles.", errors)
    require("display_name" in store, "Profile store must read/write display_name.", errors)
    require(".upsert(" in store, "Profile store must upsert the signed-in user's profile.", errors)
    require("maybeSingle()" in store, "Profile store must handle a missing profile row.", errors)
    require("normalizeDisplayName" in store and "validateDisplayName" in store, "Profile store must normalize and validate public player names.", errors)

    require("profileStore = null" in identity, "Identity surface must accept the profile store seam.", errors)
    require("Public player name" in identity, "Identity surface must render a public player name field.", errors)
    require("Save player name" in identity, "Identity surface must let signed-in users save player name.", errors)
    require("Do not use your private email as your player name" in identity, "Identity surface must protect email/player-name distinction.", errors)
    require("Bracket saving:" in identity and "not enabled yet" in identity, "Profile step must not enable bracket saving.", errors)

    require('import { createSupabaseProfileStore } from "./services/SupabaseProfileStore.js";' in app, "App must import SupabaseProfileStore.", errors)
    require("const profileStore = createSupabaseProfileStore();" in app, "App must instantiate SupabaseProfileStore.", errors)
    require("createSupabaseIdentitySurface({ root, authService, profileStore })" in app, "App must pass ProfileStore into identity surface.", errors)

    forbidden_store_tokens = [
        'from("user_brackets")',
        "bracket_json",
        "picks_json",
        "BracketDocument",
        "SupabaseBracketStore",
    ]
    for token in forbidden_store_tokens:
        require(token not in store, f"Profile store must not touch bracket persistence: {token}", errors)

    require(
        "python3 tools/verify_wc2026_supabase_profile_store_public_player_name.py" in makefile,
        "Makefile verify must include the public player name profile-store verifier.",
        errors,
    )

    if errors:
        print("Supabase profile store public player name verification failed: " + "; ".join(errors))
        return 1

    print("OK: SupabaseProfileStore public player name step is wired without enabling bracket save/load.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
