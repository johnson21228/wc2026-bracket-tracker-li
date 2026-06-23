#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    identity = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
    app = Path("site/js/app.js").read_text()
    config = Path("site/js/config/supabase.public.js").read_text()
    live_picks = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
    makefile = Path("Makefile").read_text()

    require("WC2026_SUPABASE_PUBLIC_CONFIG" in config,
            "Supabase public config must remain the browser-owned identity configuration.", errors)
    require("supabaseUrl" in config and "supabasePublishableKey" in config,
            "Supabase public config must expose url and publishable key only.", errors)
    require("service_role" not in config.lower() and "secret" not in config.lower(),
            "Browser config must not expose service-role or secret credentials.", errors)

    require("createSupabaseIdentitySurface" in identity,
            "Identity surface must still be site-owned browser UI.", errors)
    require("Join" in identity and "Joined" in identity and "Joined as" in identity,
            "Identity surface must use Join-first player language.", errors)
    require("Profile" in identity and "Public player name" in identity,
            "Joined player profile must focus on public player name.", errors)
    require("Join to enter standings." in identity,
            "Join-first surface must connect joining to standings participation.", errors)
    require("Join the game to keep picks live and enter standings." in identity,
            "Join panel must explain live picks and standings without save/load language.", errors)
    require("Your public player name is what other players see." in identity,
            "Profile panel must keep public player name separate from private account identity.", errors)

    for forbidden in [
        "Save Picks",
        "Load Saved",
        "Bracket persistence:",
        "bracket writes are not enabled yet",
        "Bracket saving:",
        "Sign in to save",
        "Supabase Auth is not configured yet",
        "Supabase profile store",
        "Remote store",
        "Storage mode",
    ]:
        require(forbidden not in identity,
                f"Identity surface must not expose old implementation/persistence copy: {forbidden}", errors)

    require("createAccountSaveActionSurface" in app,
            "App must mount the joined live-picks persistence surface.", errors)
    require("createSupabaseIdentitySurface" in app,
            "App must mount Join/Profile identity surface.", errors)

    require("AUTOSAVE_DELAY_MS" in live_picks and "wc2026:picks-changed" in live_picks,
            "Joined picks must autosave after pick changes.", errors)
    require("saveUserBracket(bracketDocument)" in live_picks,
            "Joined live picks must write through SupabaseBracketStore seam.", errors)
    require("You already have picks saved. Use saved picks or keep this board?" in live_picks,
            "Joined conflict handling must be one explicit player choice.", errors)

    require("python3 tools/verify_wc2026_supabase_auth_identity_surface_before_postgres.py" in makefile,
            "Makefile must keep this identity boundary verifier wired.", errors)

    if errors:
        print("Join-first Supabase identity boundary verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Supabase identity boundary is Join-first, public-name based, and live-picks ready without exposing save/load/storage implementation language.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
