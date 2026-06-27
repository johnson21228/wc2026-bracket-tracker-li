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

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

# This verifier originally protected the Czechia 1-1 South Africa patch.
# It now protects that historical final while allowing later Group A matches
# to advance standings beyond the old 2-played interim state.
target = None
for match in matches:
    if not isinstance(match, dict):
        continue
    ids = {match.get("homeTeamId"), match.get("awayTeamId")}
    if match.get("groupId") == "A" and ids == {"CZE", "RSA"}:
        target = match
        break

require(target is not None, "Group A Czechia-South Africa match not found")

if target:
    require(target.get("status") == "final", "Czechia-South Africa should remain final")
    require(target.get("homeTeamId") == "CZE", "Czechia should remain home team for protected match")
    require(target.get("awayTeamId") == "RSA", "South Africa should remain away team for protected match")
    require(target.get("homeScore") == 1, f"Czechia score expected 1, found {target.get('homeScore')}")
    require(target.get("awayScore") == 1, f"South Africa score expected 1, found {target.get('awayScore')}")

group_a = groups.get("A", {}).get("entries", [])
by_id = {row.get("teamId"): row for row in group_a}

require([row.get("teamId") for row in group_a] == ["MEX", "RSA", "KOR", "CZE"],
        f"Group A completed order should be ['MEX', 'RSA', 'KOR', 'CZE'], found {[row.get('teamId') for row in group_a]}")

expected = {
    "MEX": {"played": 3, "points": 9, "goalDifference": 6},
    "RSA": {"played": 3, "points": 4, "goalDifference": -1},
    "KOR": {"played": 3, "points": 3, "goalDifference": -1},
    "CZE": {"played": 3, "points": 1, "goalDifference": -4},
}

for team_id, expected_fields in expected.items():
    row = by_id.get(team_id)
    require(row is not None, f"Group A standings missing {team_id}")
    if not row:
        continue
    for field, value in expected_fields.items():
        require(row.get(field) == value, f"Group A {team_id} {field} expected {value}, found {row.get(field)}")

if errors:
    print("WC2026 safe group result verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: Czechia-South Africa result remains protected and Group A completed standings are current.")
