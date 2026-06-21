# Capture Back: Spain 4-0 Saudi Arabia Result and Highlight

## Intent

Capture the completed Group H result supplied by the user and attach the provided highlight link.

## Result captured

- Spain 4 – 0 Saudi Arabia
- Group H
- Match date: 2026-06-21
- ESPN match ID: 66456998
- Poster match ID: GS-2026-06-21-H4
- Highlight: https://youtu.be/w453UjgtQw4

## Evidence

The user provided:

- an ESPN final-score screenshot showing FT Spain 4-0 Saudi Arabia
- a YouTube highlight URL

## Files updated

- `site/data/current/group_matches.json`
- `site/data/current/match_highlights.json`
- `site/data/current/group_standings.json`
- `source/text/group_result_evidence_20260621_spain_saudi.json`

## Verification

Run:

- `python3 tools/verify_wc2026_spain_saudi_result_and_highlight.py`
- `make verify`
