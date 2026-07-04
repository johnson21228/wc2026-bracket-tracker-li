# Capture Back: Colombia/Ghana knockout result

## Intent

Add only the official Colombia vs Ghana Round of 32 result to the append-only knockout results file.

## Result

- COL 1–0 GHA
- Winner: COL
- Highlight URL: https://youtu.be/9TJRhuQOJuE

## Files changed

- `site/data/official_knockout_results.json`

## Guardrails

- Do not modify `site/data/current/official_truth.json`.
- Do not add or update Argentina vs Cabo Verde in this slice.
- Do not rebuild official knockout results from scratch.
- Preserve existing result rows.
