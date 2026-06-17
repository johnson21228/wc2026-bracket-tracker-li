# WC2026 Game 1 lifecycle status surface

The game board is the primary invitation surface. Game 1 begins before the official Round of 32 is locked, so the board must explain the current phase.

## Board surface responsibilities

- Identify the current Game 1 lifecycle state.
- Explain what the player can do now.
- Reinforce the product promise.
- Stay read-only.

## Data source

The surface reads:

```text
site/data/model/game1_lifecycle.json
site/data/model/game1_lifecycle_seed.json
```

It displays the first seed record's `lifecycleState` and maps it to player-facing invitation copy.
