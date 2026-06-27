#!/usr/bin/env python3
from pathlib import Path

surface = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require('<th scope="col">Score</th>' in surface, "Player Standings must label earned-points column as Score.")
require('<th scope="col">Max Possible</th>' in surface, "Player Standings must label ceiling column as Max Possible.")

for forbidden in [
    '<th scope="col">Group</th>',
    '<th scope="col">Knockout</th>',
]:
    require(forbidden not in surface, f"Old standings header must be removed: {forbidden}")

require("player-standings-group-count" in surface, "Existing score cell class may remain for compatibility.")
require("player-standings-knockout-count" in surface, "Existing max-possible cell class may remain for compatibility.")

if errors:
    print("WC2026 Player Standings score header verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings headers now read Score and Max Possible.")
