# Card 176 — Show Game 1 lifecycle status on the board surface

## Intent

Make the Game 1 lifecycle visible on the player board surface.

The board should tell players what kind of game they are currently playing:

```text
GROUP_STAGE_OPEN
R32_PROJECTION_LIVE
FIFA_R32_LOCKED
KNOCKOUT_PICKING_OPEN
KNOCKOUT_LIVE
COMPLETE
```

## Product promise

```text
Pick the bracket before FIFA locks it.
Watch the groups reshape the board.
See whether your read of the tournament was right.
```

## Change

Add a board layer that reads:

- `site/data/model/game1_lifecycle.json`
- `site/data/model/game1_lifecycle_seed.json`

and displays the current lifecycle state and invitation copy directly on the board.

## Acceptance

- The board includes a visible Game 1 lifecycle status surface.
- The surface includes the current lifecycle state.
- The surface includes the Game 1 product promise/invitation.
- The surface fails soft if JSON is unavailable.
- `make verify` and `make pack` pass.
