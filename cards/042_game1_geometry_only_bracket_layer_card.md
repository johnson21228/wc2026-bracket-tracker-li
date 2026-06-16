# Card 042 — Game 1 Geometry-Only Bracket Layer

## Intent
Replace the numbered transparent board overlay with a geometry-only alpha PNG so the pub background shows through and slot numbers are not baked into the middle visual layer.

## Acceptance
- `site/assets/playfield/r32_bracket_geometry_overlay.png` exists.
- `site/game1/index.html` uses the geometry overlay as the Game 1 board/middle layer.
- The geometry image contains bracket rectangles and connector lines only.
- Hit testing remains runtime-driven and above decorative layers.
