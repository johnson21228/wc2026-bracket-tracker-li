#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
results = json.loads((ROOT / "site/data/official_knockout_results.json").read_text())
errors = []

expected = {
    "r16-fra-par-2026-07-04": {
        "winnerTeamId": "FRA",
        "siteWinnerSlotId": "L-QF-01",
        "siteSlotPair": ["L-R16-01", "L-R16-02"],
        "extendedHighlightsUrl": "https://youtu.be/bQ5Z4Q8VQ8w",
    },
    "r16-can-mor-2026-07-04": {
        "winnerTeamId": "MAR",
        "siteWinnerSlotId": "L-QF-02",
        "siteSlotPair": ["L-R16-03", "L-R16-04"],
        "extendedHighlightsUrl": "https://youtu.be/QLFucR6SGr4",
    },
}

by_id = {match.get("resultId"): match for match in results.get("matches", [])}

for result_id, fields in expected.items():
    match = by_id.get(result_id)
    if not match:
        errors.append(f"missing result record: {result_id}")
        continue
    for key, value in fields.items():
        if match.get(key) != value:
            errors.append(f"{result_id} expected {key}={value!r}, found {match.get(key)!r}")
    if "highlightUrl" in match and match.get("highlightUrl") != match.get("extendedHighlightsUrl"):
        errors.append(f"{result_id} must not have conflicting highlightUrl and extendedHighlightsUrl")

capture = (ROOT / "captures/CAPTURE_BACK_JULY_04_R16_EXTENDED_HIGHLIGHTS.md").read_text()
for token in [
    "https://youtu.be/bQ5Z4Q8VQ8w",
    "https://youtu.be/QLFucR6SGr4",
    "r16-fra-par-2026-07-04",
    "r16-can-mor-2026-07-04",
]:
    if token not in capture:
        errors.append(f"capture missing token: {token}")

if errors:
    print("July 4 R16 extended highlights verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: July 4 R16 extended highlights are captured on the official knockout result records.")
