# Card 062 — Capture shared 32-bit PNG game board source

## Intent

Establish the 32-bit anti-aliased PNG as the single shared game board authority for Game 1 and Game 2.

## Decision

Use:

`site/assets/playfield/r32_bracket_geometry_overlay.png`

as the canonical runtime board image and native pixel coordinate system.

## Rationale

PNG preserves alpha, anti-aliased geometry, and stable pixel boundaries. JPEG should not define geometry truth because it introduces compression artifacts and lacks transparency.

## Invariant

Every Game 1 and Game 2 logical item must map to a pixel-defined region on the 1536 × 1024 board. The page may scale the full board plane, but hit-testing and rendering must remain pixel-native.

## Next

Capture R32 slot geometry from the PNG into pixel-native data, then use that same data for rendering and hit-testing.
