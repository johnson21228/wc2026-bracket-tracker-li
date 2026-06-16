# Card 057 — Capture Game 2 Bracket Geometry Slots

## Intent
Move Game 2 from near-board item placement to image-defined slot placement.

## First-order rule
Bracket items must be rendered into bracket slots captured from the shared middle-layer PNG.

## Evidence
- `site/data/game2_bracket_geometry_slots.json` captures the current image-defined slot geometry.
- `site/game2/index.html` renders bracket items by `slotId` into that geometry.
- Game 1 is not touched.
