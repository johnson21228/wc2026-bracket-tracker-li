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
    "GS-2026-06-27-J5": {"homeTeamId":"ALG","awayTeamId":"AUT","homeScore":3,"awayScore":3,"summary":"Algeria 3-3 Austria"},
    "GS-2026-06-27-J6": {"homeTeamId":"JOR","awayTeamId":"ARG","homeScore":1,"awayScore":3,"summary":"Jordan 1-3 Argentina"},
    "GS-2026-06-27-K5": {"homeTeamId":"COL","awayTeamId":"POR","homeScore":0,"awayScore":0,"summary":"Colombia 0-0 Portugal"},
    "GS-2026-06-27-K6": {"homeTeamId":"COD","awayTeamId":"UZB","homeScore":3,"awayScore":1,"summary":"Congo DR 3-1 Uzbekistan"},
    "GS-2026-06-27-L5": {"homeTeamId":"PAN","awayTeamId":"ENG","homeScore":0,"awayScore":2,"summary":"Panama 0-2 England"},
    "GS-2026-06-27-L6": {"homeTeamId":"CRO","awayTeamId":"GHA","homeScore":2,"awayScore":1,"summary":"Croatia 2-1 Ghana"},
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
    "J": {
        "ARG": {"played":3,"wins":3,"points":9,"goalsFor":8,"goalsAgainst":1,"goalDifference":7,"rank":1},
        "AUT": {"played":3,"wins":1,"draws":1,"points":4,"goalsFor":6,"goalsAgainst":6,"goalDifference":0,"rank":2},
        "DZA": {"played":3,"wins":1,"draws":1,"points":4,"goalsFor":5,"goalsAgainst":7,"goalDifference":-2,"rank":3},
        "JOR": {"played":3,"losses":3,"points":0,"goalsFor":3,"goalsAgainst":8,"goalDifference":-5,"rank":4},
    },
    "K": {
        "COL": {"played":3,"wins":2,"draws":1,"points":7,"goalsFor":4,"goalsAgainst":1,"goalDifference":3,"rank":1},
        "POR": {"played":3,"wins":1,"draws":2,"points":5,"goalsFor":6,"goalsAgainst":1,"goalDifference":5,"rank":2},
        "COD": {"played":3,"wins":1,"draws":1,"points":4,"goalsFor":4,"goalsAgainst":3,"goalDifference":1,"rank":3},
        "UZB": {"played":3,"losses":3,"points":0,"goalsFor":2,"goalsAgainst":11,"goalDifference":-9,"rank":4},
    },
    "L": {
        "ENG": {"played":3,"wins":2,"draws":1,"points":7,"goalsFor":6,"goalsAgainst":2,"goalDifference":4,"rank":1},
        "CRO": {"played":3,"wins":2,"losses":1,"points":6,"goalsFor":5,"goalsAgainst":5,"goalDifference":0,"rank":2},
        "GHA": {"played":3,"wins":1,"draws":1,"losses":1,"points":4,"goalsFor":2,"goalsAgainst":2,"goalDifference":0,"rank":3},
        "PAN": {"played":3,"losses":3,"points":0,"goalsFor":0,"goalsAgainst":4,"goalDifference":-4,"rank":4},
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

third = standings.get("thirdPlaceTable", [])
third_by_group = {e.get("groupId"): e for e in third}
for group_id, team_id in {"J":"DZA", "K":"COD", "L":"GHA"}.items():
    row = third_by_group.get(group_id)
    if not row or row.get("teamId") != team_id:
        errors.append(f"thirdPlaceTable should use {team_id} as Group {group_id} third-place team")
    elif row.get("qualificationContext") != "third-place-advancing-context":
        errors.append(f"thirdPlaceTable {team_id} should be marked advancing-context")

required_files = [
    "source/text/group_result_evidence_20260628.json",
    "captures/CAPTURE_BACK_JUNE_27_FINAL_GROUP_RESULTS.md",
    "cards/300_june_27_final_group_results_card.md",
]
for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

makefile = (ROOT / "Makefile").read_text()
if "python3 tools/verify_wc2026_june_27_final_group_results.py" not in makefile:
    errors.append("Makefile verify target does not run June 27 final group result verifier")

if errors:
    raise SystemExit("WC2026 June 27 final group result verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 June 27 final Group J/K/L results are captured and verified.")
