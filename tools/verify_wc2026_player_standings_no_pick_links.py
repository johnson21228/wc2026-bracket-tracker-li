#!/usr/bin/env python3
from pathlib import Path

surface = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

for forbidden in [
    "data-player-board-viewer-open",
    "player-standings-player-button",
    "openBoardButton",
    "View picks",
    "View player picks",
    "Open picks",
    "Open player picks",
    "View bracket",
    "Open bracket",
    "picks on the board",
]:
    require(forbidden not in surface, f"Player Standings must not expose pick/bracket link token: {forbidden}")

require("player-standings-player-summary" in surface, "Player rows must still show a non-interactive player summary")
require("player-standings-player-name" in surface, "Player rows must still show public player names")
require("data-player-standings-panel" in surface, "Player Standings panel must remain present")
require("standingsStore?.listPlayerStandings?.()" in surface, "Player Standings must still read storage-backed rows")

if errors:
    print("WC2026 Player Standings no pick links verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings lists players without links/buttons to player picks.")
