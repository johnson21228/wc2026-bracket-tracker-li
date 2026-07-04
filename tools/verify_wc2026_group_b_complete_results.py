#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
matches_path = ROOT / "site" / "data" / "current" / "group_matches.json"
standings_path = ROOT / "site" / "data" / "current" / "group_standings.json"

matches_data = json.loads(matches_path.read_text())
standings_data = json.loads(standings_path.read_text())

matches = matches_data.get("matches", matches_data) if isinstance(matches_data, dict) else matches_data
groups = standings_data.get("groups", {})
thirds = standings_data.get("thirdPlaceTable", [])

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def find_group_b_match(home_id, away_id):
    for match in matches:
        if not isinstance(match, dict):
            continue
        if match.get("groupId") == "B" and match.get("homeTeamId") == home_id and match.get("awayTeamId") == away_id:
            return match
    return None

def require_final(home_id, away_id, home_score, away_score):
    match = find_group_b_match(home_id, away_id)
    require(match is not None, f"Missing Group B match {home_id}-{away_id}")
    if not match:
        return
    require(match.get("status") == "final", f"Group B {home_id}-{away_id} should be final")
    require(match.get("homeScore") == home_score,
            f"Group B {home_id} score expected {home_score}, found {match.get('homeScore')}")
    require(match.get("awayScore") == away_score,
            f"Group B {away_id} score expected {away_score}, found {match.get('awayScore')}")

# Preserve complete Group B result evidence.
require_final("CAN", "BIH", 1, 1)
require_final("QAT", "SUI", 1, 1)
require_final("SUI", "BIH", 4, 1)
require_final("CAN", "QAT", 6, 0)
require_final("SUI", "CAN", 2, 1)
require_final("BIH", "QAT", 3, 1)

group_b = groups.get("B", {}).get("entries", [])
observed_order = [row.get("teamId") for row in group_b]
expected_order = ["SUI", "CAN", "BIH", "QAT"]
require(observed_order == expected_order,
        f"Group B order expected {expected_order}, found {observed_order}")

by_id = {row.get("teamId"): row for row in group_b}
expected_rows = {
    "SUI": {"played": 3, "wins": 2, "draws": 1, "losses": 0, "goalsFor": 7, "goalsAgainst": 3, "goalDifference": 4, "points": 7, "rank": 1},
    "CAN": {"played": 3, "wins": 1, "draws": 1, "losses": 1, "goalsFor": 8, "goalsAgainst": 3, "goalDifference": 5, "points": 4, "rank": 2},
    "BIH": {"played": 3, "wins": 1, "draws": 1, "losses": 1, "goalsFor": 5, "goalsAgainst": 6, "goalDifference": -1, "points": 4, "rank": 3},
    "QAT": {"played": 3, "wins": 0, "draws": 1, "losses": 2, "goalsFor": 2, "goalsAgainst": 10, "goalDifference": -8, "points": 1, "rank": 4},
}

for team_id, expected in expected_rows.items():
    row = by_id.get(team_id)
    require(row is not None, f"Group B standings missing {team_id}")
    if not row:
        continue
    for field, value in expected.items():
        require(row.get(field) == value,
                f"Group B {team_id} {field} expected {value}, found {row.get(field)}")

third_by_group = {row.get("groupId"): row for row in thirds}
bih = third_by_group.get("B")
require(bih is not None, "thirdPlaceTable should include Group B third-place team")
if bih:
    require(bih.get("teamId") == "BIH",
            f"thirdPlaceTable Group B team expected BIH, found {bih.get('teamId')}")
    require(bih.get("points") == 4,
            f"thirdPlaceTable BIH points expected 4, found {bih.get('points')}")
    require(isinstance(bih.get("thirdPlaceRank"), int) and bih.get("thirdPlaceRank") >= 1,
            f"thirdPlaceTable BIH should have a current third-place rank, found {bih.get('thirdPlaceRank')}")

if errors:
    print("WC2026 Group B complete result verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: Group B complete results remain protected and third-place rank reflects current completed groups.")
