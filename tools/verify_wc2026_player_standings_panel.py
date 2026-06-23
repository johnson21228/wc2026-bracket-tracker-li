#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    app = Path("site/js/app.js").read_text()
    standings = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
    css = Path("site/css/app.css").read_text()
    makefile = Path("Makefile").read_text()

    require('import { createPlayerStandingsSurface } from "./standings/PlayerStandingsSurface.js";' in app,
            "App must import player standings surface.", errors)
    require("createPlayerStandingsSurface({" in app,
            "App must mount player standings surface.", errors)
    require("profileStore" in app,
            "App must provide profile store to standings surface.", errors)

    require("data-player-standings-panel" in standings,
            "Standings panel must keep the player standings panel hook.", errors)
    require("standings-icon-button" in standings,
            "Standings surface must provide the standings button.", errors)
    require("syncStandingsButtonState" in standings,
            "Standings button must sync joined/not-joined state.", errors)
    require("button.disabled = !joined" in standings,
            "Standings must be disabled until joined.", errors)
    require("Join to enter standings." in standings,
            "Signed-out standings copy must use Join-first wording.", errors)
    require("Loading standings…" in standings,
            "Standings panel must provide loading state.", errors)
    require("No players yet" in standings,
            "Standings panel must provide empty state.", errors)
    require("Standings unavailable" in standings,
            "Standings panel must provide error state.", errors)
    require("fallbackParticipationRows" in standings,
            "Standings must still provide participation fallback rows.", errors)
    require("publicNameFromAuthState" in standings,
            "Standings must use public player names instead of raw identity.", errors)

    for forbidden in [
        "Sign in to join the standings",
        "login",
        "Save Picks",
        "Load Saved",
        "email",
    ]:
        require(forbidden not in standings,
                f"Standings surface must not expose stale login/save/load/private identity copy: {forbidden}", errors)

    require(".player-standings-control" in css and ".standings-icon-button" in css,
            "Standings control must have visible browser chrome styling.", errors)
    require(".standings-icon-button.is-join-required" in css or ".standings-icon-button:disabled" in css,
            "Disabled Join-required standings state must have styling.", errors)

    require("python3 tools/verify_wc2026_player_standings_panel.py" in makefile,
            "Makefile verify must include player standings verifier.", errors)

    if errors:
        print("Join-first player standings panel verification failed: " + "; ".join(errors))
        return 1

    print("OK: Player standings panel is Join-first, disabled until joined, and preserves loading/empty/error states.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
