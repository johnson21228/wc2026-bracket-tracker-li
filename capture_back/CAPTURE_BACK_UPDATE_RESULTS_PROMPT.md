# Capture Back: UPDATE RESULTS Prompt

## Change
Added a reusable prompt for the command phrase `UPDATE RESULTS`.

## Why
World Cup result updates happen during live match windows. The prompt must distinguish confirmed finals from live/in-progress scores before patching repo data.

## Files
- `prompts/update_results_from_web.md`
- `docs/workflows/update_results_from_web.md`
- `li/workflow/update_results_from_web_protocol.md`
- `cards/202_capture_update_results_prompt_card.md`
- `tools/verify_wc2026_update_results_prompt.py`

## Verification
`make verify` runs the update-results prompt verifier.
