#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    return json.loads((ROOT / rel).read_text())

matches = read("site/data/current/group_matches.json").get("matches", [])
by_id = {str(m.get("matchId") or m.get("id")): m for m in matches}

cze = by_id.get("66456910")
if not cze:
    errors.append("missing match 66456910")
else:
    expected = {
        "status": "final",
        "homeTeamId": "CZE",
        "awayTeamId": "RSA",
        "homeScore": 1,
        "awayScore": 1,
        "summary": "Czechia 1-1 South Africa",
    }
    for key, value in expected.items():
        if cze.get(key) != value:
            errors.append(f"66456910 {key} expected {value!r}, found {cze.get(key)!r}")
    if "reuters.com" not in cze.get("resultSourceUrl", ""):
        errors.append("66456910 missing Reuters resultSourceUrl")

sui = by_id.get("66456922")
if not sui:
    errors.append("missing watchlist match 66456922")
elif sui.get("status") == "final":
    errors.append("66456922 should not be patched as final by Card 202")

standings = read("site/data/current/group_standings.json")
group_a = standings.get("groups", {}).get("A", {}).get("entries", [])
entry = {e.get("teamId"): e for e in group_a}
checks = {
    "CZE": {"played": 2, "draws": 1, "losses": 1, "goalsFor": 2, "goalsAgainst": 3, "goalDifference": -1, "points": 1},
    "RSA": {"played": 2, "draws": 1, "losses": 1, "goalsFor": 1, "goalsAgainst": 3, "goalDifference": -2, "points": 1},
}
for team, expected in checks.items():
    e = entry.get(team)
    if not e:
        errors.append(f"Group A missing {team}")
        continue
    for key, value in expected.items():
        if e.get(key) != value:
            errors.append(f"Group A {team} {key} expected {value!r}, found {e.get(key)!r}")

evidence_path = ROOT / "source/text/group_result_evidence_20260618.json"
if not evidence_path.exists():
    errors.append("missing source/text/group_result_evidence_20260618.json")
else:
    evidence = json.loads(evidence_path.read_text())
    items = evidence.get("items", [])
    if not any(str(i.get("matchId")) == "66456910" and i.get("decision") == "PATCH" for i in items):
        errors.append("evidence missing PATCH item for 66456910")
    watch = evidence.get("watchlist", [])
    if not any(str(i.get("matchId")) == "66456922" and i.get("decision") == "WATCH" for i in watch):
        errors.append("evidence missing WATCH item for 66456922")

required_files = [
    "li/world_cup/current_group_result_evidence_rule.md",
    "docs/features/current_group_result_evidence.md",
    "cards/202_capture_safe_group_result_cze_rsa_card.md",
    "capture_back/CAPTURE_BACK_SAFE_GROUP_RESULT_CZE_RSA.md",
]
for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"missing file: {rel}")

if errors:
    raise SystemExit("WC2026 safe group result verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 safe Czechia-South Africa group result patch is captured and verified.")
