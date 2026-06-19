# WC2026 Raw Pick ID Truth Model

The site needs two related but separate models:

1. **Raw pick state** — the durable saved user record.
2. **Projection/UI state** — the board rendering, hit targets, and visual slot mapping.

## Raw pick state

The raw pick state is what should be saved locally and later sent to a backend.

```json
{
  "schemaVersion": 1,
  "userId": "local-user",
  "tournamentId": "wc2026",
  "gameId": "game1",
  "status": "draft",
  "picks": {
    "game1.r32.slot01": null,
    "game1.r32.slot02": null,
    "game1.final.champion": null,
    "game1.thirdPlace.winner": null
  }
}
```

## Projection/UI state

The projection model may use visual board IDs and geometry:

```text
L-R32-01
R-R16-04
CENTER-FINAL-FOUR
boundsPx
```

Those identifiers are valid for rendering, hit testing, and board layout. They are not the raw storage authority.

## Stable pick ID invariant

```text
pickId is truth.
visual slot is projection.
UI geometry may change.
pickId must not change.
```

## Recommended next manifest

Add a canonical pick ID manifest:

```text
site/data/model/canonical_pick_ids.json
```

The manifest should contain:

- Game 1 expected total: 64 raw pick IDs.
- Game 2 expected total: 32 raw pick IDs.
- Stable IDs for R32 entrants, advancement winners, champion, and third-place winner.
- Enough metadata for validation without binding to `boundsPx` or current board geometry.

## Projection map

A later projection map may connect storage truth to the board:

```text
pickId -> sitePickId
pickId -> visual slot
pickId -> candidate source
```

That map is allowed to change as the UI evolves. The raw pick ID is not.
