# WC2026 Game 1 projection-to-bracket lifecycle model

Game 1 has two acts.

## Act 1 — Read the field

Players pick the Round of 32 before FIFA locks it. Curated standings updates may reshape projected qualifiers and board placement.

## Act 2 — Play the bracket

After FIFA locks the official Round of 32, the same board becomes a familiar knockout bracket game. The player continues by picking winners from R32 to champion.

## Lifecycle states

```text
GROUP_STAGE_OPEN
R32_PROJECTION_LIVE
FIFA_R32_LOCKED
KNOCKOUT_PICKING_OPEN
KNOCKOUT_LIVE
COMPLETE
```

## Truth layers

```text
playerProjection
  what the player predicted before lock

curatedProjection
  what curated standings currently imply

officialLockedR32
  what FIFA eventually confirms

knockoutWinnerPicks
  post-lock winner picks

history
  scoring evidence and lifecycle events
```
