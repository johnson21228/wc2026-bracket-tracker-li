#!/usr/bin/env python3
from pathlib import Path

paths = [
    Path("li/world_cup/player_standings_scoring_vocabulary_rule.md"),
    Path("docs/features/player_standings_scoring_vocabulary.md"),
    Path("cards/296_player_standings_scoring_vocabulary_card.md"),
    Path("captures/CAPTURE_BACK_PLAYER_STANDINGS_SCORING_VOCABULARY.md"),
]

surface = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
makefile = Path("Makefile").read_text()
combined = "\n".join(path.read_text() for path in paths if path.exists())

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

for path in paths:
    require(path.exists(), f"Missing governance/doc file: {path}")

for token in [
    "Player Standings is a scoring table",
    "not a Group/Knockout category table",
    "`Score`",
    "`Max Possible`",
    "temporary storage-boundary compatibility inputs",
]:
    require(token in combined, f"Missing scoring vocabulary token: {token}")

require('<th scope="col">Score</th>' in surface, "Standings table must render Score header.")
require('<th scope="col">Max Possible</th>' in surface, "Standings table must render Max Possible header.")
require('<th scope="col">Group</th>' not in surface, "Standings table must not render Group header.")
require('<th scope="col">Knockout</th>' not in surface, "Standings table must not render Knockout header.")

require("player-standings-score" in surface, "Standings surface must use score cell class.")
require("player-standings-max-possible" in surface, "Standings surface must use max possible cell class.")
require("player-standings-group-count" not in surface, "Old group-count display class must not remain.")
require("player-standings-knockout-count" not in surface, "Old knockout-count display class must not remain.")

require("python3 tools/verify_wc2026_player_standings_scoring_vocabulary.py" in makefile,
        "Makefile verify must include scoring vocabulary verifier.")

if errors:
    print("WC2026 Player Standings scoring vocabulary verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings scoring vocabulary LI is captured and visible headers use Score/Max Possible.")
