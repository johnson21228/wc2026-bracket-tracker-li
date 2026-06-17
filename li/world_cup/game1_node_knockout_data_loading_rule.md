# Game 1 Node Knockout Data Loading Rule

Any command-line test that evaluates Game 1 runtime or test harness JavaScript must install the Game 1 data authority before executing code that depends on it.

Authority order:

1. `site/data/game1_data_bundle.js`
2. extracted Game 1 runtime/test harness script
3. seeded test fixtures

The runner must fail closed with a clear error if the data bundle is missing or does not install `window.WC2026_GAME1_DATA`.
