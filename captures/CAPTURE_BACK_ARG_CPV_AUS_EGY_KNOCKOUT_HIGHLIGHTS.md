# Capture Back: ARG/CPV and AUS/EGY knockout highlights

## Intent

Add the user-provided extended highlight URLs for the two Round of 32 feeder matches that produce Argentina vs Egypt in the Round of 16.

## Results

- ARG 3–2 CPV
  - Winner: ARG
  - Extended highlights: https://youtu.be/EC2jOKluGRI

- AUS 1–1 EGY
  - Winner: EGY on penalties
  - Penalty score: EGY 4–2 AUS
  - Extended highlights: https://youtu.be/ACWOG7t8Plk

## Storage shape

The current pick/result popover renders `matchDisplay.extendedHighlightsUrl`.

The model resolves this from:

- `metadata.extendedHighlightsUrl`, or
- `result.extendedHighlightsUrl`

So this slice stores a single flat `extendedHighlightsUrl` field on the official knockout result rows.

Do not store duplicate `highlightUrl` or nested `extendedHighlights` fields for these rows.

## Files changed

- `site/data/official_knockout_results.json`

## Guardrails

- Do not modify `site/data/current/official_truth.json`.
- Do not modify COL/GHA in this slice.
- Do not rebuild official knockout results from scratch.
- Preserve existing result rows.
