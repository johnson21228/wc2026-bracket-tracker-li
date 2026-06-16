# R32 PNG Geometry Source Rule

## Authority

At the current stage of the WC2026 bracket games, the Round of 32 bracket geometry PNG is the geometry authority.

The shared middle-layer image defines:

- bracket slot positions
- bracket slot sizes
- connector paths
- left/right rail placement
- R32, R16, QF, SF, final, and champion visual locations
- where Game 1 hit targets and Game 2 bracket items must be aligned

## Source assets

Authoritative transparent middle layer:

```text
site/assets/playfield/r32_bracket_geometry_overlay.png
```

High-contrast measuring/reference image:

```text
site/assets/playfield/r32_bracket_game_board_template.jpeg
```

## Current-stage rule

The image is truth. Slot geometry data is a captured representation of the image, not an independent design source.

Therefore:

```text
PNG geometry authority
  -> measured/captured slot geometry JSON
  -> bracket items and hit targets placed from JSON
```

The JSON must conform to the PNG. The PNG must not be distorted to fit the JSON during this stage.

## Future-stage rule

Only after the measured JSON faithfully represents the PNG may the project promote numeric geometry to truth geometry.

At that future stage:

```text
truth geometry JSON
  -> generated SVG/PNG middle layer
  -> bracket items and hit targets placed from the same JSON
```

Until that promotion is explicitly accepted, generated geometry is experimental evidence only.

## Regression guard

Any Capture Back that touches Game 2 bracket item placement, Game 1 hit targets, or middle-layer assets must preserve this authority chain or explicitly state that it is changing the geometry source of truth.
