# Game 1 knockout choice resolution tests

Game 1 knockout winner menus need a testable source-resolution layer.

The menu rule is:

- R16 choices come from the two R32 contestants that feed the R16 match.
- QF choices come from the two R16 winners that feed the QF match.
- SF choices come from the two QF winners that feed the SF match.

The failure condition is an empty menu or any menu with other than exactly two contestants when both feeder slots have contestants.

This overlay adds a browser-accessible harness at:

```js
window.WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS
```

The first smoke test is:

```js
WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS.testSeededFixture()
```

That test seeds two R32 contestants and verifies that `R16-1` resolves exactly those two choices.
