# Card 174 — Game 1 projection-to-bracket lifecycle model

## Intent

Define Game 1 as a lifecycle game:

1. It begins as a pre-lock Round of 32 projection game.
2. Curated standings can reshape the projected bracket.
3. FIFA eventually locks the official Round of 32.
4. The same board then becomes a familiar knockout bracket game.
5. The user's original pre-lock projection remains scoring evidence.

## Product promise

```text
Pick the bracket before FIFA locks it.
Watch the groups reshape the board.
See whether your read of the tournament was right.
```

## Acceptance

- A lifecycle state model exists.
- A seed Game 1 lifecycle record exists.
- Player projection, curated projection, official locked R32, and knockout winner picks are separate layers.
- The model preserves pre-lock projection picks after official lock.
- The model supports later scoring.
- `make verify` and `make pack` pass.
