#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        return {}
    return json.loads(path.read_text())

matches = read("site/data/current/group_matches.json").get("matches", [])
by_id = {str(m.get("matchId")): m for m in matches}
expected_matches = {
    "GS-2026-06-23-K3": {"homeTeamId":"POR","awayTeamId":"UZB","homeScore":5,"awayScore":0,"summary":"Portugal 5-0 Uzbekistan","currentEvidenceMatchId":"760461"},
    "GS-2026-06-23-L3": {"homeTeamId":"ENG","awayTeamId":"GHA","homeScore":0,"awayScore":0,"summary":"England 0-0 Ghana","currentEvidenceMatchId":"760458"},
    "GS-2026-06-23-L4": {"homeTeamId":"PAN","awayTeamId":"CRO","homeScore":0,"awayScore":1,"summary":"Panama 0-1 Croatia","currentEvidenceMatchId":"760460"},
    "GS-2026-06-23-K4": {"homeTeamId":"COL","awayTeamId":"COD","homeScore":1,"awayScore":0,"summary":"Colombia 1-0 Congo DR","currentEvidenceMatchId":"760459"},
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
    if not str(row.get("resultSourceUrl", "")).startswith("https://"):
        errors.append(f"{match_id} missing https resultSourceUrl")
    if not str(row.get("resultSource", "")).startswith("public-score-research"):
        errors.append(f"{match_id} missing public-score-research resultSource")

standings = read("site/data/current/group_standings.json")
checks = {
    "K": {
        "COL": {"played":2,"wins":2,"points":6,"goalsFor":4,"goalsAgainst":1,"goalDifference":3,"rank":1},
        "POR": {"played":2,"wins":1,"draws":1,"points":4,"goalsFor":6,"goalsAgainst":1,"goalDifference":5,"rank":2},
        "COD": {"played":2,"draws":1,"losses":1,"points":1,"goalsFor":1,"goalsAgainst":2,"goalDifference":-1,"rank":3},
        "UZB": {"played":2,"losses":2,"points":0,"goalsFor":1,"goalsAgainst":8,"goalDifference":-7,"rank":4},
    },
    "L": {
        "ENG": {"played":2,"wins":1,"draws":1,"points":4,"goalsFor":4,"goalsAgainst":2,"goalDifference":2,"rank":1},
        "GHA": {"played":2,"wins":1,"draws":1,"points":4,"goalsFor":1,"goalsAgainst":0,"goalDifference":1,"rank":2},
        "CRO": {"played":2,"wins":1,"losses":1,"points":3,"goalsFor":3,"goalsAgainst":4,"goalDifference":-1,"rank":3},
        "PAN": {"played":2,"losses":2,"points":0,"goalsFor":0,"goalsAgainst":2,"goalDifference":-2,"rank":4},
    },
}
for group_id, group_checks in checks.items():
    entries = standings.get("groups", {}).get(group_id, {}).get("entries", [])
    by_team = {e.get("teamId"): e for e in entries}
    for team_id, expected in group_checks.items():
        row = by_team.get(team_id)
        if not row:
            errors.append(f"Group {group_id} missing {team_id}")
            continue
        for key, value in expected.items():
            if row.get(key) != value:
                errors.append(f"Group {group_id} {team_id} {key} expected {value!r}, found {row.get(key)!r}")

third_place = standings.get("thirdPlaceTable", [])
third_by_group = {e.get("groupId"): e for e in third_place}
if third_by_group.get("L", {}).get("teamId") != "CRO":
    errors.append("thirdPlaceTable should use Croatia as Group L third after Panama 0-1 Croatia")
if third_by_group.get("K", {}).get("teamId") != "COD":
    errors.append("thirdPlaceTable should use Congo DR as Group K third after Colombia 1-0 Congo DR")
if third_by_group.get("L", {}).get("points") != 3:
    errors.append("thirdPlaceTable Croatia should have 3 points")
if third_by_group.get("K", {}).get("goalDifference") != -1:
    errors.append("thirdPlaceTable Congo DR should have -1 goal difference")
if not any(e.get("teamId") == "CRO" and e.get("thirdPlaceRank", 99) <= 8 for e in third_place):
    errors.append("Croatia should be in the provisional advancing third-place context")

required_files = [
    "source/text/group_result_evidence_20260624.json",
    "captures/CAPTURE_BACK_JUNE_23_GROUP_K_L_RESULTS.md",
    "cards/283_capture_june_23_group_k_l_results_card.md",
]
for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

makefile = (ROOT / "Makefile").read_text()
if "python3 tools/verify_wc2026_june_23_group_k_l_results.py" not in makefile:
    errors.append("Makefile verify target does not run June 23 K/L result verifier")

if errors:
    raise SystemExit("WC2026 June 23 Group K/L result verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 June 23 Group K/L results are captured and verified.")
