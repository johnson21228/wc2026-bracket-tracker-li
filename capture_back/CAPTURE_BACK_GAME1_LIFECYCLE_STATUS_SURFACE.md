# Capture Back — Game 1 lifecycle status surface

## Decision

The board is the invitation surface. The Game 1 lifecycle must be visible on the board, not only in developer diagnostics or data files.

## Surface language

```text
Pick the bracket before FIFA locks it.
Watch the groups reshape the board.
See whether your read of the tournament was right.
```

## Boundary

This card adds a read-only board surface layer. It does not mutate picks, standings, lifecycle state, or storage.
