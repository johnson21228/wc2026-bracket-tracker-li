#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

matches = json.loads((ROOT / "site/data/current/group_matches.json").read_text())
standings = json.loads((ROOT / "site/data/current/group_standings.json").read_text())
highlights = json.loads((ROOT / "site/data/current/match_highlights.json").read_text())

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def find_match(espn_id, fallback_id):
    for match in matches["matches"]:
        if match.get("espnMatchId") == espn_id or match.get("matchId") in {espn_id, fallback_id}:
            return match
    return None

expected_matches = {
    "66457010": ("GS-2026-06-22-I4", "France 3-0 Iraq", 3, 0, "https://youtu.be/Mo7aY61WF9I"),
    "66457012": ("GS-2026-06-22-I3", "Norway 3-2 Senegal", 3, 2, "https://youtu.be/vcgzGgM4uJg"),
    "66457022": ("GS-2026-06-22-J3", "Argentina 2-0 Austria", 2, 0, "https://youtu.be/JakdhltyECE"),
    "66457024": ("GS-2026-06-22-J4", "Jordan 1-2 Algeria", 1, 2, "https://youtu.be/qq3eMBEUbzY"),
}

for espn_id, (fallback_id, summary, home_score, away_score, url) in expected_matches.items():
    match = find_match(espn_id, fallback_id)
    require(match is not None, f"missing match row for {summary}")
    if match:
        require(match.get("status") == "final", f"{summary} must be final")
        require(match.get("homeScore") == home_score and match.get("awayScore") == away_score, f"{summary} score mismatch")
        require(match.get("summary") == summary, f"{summary} summary mismatch")
        require(match.get("resultSourceUrl") == url, f"{summary} result URL mismatch")
    highlight = highlights["highlights"].get(espn_id)
    require(highlight is not None, f"missing highlight for {summary}")
    if highlight:
        require(highlight.get("url") == url, f"{summary} highlight URL mismatch")
        require(highlight.get("verificationMode") == "user-provided-url-and-score-interview", f"{summary} highlight verification mode mismatch")

def by_team(group_id):
    return {entry["teamId"]: entry for entry in standings["groups"][group_id]["entries"]}

group_i = by_team("I")
group_j = by_team("J")

require(group_i["FRA"]["points"] == 6 and group_i["FRA"]["rank"] == 1 and group_i["FRA"]["goalDifference"] == 5, "Group I France standings mismatch")
require(group_i["NOR"]["points"] == 6 and group_i["NOR"]["rank"] == 2 and group_i["NOR"]["goalDifference"] == 4, "Group I Norway standings mismatch")
require(group_i["SEN"]["points"] == 0 and group_i["SEN"]["rank"] == 3 and group_i["SEN"]["goalDifference"] == -3, "Group I Senegal standings mismatch")
require(group_i["IRQ"]["points"] == 0 and group_i["IRQ"]["rank"] == 4 and group_i["IRQ"]["goalDifference"] == -6, "Group I Iraq standings mismatch")

require(group_j["ARG"]["points"] == 6 and group_j["ARG"]["rank"] == 1 and group_j["ARG"]["goalDifference"] == 5, "Group J Argentina standings mismatch")
require(group_j["AUT"]["points"] == 3 and group_j["AUT"]["rank"] == 2 and group_j["AUT"]["goalDifference"] == 0, "Group J Austria standings mismatch")
require(group_j["DZA"]["points"] == 3 and group_j["DZA"]["rank"] == 3 and group_j["DZA"]["goalDifference"] == -2, "Group J Algeria standings mismatch")
require(group_j["JOR"]["points"] == 0 and group_j["JOR"]["rank"] == 4 and group_j["JOR"]["goalDifference"] == -3, "Group J Jordan standings mismatch")

thirds = standings["thirdPlaceTable"]
require(any(row.get("teamId") == "DZA" and row.get("groupId") == "J" and row.get("points") == 3 for row in thirds), "third-place table must include Algeria from Group J")
require(any(row.get("teamId") == "SEN" and row.get("groupId") == "I" and row.get("points") == 0 for row in thirds), "third-place table must include Senegal from Group I")
require(not any(row.get("teamId") == "JOR" and row.get("groupId") == "J" for row in thirds), "third-place table must not keep Jordan as Group J third place")

if errors:
    print("June 22 Group I/J verification failed: " + "; ".join(errors))
    raise SystemExit(1)

print("OK: WC2026 June 22 Group I/J results, highlights, standings, and third-place table are captured.")
