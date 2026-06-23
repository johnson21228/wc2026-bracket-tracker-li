#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    identity = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
    profile_store = Path("site/js/services/SupabaseProfileStore.js").read_text()
    standings = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
    app = Path("site/js/app.js").read_text()
    makefile = Path("Makefile").read_text()

    require("Public player name" in identity,
            "Identity surface must let joined users edit public player name.", errors)
    require("Update player name" in identity,
            "Profile step must use Join-first player-name update copy.", errors)
    require("Your public player name is what other players see." in identity,
            "Identity UI must distinguish public player name from private account identity.", errors)
    require("Profile" in identity and "Joined status" in identity,
            "Supabase identity chip/panel must expose Join-first Profile state.", errors)
    require("Picks:" in identity and "live after joining" in identity,
            "Profile step must describe live picks after joining.", errors)

    require('.from("profiles")' in profile_store,
            "Profile persistence must live in SupabaseProfileStore.", errors)
    require(".upsert(" in profile_store and "display_name" in profile_store,
            "SupabaseProfileStore must upsert display_name.", errors)
    require("email" not in profile_store.lower(),
            "Profile store must not persist or expose raw email as player identity.", errors)

    require("publicNameFromAuthState" in standings,
            "Standings must resolve public player names from auth/profile state.", errors)
    require("profileStore" in standings,
            "Standings surface must use profile store for public player names.", errors)

    require("createSupabaseProfileStore" in app and "profileStore" in app,
            "App must wire SupabaseProfileStore into identity and standings surfaces.", errors)

    for forbidden in [
        "Signed in as:",
        "Save player name",
        "Bracket saving:",
        "not enabled yet",
        "Sign in to save",
        "Save Picks",
        "Load Saved",
        "Supabase-backed profile",
    ]:
        require(forbidden not in identity,
                f"Profile UI must not expose stale pre-Join copy: {forbidden}", errors)

    require("python3 tools/verify_wc2026_supabase_profile_store_public_player_name.py" in makefile,
            "Makefile verify must include public player name verifier.", errors)

    if errors:
        print("Join-first public player name verification failed: " + "; ".join(errors))
        return 1

    print("OK: Supabase profile store supports Join-first public player names without exposing email or stale save/load copy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
