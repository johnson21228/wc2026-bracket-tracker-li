# Card 056 — Fit Game 2 Bracket Items to Image-Defined Slots

## Status
Open / First-order implementation card

## Trigger
Game 2 can seed R32 bracket items, but the visible items are not yet subordinate to the shared middle-layer bracket geometry. They appear near the R32 lanes rather than being fitted into the actual image-defined slot boxes.

## First-order rule
Game 2 bracket items must be rendered into explicit bracket slots captured from the shared middle-layer gameboard PNG.

The current shared middle-layer PNG is the visual geometry source for both Game 1 and Game 2. Until truth geometry data exists, Game 2 must treat the PNG as geometry-defining and capture matching slot data from it.

## Required next implementation
Add or update a Game 2 geometry slot model:

- `site/data/game2_bracket_geometry_slots.json`
- coordinate system should be percent-based against the shared board container
- each R32 slot should have `slotId`, `round`, `x`, `y`, `w`, `h`, and optional `feedsTo`
- each seeded R32 team should become a `bracketItem` assigned to one `slotId`
- rendering should position each `bracketItem` inside its slot box

## Acceptance checks
- Game 2 still opens locally from `site/game2/index.html`
- shared middle-layer PNG remains visible
- seeded R32 data produces 32 bracket items
- all 32 R32 bracket items render inside image-defined slot boxes
- bracket items are not rendered as a loose list
- Game 1 is not touched

## Preservation requirements
Future CBs touching Game 2 runtime must preserve this distinction:

- `bracketSlot` = where an item belongs on the board
- `bracketItem` = the team/pick occupying that slot
- `pickState` = the player's choice over time

## Notes
This card is first-order because later winner advancement depends on the same slot model. R16/QF/SF/Final nodes should receive advanced bracket items by slot/edge, not by ad-hoc visual placement.
