# Card 117 — Repair Game 1 Node Knockout Data Loading

## Intent
Keep knockout choice-resolution tests executable outside the browser by loading the same Game 1 data bundle that the browser page loads.

## Rule
The Node runner must evaluate `site/data/game1_data_bundle.js` before evaluating the extracted Game 1 knockout choice-resolution harness.

## Acceptance
- `node tools/run_wc2026_game1_knockout_choice_resolution_tests.js` reports `ok: true`.
- The report includes `dataBundleLoaded: true`.
- The test still validates R16, QF, and SF two-contestant resolution.
