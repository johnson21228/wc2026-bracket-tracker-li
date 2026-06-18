#!/usr/bin/env python3
from pathlib import Path
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
current_path = ROOT / "site/data/current/group_matches.json"
poster_path = ROOT / "site/data/group_stage_matches_from_poster.json"

missing = []
for path in [current_path, poster_path]:
    if not path.exists():
        missing.append(f"missing file: {path.relative_to(ROOT)}")

if missing:
    raise SystemExit("WC2026 complete group matches verification failed:\n- " + "\n- ".join(missing))

current = json.loads(current_path.read_text())
poster = json.loads(poster_path.read_text())
current_matches = current.get("matches", [])
poster_matches = poster.get("matches", [])

def group_of(match):
    return str(match.get("groupId") or match.get("group") or "").strip().upper()

current_counts = Counter(group_of(match) for match in current_matches)
poster_counts = Counter(group_of(match) for match in poster_matches)

for group in list("ABCDEFGHIJKL"):
    if poster_counts[group] != 6:
        missing.append(f"poster schedule group {group} has {poster_counts[group]} matches, expected 6")
    if current_counts[group] != 6:
        missing.append(f"current group_matches group {group} has {current_counts[group]} matches, expected 6")

source_text = json.dumps(current.get("source", {}), sort_keys=True).lower()
for term in ["poster", "schedule authority", "does not scrape espn"]:
    if term not in source_text:
        missing.append(f"group_matches source metadata missing term: {term}")

for match in current_matches:
    group = group_of(match)
    if group not in list("ABCDEFGHIJKL"):
        missing.append(f"match {match.get('matchId')} has invalid group {group!r}")
    for key in ["matchId", "groupId", "status", "homeTeamId", "awayTeamId"]:
        if not match.get(key):
            missing.append(f"match {match.get('matchId') or '<unknown>'} missing {key}")
    if match.get("status") in {"final", "complete", "completed"}:
        if match.get("homeScore") is None or match.get("awayScore") is None:
            missing.append(f"completed match {match.get('matchId')} missing score")
    else:
        if not (match.get("kickoffLocal") or match.get("kickoffDate") or match.get("date")):
            missing.append(f"scheduled match {match.get('matchId')} missing kickoff date/time evidence")

if missing:
    raise SystemExit("WC2026 complete group matches verification failed:\n- " + "\n- ".join(missing))

print("WC2026 complete group matches from poster verification passed.")
