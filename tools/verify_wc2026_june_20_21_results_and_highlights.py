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
by_local = {str(m.get("matchId")): m for m in matches}

expected_matches = {
    "GS-2026-06-20-F3": {"espnMatchId": "66456972", "homeTeamId": "NED", "awayTeamId": "SWE", "homeScore": 5, "awayScore": 1, "summary": "Netherlands 5-1 Sweden"},
    "GS-2026-06-20-E3": {"espnMatchId": "66457074", "homeTeamId": "GER", "awayTeamId": "CIV", "homeScore": 2, "awayScore": 1, "summary": "Germany 2-1 Côte d’Ivoire"},
    "GS-2026-06-20-E4": {"espnMatchId": "66457076", "homeTeamId": "ECU", "awayTeamId": "CUW", "homeScore": 0, "awayScore": 0, "summary": "Ecuador 0-0 Curaçao"},
    "GS-2026-06-20-F4": {"espnMatchId": "66456974", "homeTeamId": "TUN", "awayTeamId": "JPN", "homeScore": 0, "awayScore": 4, "summary": "Tunisia 0-4 Japan"},
}

for local_id, expected in expected_matches.items():
    row = by_local.get(local_id)
    if not row:
        errors.append(f"missing match row {local_id}")
        continue
    if row.get("status") != "final":
        errors.append(f"{local_id} status expected final, found {row.get('status')!r}")
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"{local_id} {key} expected {value!r}, found {row.get(key)!r}")
    if row.get("resultSource") != "user-provided-score-and-highlight-interview":
        errors.append(f"{local_id} missing user-provided resultSource")
    if not str(row.get("resultSourceUrl", "")).startswith("https://"):
        errors.append(f"{local_id} missing https resultSourceUrl")

highlights = read("site/data/current/match_highlights.json").get("highlights", {})
expected_highlights = {
    "66456972": ("Netherlands 5-1 Sweden", "https://youtu.be/IRllRLrG7Sg"),
    "66457074": ("Germany 2-1 Côte d’Ivoire", "https://www.youtube.com/watch?v=xHtIzadh4Lg&pp=ygUHZ2VybWFueQ%3D%3D"),
    "66457076": ("Ecuador 0-0 Curaçao", "https://youtu.be/_JQLeADlzXM"),
    "66456974": ("Tunisia 0-4 Japan", "https://youtu.be/ATmlGGfCyBA"),
}
for match_id, (evidence, url) in expected_highlights.items():
    entry = highlights.get(match_id)
    if not isinstance(entry, dict):
        errors.append(f"missing highlight entry {match_id}")
        continue
    if entry.get("url") != url:
        errors.append(f"{match_id} highlight URL expected {url!r}, found {entry.get('url')!r}")
    if entry.get("matchEvidence") != evidence:
        errors.append(f"{match_id} matchEvidence expected {evidence!r}, found {entry.get('matchEvidence')!r}")
    if entry.get("verificationMode") != "user-provided-url":
        errors.append(f"{match_id} verificationMode should be user-provided-url")

standings = read("site/data/current/group_standings.json")
checks = {
    "E": {
        "GER": {"played": 2, "wins": 2, "points": 6, "goalsFor": 9, "goalsAgainst": 2, "goalDifference": 7, "rank": 1},
        "CIV": {"played": 2, "wins": 1, "losses": 1, "points": 3, "goalsFor": 2, "goalsAgainst": 2, "goalDifference": 0, "rank": 2},
        "ECU": {"played": 2, "draws": 1, "losses": 1, "points": 1, "goalsFor": 0, "goalsAgainst": 1, "goalDifference": -1, "rank": 3},
        "CUW": {"played": 2, "draws": 1, "losses": 1, "points": 1, "goalsFor": 1, "goalsAgainst": 7, "goalDifference": -6, "rank": 4},
    },
    "F": {
        "NED": {"played": 2, "wins": 1, "draws": 1, "points": 4, "goalsFor": 7, "goalsAgainst": 3, "goalDifference": 4, "rank": 1},
        "JPN": {"played": 2, "wins": 1, "draws": 1, "points": 4, "goalsFor": 6, "goalsAgainst": 2, "goalDifference": 4, "rank": 2},
        "SWE": {"played": 2, "wins": 1, "losses": 1, "points": 3, "goalsFor": 6, "goalsAgainst": 6, "goalDifference": 0, "rank": 3},
        "TUN": {"played": 2, "losses": 2, "points": 0, "goalsFor": 1, "goalsAgainst": 9, "goalDifference": -8, "rank": 4},
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
third_by_team = {e.get("teamId"): e for e in third_place}
if third_by_team.get("SWE", {}).get("points") != 3:
    errors.append("thirdPlaceTable should include Sweden on 3 points after Netherlands 5-1 Sweden")
if third_by_team.get("ECU", {}).get("points") != 1:
    errors.append("thirdPlaceTable should include Ecuador on 1 point after Ecuador 0-0 Curaçao")

required_files = [
    "source/text/group_result_evidence_20260621.json",
    "captures/CAPTURE_BACK_JUNE_20_21_RESULTS_AND_HIGHLIGHTS.md",
    "cards/235_capture_june_20_21_results_and_highlights_card.md",
]
for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

makefile = (ROOT / "Makefile").read_text()
if "python3 tools/verify_wc2026_june_20_21_results_and_highlights.py" not in makefile:
    errors.append("Makefile verify target does not run June 20/21 result verifier")

if errors:
    raise SystemExit("WC2026 June 20/21 result/highlight verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 June 20/21 Group E/F results and highlights are captured and verified.")
