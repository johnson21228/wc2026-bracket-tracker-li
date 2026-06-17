# Card 114 — Add Game 1 Node knockout choice resolution tests

## Intent

Add a repo-runnable, browser-free test for Game 1 knockout choice resolution.

## Rule

R16, QF, and SF choice menus must be testable from the command line. The test must prove that a winner-pick slot can resolve exactly two contestants from its feeding match path.

## Runtime scope

This card adds a Node-based test runner only. It does not change the Game 1 UI or pick behavior.

## Acceptance

- `node tools/run_wc2026_game1_knockout_choice_resolution_tests.js` passes from repo root.
- R16 resolves from feeding R32 assignments.
- QF resolves from feeding R16 winner picks.
- SF resolves from feeding QF winner picks.
- Empty choice sets fail closed.
