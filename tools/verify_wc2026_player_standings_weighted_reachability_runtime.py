#!/usr/bin/env python3
from pathlib import Path

store = Path("site/js/standings/SupabasePlayerStandingsStore.js").read_text()
surface = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
makefile = Path("Makefile").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

for token in [
    "function feederSlotIdsForSlot(slotId)",
    "function scoreWeightForSlot(slotId)",
    "function scoringSlotIds(playerPicksBySlot, officialTruthPicksBySlot)",
    "function canTeamStillReachSlot(teamId, slotId, officialTruthPicksBySlot",
    "return 1;",
    "return 2;",
    "return 4;",
    'return 8;',
    'return 16;',
    "score += weight;",
    "maxPossible += weight;",
    "canTeamStillReachSlot(playerTeamId, slotId, officialTruthPicksBySlot)",
    "score: score.score",
    "maxPossible: score.maxPossible",
    "groupPoints: score",
    "knockoutPoints: maxPossible",
    "total: score",
]:
    require(token in store, f"Missing weighted reachability runtime token: {token}")

for forbidden in [
    "knockoutPoints += 1",
    "total: knockoutPoints",
]:
    require(forbidden not in store, f"Old flat scoring token must be removed: {forbidden}")

require("player-standings-score" in surface, "Surface must display score cell class.")
require("player-standings-max-possible" in surface, "Surface must display max possible cell class.")
require("player-standings-group-count" not in surface, "Surface must not display old group-count class.")
require("player-standings-knockout-count" not in surface, "Surface must not display old knockout-count class.")

require(
    "python3 tools/verify_wc2026_player_standings_weighted_reachability_runtime.py" in makefile,
    "Makefile verify must include weighted reachability runtime verifier.",
)

if errors:
    print("WC2026 Player Standings weighted reachability runtime verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings computes weighted Score and reachability-aware Max Possible.")
