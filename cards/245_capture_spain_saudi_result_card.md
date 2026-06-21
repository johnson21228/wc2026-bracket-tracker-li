# Card 245: Capture Spain 4-0 Saudi Arabia Result

## Goal

Capture the user-provided Spain 4-0 Saudi Arabia Group H final result and highlight link.

## Scope

- Patch the Group H match result.
- Store the YouTube highlight link.
- Recompute Group H standings from checked-in final match data.
- Preserve runtime rule: checked-in JSON only, no external scraping.
- Capture source evidence.

## Verification

Run:

- `python3 tools/verify_wc2026_spain_saudi_result_and_highlight.py`
- `make verify`
