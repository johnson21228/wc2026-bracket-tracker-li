#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
matches_path = ROOT / "site" / "data" / "current" / "group_matches.json"
standings_path = ROOT / "site" / "data" / "current" / "group_standings.json"
highlights_path = ROOT / "site" / "data" / "current" / "match_highlights.json"

matches_data = json.loads(matches_path.read_text())
standings_data = json.loads(standings_path.read_text())

matches = matches_data.get("matches", matches_data) if isinstance(matches_data, dict) else matches_data
groups = standings_data.get("groups", {})
thirds = standings_data.get("thirdPlaceTable", [])

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def by_team(group_id):
    return {row.get("teamId"): row for row in groups.get(group_id, {}).get("entries", [])}

def require_group(group_id, expected_order, expected_rows):
    entries = groups.get(group_id, {}).get("entries", [])
    observed = [row.get("teamId") for row in entries]
    require(observed == expected_order, f"Group {group_id} order expected {expected_order}, found {observed}")

    rows = by_team(group_id)
    for team_id, expected in expected_rows.items():
        row = rows.get(team_id)
        require(row is not None, f"Group {group_id} missing {team_id}")
        if not row:
            continue
        for field, value in expected.items():
            require(row.get(field) == value,
                    f"Group {group_id} {team_id} {field} expected {value}, found {row.get(field)}")

# Group I is now complete after Norway-France and Senegal-Iraq.
require_group("I", ["FRA", "NOR", "SEN", "IRQ"], {
    "FRA": {"played": 3, "wins": 3, "draws": 0, "losses": 0, "goalsFor": 10, "goalsAgainst": 2, "goalDifference": 8, "points": 9, "rank": 1},
    "NOR": {"played": 3, "wins": 2, "draws": 0, "losses": 1, "goalsFor": 8, "goalsAgainst": 7, "goalDifference": 1, "points": 6, "rank": 2},
    "SEN": {"played": 3, "wins": 1, "draws": 0, "losses": 2, "goalsFor": 8, "goalsAgainst": 6, "goalDifference": 2, "points": 3, "rank": 3},
    "IRQ": {"played": 3, "wins": 0, "draws": 0, "losses": 3, "goalsFor": 1, "goalsAgainst": 12, "goalDifference": -11, "points": 0, "rank": 4},
})

# Group J is now complete after the June 27 final matchday.
require_group("J", ["ARG", "AUT", "DZA", "JOR"], {
    "ARG": {"played": 3, "wins": 3, "draws": 0, "losses": 0, "goalsFor": 8, "goalsAgainst": 1, "goalDifference": 7, "points": 9, "rank": 1},
    "AUT": {"played": 3, "wins": 1, "draws": 1, "losses": 1, "goalsFor": 6, "goalsAgainst": 6, "goalDifference": 0, "points": 4, "rank": 2},
    "DZA": {"played": 3, "wins": 1, "draws": 1, "losses": 1, "goalsFor": 5, "goalsAgainst": 7, "goalDifference": -2, "points": 4, "rank": 3},
    "JOR": {"played": 3, "wins": 0, "draws": 0, "losses": 3, "goalsFor": 3, "goalsAgainst": 8, "goalDifference": -5, "points": 0, "rank": 4},
})

third_by_group = {row.get("groupId"): row for row in thirds}
require(third_by_group.get("I", {}).get("teamId") == "SEN",
        "third-place table must include Senegal from Group I")
require(third_by_group.get("I", {}).get("points") == 3,
        "third-place table must include Senegal on 3 points from completed Group I")

require(highlights_path.exists(), "match_highlights.json should exist")

if errors:
    print("June 22 Group I/J verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: June 22 Group I/J evidence remains protected and Group J now reflects final completed standings.")
