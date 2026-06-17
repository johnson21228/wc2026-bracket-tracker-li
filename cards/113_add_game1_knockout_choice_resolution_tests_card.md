# Card 113 — Add Game 1 knockout choice resolution tests

## Intent
Add a test harness that proves knockout winner-pick menus can find exactly two choices from the match contestants that feed a tapped R16/QF/SF slot.

## Rule captured
R16/QF/SF menus must be driven by resolved bracket contestants, not by group eligibility rules and not by static team pools.

## Verification
Run:

```bash
python3 tools/verify_wc2026_game1_knockout_choice_resolution_tests.py
```

In browser console, run:

```js
WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS.testSeededFixture()
```
