# Card 202: Capture UPDATE RESULTS Prompt

## Intent
Make `UPDATE RESULTS` a reusable Workbench prompt for safely finding missing group-stage results from current internet sources.

## Rule
The prompt must inspect repo data first, search only stale/missing candidate matches, and patch only confirmed final results.

## Acceptance
- `prompts/update_results_from_web.md` exists.
- `UPDATE RESULTS` trigger phrase is documented.
- `PATCH`, `WATCH`, `WAIT`, and `CONFLICT` decisions are present.
- Verification is wired into `make verify`.
