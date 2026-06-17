# Repair Game 1 Node Knockout Data Loading

Patch the command-line Game 1 knockout choice-resolution test runner so it loads `site/data/game1_data_bundle.js` before evaluating the extracted Game 1 test harness. Verify that the runner reports `dataBundleLoaded: true` and still validates R16/QF/SF contestant resolution.
