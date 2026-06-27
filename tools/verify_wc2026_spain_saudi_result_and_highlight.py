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

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def find_match(group_id, home_id, away_id):
    for match in matches:
        if not isinstance(match, dict):
            continue
        if match.get("groupId") == group_id and match.get("homeTeamId") == home_id and match.get("awayTeamId") == away_id:
            return match
    return None

# Preserve the original Spain 4-0 Saudi Arabia evidence this verifier was created for.
spain_saudi = find_match("H", "ESP", "KSA")
require(spain_saudi is not None, "Missing Group H Spain-Saudi Arabia match")

if spain_saudi:
    require(spain_saudi.get("status") == "final", "Spain-Saudi Arabia should remain final")
    require(spain_saudi.get("homeScore") == 4, f"Spain score expected 4, found {spain_saudi.get('homeScore')}")
    require(spain_saudi.get("awayScore") == 0, f"Saudi Arabia score expected 0, found {spain_saudi.get('awayScore')}")

# Accept completed Group H standings after Cabo Verde 0-0 Saudi Arabia and Uruguay 0-1 Spain.
group_h = groups.get("H", {}).get("entries", [])
by_id = {row.get("teamId"): row for row in group_h}

expected_order = ["ESP", "CPV", "URU", "KSA"]
require([row.get("teamId") for row in group_h] == expected_order,
        f"Group H current order should be {expected_order}, found {[row.get('teamId') for row in group_h]}")

expected_rows = {
    "ESP": {"played": 3, "wins": 2, "draws": 1, "losses": 0, "goalsFor": 5, "goalsAgainst": 0, "goalDifference": 5, "points": 7, "rank": 1},
    "CPV": {"played": 3, "wins": 0, "draws": 3, "losses": 0, "goalsFor": 2, "goalsAgainst": 2, "goalDifference": 0, "points": 3, "rank": 2},
    "URU": {"played": 3, "wins": 0, "draws": 2, "losses": 1, "goalsFor": 3, "goalsAgainst": 4, "goalDifference": -1, "points": 2, "rank": 3},
    "KSA": {"played": 3, "wins": 0, "draws": 2, "losses": 1, "goalsFor": 1, "goalsAgainst": 5, "goalDifference": -4, "points": 2, "rank": 4},
}

for team_id, expected in expected_rows.items():
    row = by_id.get(team_id)
    require(row is not None, f"Group H standings missing {team_id}")
    if not row:
        continue
    for field, value in expected.items():
        require(row.get(field) == value,
                f"Group H {team_id} {field} expected {value}, found {row.get(field)}")

require(highlights_path.exists(), "match_highlights.json should exist")

if errors:
    print("WC2026 Spain-Saudi result verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: Spain-Saudi result remains protected and Group H completed standings are current.")
