# Card 063 — Capture R32 PNG Geometry Source

## Purpose

Declare the uploaded R32 bracket PNG as the current geometry authority for the two WC2026 apps.

## Decision

The image defines the current geometry. Numeric slot geometry is a measured representation to be captured from the image.

## Preserved behavior

- Game 1 remains the R32 selection app.
- Game 2 remains the seeded bracket-item app.
- Both apps continue using the shared middle-layer bracket geometry concept.

## Added artifacts

- `li/world_cup/r32_png_geometry_source_rule.md`
- `docs/geometry/r32_png_geometry_source.md`
- `site/data/geometry/r32_png_geometry_source_manifest.json`
- `site/assets/playfield/r32_bracket_geometry_overlay.png`
- `site/assets/playfield/r32_bracket_game_board_template.jpeg`

## Next card

Capture measured R32 slot boxes from the PNG into `site/data/game2_bracket_geometry_slots.json`, then render Game 2 bracket items into those slots.
