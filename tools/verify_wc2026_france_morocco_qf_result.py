#!/usr/bin/env python3
from pathlib import Path
import json
import sys

errors = []

data = json.loads(Path("site/data/official_knockout_results.json").read_text())

if isinstance(data, list):
    results = data
elif isinstance(data, dict):
    results = None
    for key in ["results", "matches", "officialKnockoutResults", "knockoutResults"]:
        if isinstance(data.get(key), list):
            results = data[key]
            break
    if results is None:
        errors.append("Could not find knockout result list")
        results = []
else:
    errors.append("Unexpected official_knockout_results.json shape")
    results = []

matches = [r for r in results if r.get("resultId") == "qf-fra-mar-2026-07-09"]

if len(matches) != 1:
    errors.append(f"expected exactly one qf-fra-mar-2026-07-09 result row, found {len(matches)}")
else:
    r = matches[0]
    expected = {
        "round": "Quarterfinal",
        "homeTeamId": "FRA",
        "homeTeamName": "France",
        "homeScore": 2,
        "awayTeamId": "MAR",
        "awayTeamName": "Morocco",
        "awayScore": 0,
        "winnerTeamId": "FRA",
        "winnerTeamName": "France",
        "resultLabel": "France 2–0 Morocco",
        "resultText": "France 2–0 Morocco",
        "espnGameId": "53452525",
    }
    for key, value in expected.items():
        if r.get(key) != value:
            errors.append(f"{key} must be {value!r}; found {r.get(key)!r}")

ids = {}
for r in results:
    rid = r.get("resultId")
    if rid:
        ids.setdefault(rid, 0)
        ids[rid] += 1

dupes = sorted(rid for rid, count in ids.items() if count > 1)
if dupes:
    errors.append("duplicate resultId rows remain: " + ", ".join(dupes))

bad_copies = [
    r for r in results
    if r.get("resultId") == "r16-fra-par-2026-07-04"
    and r.get("round") == "Quarterfinal"
]
if bad_copies:
    errors.append("bad copied France-Paraguay resultId remains on a Quarterfinal row")

official_truth = Path("site/data/official_truth.json")
if official_truth.exists() and "53452525" in official_truth.read_text():
    errors.append("official_truth.json must remain R32-only; QF result belongs in official_knockout_results.json")

makefile = Path("Makefile").read_text()
if "python3 tools/verify_wc2026_france_morocco_qf_result.py" not in makefile:
    errors.append("Makefile verify target must include France/Morocco QF verifier")

if errors:
    print("France/Morocco QF result verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: France-Morocco QF result is qf-fra-mar-2026-07-09, FRA 2-0 MAR, France advances, and official_truth remains R32-only.")
