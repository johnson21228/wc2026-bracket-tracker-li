# Game 1 FIFA R32 extraction, logic map, geometry bridge, and render proof

## Goal

Make the game board shaped like FIFA while keeping logic and rendering separate.

## Layers

### Source evidence

```text
source/images/game1_fifa_to_board_mapping_reference_20260617.png
source/text/fifa_r32_slot_extraction_20260617.md
source/text/fifa_r32_slot_extraction_20260617.json
```

### FIFA logical slot order

```text
site/data/model/fifa_r32_logical_slot_order.json
```

This owns labels like `1E`, `3 ABCDF`, `1I`, and their side/order/matchup pairing.

### Board geometry

```text
site/data/geometry/gameboard_manifest.json
```

This owns board slot bounds and visual placement.

### Bridge map

```text
site/data/geometry/game1_fifa_slot_geometry_map.json
```

This maps FIFA slot IDs to board geometry slot IDs.

### Render proof

```text
site/js/board/FifaSlotMapLayer.js
```

The developer toggle can render the FIFA labels over the board to prove that logic and geometry line up.
