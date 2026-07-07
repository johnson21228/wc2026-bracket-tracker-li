#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
results = json.loads((ROOT / "site/data/official_knockout_results.json").read_text())
errors = []

expected = {
    "resultId": "r16-arg-egy-2026-07-07",
    "matchId": "53452521",
    "round": "Round of 16",
    "status": "final",
    "resultType": "regulation",
    "siteWinnerSlotId": "R-QF-03",
    "siteSlotPair": ["R-R16-05", "R-R16-06"],
    "homeTeamId": "ARG",
    "homeScore": 3,
    "awayTeamId": "EGY",
    "awayScore": 2,
    "winnerTeamId": "ARG",
    "resultLabel": "Argentina 3–2 Egypt",
}

matches = results.get("matches", [])
rows = [match for match in matches if match.get("resultId") == expected["resultId"]]
if len(rows) != 1:
    errors.append(f"expected exactly one {expected['resultId']} result row; found {len(rows)}")
else:
    row = rows[0]
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"{expected['resultId']} expected {key}={value!r}, found {row.get(key)!r}")
    if row.get("homeScore") <= row.get("awayScore"):
        errors.append("Argentina must be the regulation winner for ARG 3–2 EGY.")

capture_path = ROOT / "captures/CAPTURE_BACK_ARGENTINA_EGYPT_R16_RESULT.md"
if not capture_path.exists():
    errors.append("missing capture: CAPTURE_BACK_ARGENTINA_EGYPT_R16_RESULT.md")
else:
    capture = capture_path.read_text()
    for token in ["r16-arg-egy-2026-07-07", "Argentina 3–2 Egypt", "R-QF-03"]:
        if token not in capture:
            errors.append(f"capture missing token: {token}")

if errors:
    print("Argentina/Egypt R16 result verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Argentina 3–2 Egypt R16 result is captured as an official knockout result.")
