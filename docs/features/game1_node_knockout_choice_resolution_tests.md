# Game 1 Node knockout choice resolution tests

Game 1 knockout winner-pick behavior needs a command-line test before more UI wiring is added.

The test runner extracts the existing `WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS` script from `site/game1/index.html`, evaluates it inside a minimal Node VM `window`, seeds deterministic bracket picks, and verifies that contestant resolution returns exactly two choices.

## Tested paths

- `R16-1` resolves from `R32-1` and `R32-2`.
- `R16-2` resolves from `R32-3` and `R32-4`.
- `QF-1` resolves from `R16-1` and `R16-2` winner picks.
- `SF-1` resolves from `QF-1` and `QF-2` winner picks.

## Command

```bash
node tools/run_wc2026_game1_knockout_choice_resolution_tests.js
```

This test does not require a browser. It fails if a tested slot resolves zero or one contestant instead of two.
