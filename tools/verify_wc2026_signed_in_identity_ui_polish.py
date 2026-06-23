#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    identity = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
    profile_store = Path("site/js/services/SupabaseProfileStore.js").read_text()
    app = Path("site/js/app.js").read_text()
    makefile = Path("Makefile").read_text()

    require("createSupabaseIdentitySurface" in identity,
            "Identity surface must remain the site-owned player surface.", errors)
    require("Profile" in identity,
            "Joined player button must collapse to a concise Profile control.", errors)
    require("Join" in identity and "Joined" in identity and "Joined as" in identity,
            "Identity UI must use Join-first player-facing states.", errors)
    require("Public player name" in identity,
            "Profile panel must edit public player name.", errors)
    require("Your public player name is what other players see." in identity,
            "Profile panel must explain public player identity.", errors)
    require("Joined status" in identity,
            "Profile panel must show joined status.", errors)
    require("Picks:" in identity and "live after joining" in identity,
            "Profile panel must describe live picks after joining.", errors)
    require("Join to keep picks live and enter standings." in identity,
            "Join panel must explain the joined-play benefit.", errors)
    require("Before joining, this board is temporary browser play." in identity,
            "Anonymous local exploration must remain available before joining.", errors)

    require('.from("profiles")' in profile_store,
            "Public player name persistence must remain in SupabaseProfileStore.", errors)
    require(".upsert(" in profile_store and "display_name" in profile_store,
            "Profile store must still upsert public display names.", errors)
    require("createSupabaseIdentitySurface({" in app and "profileStore" in app,
            "App must mount identity surface with profile store.", errors)

    for forbidden in [
        "Sign in to save",
        "Signed in as:",
        "Close sign-in panel",
        "Bracket saving:",
        "bracket saving is not enabled",
        "Supabase-backed profile",
        "Supabase profile store",
        "login",
        "Save Picks",
        "Load Saved",
        "Storage mode",
        "Remote store",
    ]:
        require(forbidden not in identity,
                f"Signed-in player UI must not expose old login/storage copy: {forbidden}", errors)

    require("python3 tools/verify_wc2026_signed_in_identity_ui_polish.py" in makefile,
            "Makefile verify must keep signed-in identity polish verifier wired.", errors)

    if errors:
        print("Join-first signed-in identity UI polish verification failed: " + "; ".join(errors))
        return 1

    print("OK: signed-in identity UI is Join-first: concise Profile control, public player name editing, joined status, and live-picks copy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
