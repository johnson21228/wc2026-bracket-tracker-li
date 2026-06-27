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

require("player-standings-score" in surface, "Player Standings score cell class must use score language.")
require("player-standings-max-possible" in surface, "Player Standings max possible cell class must use max-possible language.")
require("player-standings-group-count" not in surface, "Old group-count display class must be removed.")
require("player-standings-knockout-count" not in surface, "Old knockout-count display class must be removed.")

if errors:
    print("WC2026 Player Standings score header verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings headers now read Score and Max Possible.")
