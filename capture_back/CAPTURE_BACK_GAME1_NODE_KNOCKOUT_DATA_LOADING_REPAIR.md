# Capture Back — Game 1 Node Knockout Data Loading Repair

## Captured problem
The command-line knockout choice-resolution test failed after lifecycle-state work because the extracted Game 1 harness expected `GAME1_DATA` / `window.WC2026_GAME1_DATA`, but the Node VM did not load the browser data bundle first.

## Captured decision
Repair the Node runner rather than weakening the harness. The runner should mirror the browser precondition by evaluating `site/data/game1_data_bundle.js` before evaluating the extracted harness.

## Captured outcome
The test can continue to run without a browser while still proving that R16/QF/SF menus can resolve exactly two match contestants from existing picks.
