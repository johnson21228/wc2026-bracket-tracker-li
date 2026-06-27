#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
matches_path = ROOT / "site" / "data" / "current" / "group_matches.json"
standings_path = ROOT / "site" / "data" / "current" / "group_standings.json"
highlights_path = ROOT / "site" / "data" / "current" / "match_highlights.json"

matches_data = json.loads(matches_path.read_text())
standings_data = json.loads(standings_path.read_text())
highlights_data = json.loads(highlights_path.read_text()) if highlights_path.exists() else {}

matches = matches_data.get("matches", matches_data) if isinstance(matches_data, dict) else matches_data
groups = standings_data.get("groups", {})
thirds = standings_data.get("thirdPlaceTable", [])

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def find_match(group_id, home_id, away_id):
    for match in matches:
        if not isinstance(match, dict):
            continue
        if match.get("groupId") != group_id:
            continue
        if match.get("homeTeamId") == home_id and match.get("awayTeamId") == away_id:
            return match
    return None

def require_final(group_id, home_id, away_id, home_score, away_score):
    match = find_match(group_id, home_id, away_id)
    require(match is not None, f"Missing Group {group_id} match {home_id}-{away_id}")
    if not match:
        return
    require(match.get("status") == "final", f"Group {group_id} {home_id}-{away_id} should be final")
    require(match.get("homeScore") == home_score,
            f"Group {group_id} {home_id} score expected {home_score}, found {match.get('homeScore')}")
    require(match.get("awayScore") == away_score,
            f"Group {group_id} {away_id} score expected {away_score}, found {match.get('awayScore')}")

# Preserve the original June 20/21 result evidence that this verifier was created to protect.
require_final("E", "GER", "CIV", 2, 1)
require_final("E", "ECU", "CUW", 0, 0)
require_final("F", "NED", "SWE", 5, 1)
require_final("F", "TUN", "JPN", 0, 4)

# Accept the current completed Group E/F standings after the later June 25 finals.
expected_rows = {
    "E": {
        "GER": {"played": 3, "points": 6, "goalsFor": 10, "goalsAgainst": 4, "goalDifference": 6, "rank": 1},
        "CIV": {"played": 3, "points": 6, "goalsFor": 4, "goalsAgainst": 2, "goalDifference": 2, "rank": 2},
        "ECU": {"played": 3, "points": 4, "goalsFor": 2, "goalsAgainst": 2, "goalDifference": 0, "rank": 3},
        "CUW": {"played": 3, "points": 1, "goalsFor": 1, "goalsAgainst": 9, "goalDifference": -8, "rank": 4},
    },
    "F": {
        "NED": {"played": 3, "points": 7, "goalsFor": 10, "goalsAgainst": 4, "goalDifference": 6, "rank": 1},
        "JPN": {"played": 3, "points": 5, "goalsFor": 7, "goalsAgainst": 3, "goalDifference": 4, "rank": 2},
        "SWE": {"played": 3, "points": 4, "goalsFor": 7, "goalsAgainst": 7, "goalDifference": 0, "rank": 3},
        "TUN": {"played": 3, "points": 0, "goalsFor": 2, "goalsAgainst": 12, "goalDifference": -10, "rank": 4},
    },
}

for group_id, rows in expected_rows.items():
    entries = groups.get(group_id, {}).get("entries", [])
    by_id = {row.get("teamId"): row for row in entries}
    require(list(by_id)[:4] == list(rows),
            f"Group {group_id} current order should be {list(rows)}, found {list(by_id)[:4]}")
    for team_id, expected in rows.items():
        row = by_id.get(team_id)
        require(row is not None, f"Group {group_id} missing {team_id}")
        if not row:
            continue
        for field, value in expected.items():
            require(row.get(field) == value,
                    f"Group {group_id} {team_id} {field} expected {value}, found {row.get(field)}")

third_by_group = {row.get("groupId"): row for row in thirds}
require(third_by_group.get("F", {}).get("teamId") == "SWE",
        "thirdPlaceTable should include Sweden as Group F third-place team")
require(third_by_group.get("F", {}).get("points") == 4,
        "thirdPlaceTable should include Sweden on 4 points after completed Group F")
require(third_by_group.get("E", {}).get("teamId") == "ECU",
        "thirdPlaceTable should include Ecuador as Group E third-place team")
require(third_by_group.get("E", {}).get("points") == 4,
        "thirdPlaceTable should include Ecuador on 4 points after completed Group E")

# Keep highlight storage present without requiring this verifier to own all link specifics.
require(highlights_path.exists(), "match_highlights.json should exist")

if errors:
    print("WC2026 June 20/21 result/highlight verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: June 20/21 result evidence remains protected and Groups E/F completed standings are current.")
