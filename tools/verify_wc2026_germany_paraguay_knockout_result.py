#!/usr/bin/env python3
import json
import sys
from pathlib import Path

errors = []

truth = json.loads(Path("site/data/current/official_truth.json").read_text())
results = json.loads(Path("site/data/official_knockout_results.json").read_text())

non_r32_truth = [
    slot_id for slot_id in truth.get("picksBySlot", {})
    if "-R32-" not in slot_id
]
if non_r32_truth:
    errors.append(f"official_truth.json must remain R32-only; found {non_r32_truth}")

matches = results.get("matches", [])
ids = [match.get("resultId") for match in matches]

if ids.count("r32-ger-par-2026-06-29") != 1:
    errors.append("expected exactly one GER/PAR knockout result")

match = next((m for m in matches if m.get("resultId") == "r32-ger-par-2026-06-29"), None)
if match:
    expected = {
        "round": "R32",
        "status": "final",
        "resultType": "penalties",
        "winnerTeamId": "PAR",
        "winnerTeamName": "Paraguay",
        "siteWinnerSlotId": "L-R16-01",
        "resultLabel": "Germany 1–1 Paraguay; Paraguay advances 4–3 on penalties",
    }
    for key, value in expected.items():
        if match.get(key) != value:
            errors.append(f"GER/PAR {key} expected {value!r}, found {match.get(key)!r}")

    if match.get("scoreByTeamId") != {"GER": 1, "PAR": 1}:
        errors.append("GER/PAR scoreByTeamId should be tied 1-1")

    if match.get("penaltyScoreByTeamId") != {"GER": 3, "PAR": 4}:
        errors.append("GER/PAR penaltyScoreByTeamId should be GER 3, PAR 4")

    if match.get("siteSlotPair") != ["L-R32-01", "L-R32-02"]:
        errors.append("GER/PAR siteSlotPair should be L-R32-01/L-R32-02")

    teams = {team.get("teamId"): team for team in match.get("teams", [])}
    if teams.get("GER", {}).get("siteSlotId") != "L-R32-01":
        errors.append("GER should be recorded at L-R32-01")
    if teams.get("PAR", {}).get("siteSlotId") != "L-R32-02":
        errors.append("PAR should be recorded at L-R32-02")
    if teams.get("GER", {}).get("penaltyScore") != 3:
        errors.append("GER penalty score should be 3")
    if teams.get("PAR", {}).get("penaltyScore") != 4:
        errors.append("PAR penalty score should be 4")

protected_ids = {
    "r32-rsa-can-2026-06-28",
    "r32-bra-jpn-2026-06-29",
    "r32-ger-par-2026-06-29",
}
missing = protected_ids - set(ids)
if missing:
    errors.append(f"missing protected knockout result ids: {sorted(missing)}")

if errors:
    print("WC2026 Germany-Paraguay knockout result verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: Germany-Paraguay penalty result is append-only, Paraguay advances, and official_truth remains R32-only.")
