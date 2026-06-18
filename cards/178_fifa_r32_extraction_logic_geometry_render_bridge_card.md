# Card 178 — FIFA R32 extraction, logic map, geometry bridge, and render proof

## Intent

Capture the FIFA-to-board mapping image, extract the FIFA R32 slot logic, keep logic separate from board geometry, and prove rendering can use both.

## Boundary

Keep these separate:

```text
source image / extraction evidence
  source/images/game1_fifa_to_board_mapping_reference_20260617.png
  source/text/fifa_r32_slot_extraction_20260617.md
  source/text/fifa_r32_slot_extraction_20260617.json

FIFA logic
  site/data/model/fifa_r32_logical_slot_order.json

Board geometry
  site/data/geometry/gameboard_manifest.json

Bridge
  site/data/geometry/game1_fifa_slot_geometry_map.json

Render proof
  site/js/board/FifaSlotMapLayer.js
```

## Acceptance

- The source image is stored.
- The human-reviewed extraction is stored.
- The FIFA logical slot order has 32 unique R32 slots.
- The geometry bridge has 32 matching R32 slots.
- Every bridge geometry slot exists in the board manifest.
- The developer UI can show/hide the FIFA slot map.
- `make verify` and `make pack` pass.
