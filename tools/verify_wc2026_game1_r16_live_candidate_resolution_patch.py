from pathlib import Path

text = Path("site/game1/index.html").read_text(encoding="utf-8")
required = [
    "WC2026_R16_LIVE_CANDIDATE_RESOLUTION_START",
    "wc2026SlotAliases",
    "R32-${side}-M${match}${leg}",
    "r16CandidateTeams = function wc2026R16CandidateTeamsFromLiveR32Picks",
    "wc2026ResolvedKnockoutContestants = function wc2026ResolvedKnockoutContestantsFromLivePicks",
    "WC2026_GAME1_R16_LIVE_CANDIDATE_RESOLUTION",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing R16 live candidate resolution markers: " + ", ".join(missing))
print("Game 1 R16 live candidate resolution verification passed.")
