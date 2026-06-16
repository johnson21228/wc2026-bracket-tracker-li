# R32 PNG Geometry Source

This document captures the current geometry source for the WC2026 bracket games.

## Current truth

The bracket geometry image is the current truth. It is not merely a decorative layer. It defines the visible gameboard shape that both apps must respect.

```text
site/assets/playfield/r32_bracket_geometry_overlay.png
```

A high-contrast version is retained for visual inspection and measurement:

```text
site/assets/playfield/r32_bracket_game_board_template.jpeg
```

## Why this matters

Game 2 currently needs bracket items to occupy the same boxes that the image visually defines. If bracket items are placed by guessed percentages, they can appear near the bracket but not inside the true visual slots.

The next implementation step is therefore not more runtime tuning. It is capturing the image-defined geometry into measured slot data.

## Required direction

```text
1. Use the PNG as the authority.
2. Capture slot boxes from the PNG into JSON.
3. Place Game 2 bracket items by slotId using that JSON.
4. Keep Game 1 hit targets aligned to the same geometry source.
5. Promote JSON to truth only after it faithfully matches the PNG.
```

## Future transition

The future goal remains valid: build the middle layer from numeric truth geometry. But that cannot be the current assumption. The current middle layer already exists and defines the board. The WB must first translate it into durable numbers.
