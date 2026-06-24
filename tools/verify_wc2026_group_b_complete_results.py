#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read_json(rel):
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        return {}
    return json.loads(path.read_text())

matches = read_json("site/data/current/group_matches.json").get("matches", [])
by_id = {str(m.get("matchId")): m for m in matches}
expected_matches = {
    "GS-2026-06-24-B5": {
        "homeTeamId": "SUI",
        "awayTeamId": "CAN",
        "homeScore": 2,
        "awayScore": 1,
        "summary": "Switzerland 2-1 Canada",
        "currentEvidenceMatchId": "66456924",
    },
    "GS-2026-06-24-B6": {
        "homeTeamId": "BIH",
        "awayTeamId": "QAT",
        "homeScore": 3,
        "awayScore": 1,
        "summary": "Bosnia-Herzegovina 3-1 Qatar",
        "currentEvidenceMatchId": "66456926",
    },
}
for match_id, expected in expected_matches.items():
    row = by_id.get(match_id)
    if not row:
        errors.append(f"missing match row {match_id}")
        continue
    if row.get("status") != "final":
        errors.append(f"{match_id} status expected final, found {row.get('status')!r}")
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"{match_id} {key} expected {value!r}, found {row.get(key)!r}")
    if row.get("resultSource") != "public-score-research-2026-06-24":
        errors.append(f"{match_id} missing public score resultSource")
    if row.get("resultSourceUrl") != "https://www.espn.com/soccer/scoreboard/_/date/20260624":
        errors.append(f"{match_id} missing ESPN June 24 resultSourceUrl")

standings = read_json("site/data/current/group_standings.json")
entries = standings.get("groups", {}).get("B", {}).get("entries", [])
by_team = {e.get("teamId"): e for e in entries}
expected_standings = {
    "SUI": {"played": 3, "wins": 2, "draws": 1, "losses": 0, "goalsFor": 7, "goalsAgainst": 3, "goalDifference": 4, "points": 7, "rank": 1, "qualificationContext": "group-winner"},
    "CAN": {"played": 3, "wins": 1, "draws": 1, "losses": 1, "goalsFor": 8, "goalsAgainst": 3, "goalDifference": 5, "points": 4, "rank": 2, "qualificationContext": "runner-up"},
    "BIH": {"played": 3, "wins": 1, "draws": 1, "losses": 1, "goalsFor": 5, "goalsAgainst": 6, "goalDifference": -1, "points": 4, "rank": 3, "qualificationContext": "third-place-candidate"},
    "QAT": {"played": 3, "wins": 0, "draws": 1, "losses": 2, "goalsFor": 2, "goalsAgainst": 10, "goalDifference": -8, "points": 1, "rank": 4, "qualificationContext": "fourth-place"},
}
for team_id, expected in expected_standings.items():
    row = by_team.get(team_id)
    if not row:
        errors.append(f"Group B missing {team_id}")
        continue
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"Group B {team_id} {key} expected {value!r}, found {row.get(key)!r}")

third = standings.get("thirdPlaceTable", [])
third_by_group = {e.get("groupId"): e for e in third}
b = third_by_group.get("B")
if not b:
    errors.append("thirdPlaceTable missing Group B")
elif b.get("teamId") != "BIH":
    errors.append(f"thirdPlaceTable Group B expected BIH, found {b.get('teamId')!r}")
else:
    if b.get("points") != 4:
        errors.append("thirdPlaceTable BIH should have 4 points")
    if b.get("thirdPlaceRank") != 1:
        errors.append(f"thirdPlaceTable BIH should rank 1 provisionally, found {b.get('thirdPlaceRank')!r}")
    if b.get("qualificationContext") != "third-place-advancing-context":
        errors.append("thirdPlaceTable BIH should be in provisional advancing context")

required_files = [
    "source/text/group_b_result_evidence_20260624.json",
    "captures/CAPTURE_BACK_GROUP_B_COMPLETE_RESULTS.md",
    "cards/287_capture_group_b_complete_results_card.md",
]
for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

makefile = (ROOT / "Makefile").read_text()
needle = "python3 tools/verify_wc2026_group_b_complete_results.py"
if needle not in makefile:
    errors.append("Makefile verify target does not run Group B complete results verifier")

if errors:
    raise SystemExit("WC2026 Group B complete result verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 Group B complete results are captured and verified.")
