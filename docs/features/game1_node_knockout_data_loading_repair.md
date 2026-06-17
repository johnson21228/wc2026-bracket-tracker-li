# Game 1 Node Knockout Data Loading Repair

The browser loads `site/data/game1_data_bundle.js` before Game 1 runtime code executes. The command-line knockout choice-resolution test must mirror that environment.

This repair updates the Node runner to:

- create a minimal VM-backed `window`,
- evaluate `site/data/game1_data_bundle.js`,
- expose both `window.WC2026_GAME1_DATA` and `GAME1_DATA`,
- then evaluate the extracted Game 1 knockout choice-resolution harness.

This keeps the test independent of the browser while preserving the same data precondition as the page.
