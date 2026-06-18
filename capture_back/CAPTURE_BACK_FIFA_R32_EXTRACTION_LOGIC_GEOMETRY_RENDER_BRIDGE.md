# Capture Back — FIFA R32 extraction, logic map, geometry bridge, and render proof

## Decision

The uploaded FIFA-shaped board image is valuable because it shows how FIFA R32 labels map onto the game board.

## What was captured

```text
source/images/game1_fifa_to_board_mapping_reference_20260617.png
source/text/fifa_r32_slot_extraction_20260617.md
source/text/fifa_r32_slot_extraction_20260617.json
```

## What became runtime data

```text
site/data/model/fifa_r32_logical_slot_order.json
site/data/geometry/game1_fifa_slot_geometry_map.json
```

## Boundary

FIFA logic, geometry, and rendering remain separate.

The extraction says what each R32 slot means. The geometry manifest says where board slots are. The bridge connects those two without merging them.
