# Capture Back: Scotland Flag Emoji Data

## Intent

Update Scotland/SCO flag emoji data to use the Scotland flag emoji supplied for the Bracketeering UI.

## Rule

Scotland/SCO team data should use the full Scotland flag emoji tag sequence, not a plain black-flag-only character.

## Runtime boundary

This is data/copy only. It must not change pick identity, scoring, menu eligibility, storage, or bracket geometry.

## Verification

- `python3 tools/verify_wc2026_scotland_flag_emoji_data.py`
- `make verify`
