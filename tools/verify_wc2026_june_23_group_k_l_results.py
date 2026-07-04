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
    "GS-2026-06-23-K3": {"homeTeamId":"POR","awayTeamId":"UZB","homeScore":5,"awayScore":0,"summary":"Portugal 5-0 Uzbekistan","currentEvidenceMatchId":"760461"},
    "GS-2026-06-23-L3": {"homeTeamId":"ENG","awayTeamId":"GHA","homeScore":0,"awayScore":0,"summary":"England 0-0 Ghana","currentEvidenceMatchId":"760458"},
    "GS-2026-06-23-L4": {"homeTeamId":"PAN","awayTeamId":"CRO","homeScore":0,"awayScore":1,"summary":"Panama 0-1 Croatia","currentEvidenceMatchId":"760460"},
    "GS-2026-06-23-K4": {"homeTeamId":"COL","awayTeamId":"COD","homeScore":1,"awayScore":0,"summary":"Colombia 1-0 Congo DR","currentEvidenceMatchId":"760459"},
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

# This verifier protects the June 23 Group K/L result capture. Current standings
# may legitimately advance after later Group K/L matches are captured, so do not
# freeze the current standings table to the June 23 intermediate snapshot.
for group_id in ["K", "L"]:
    entries = standings.get("groups", {}).get(group_id, {}).get("entries", [])
    if not entries:
        errors.append(f"Group {group_id} missing current standings entries")
    for row in entries:
        if row.get("played", 0) < 2:
            errors.append(f"Group {group_id} {row.get('teamId')} current standings regressed below the June 23 capture")

third_place = standings.get("thirdPlaceTable", [])
if not third_place:
    errors.append("thirdPlaceTable missing from current standings")

required_files = [
    "source/text/group_result_evidence_20260624.json",
    "captures/CAPTURE_BACK_JUNE_23_GROUP_K_L_RESULTS.md",
    "cards/283_capture_june_23_group_k_l_results_card.md",
]
for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"missing required file: {rel}")

makefile = (ROOT / "Makefile").read_text()
if "python3 tools/verify_wc2026_june_23_group_k_l_results.py" not in makefile:
    errors.append("Makefile verify target does not run June 23 K/L result verifier")

if errors:
    raise SystemExit("WC2026 June 23 Group K/L result verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 June 23 Group K/L results are captured and verified.")
