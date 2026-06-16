# Capture Back — Shared 32-bit PNG game board source

## Captured decision

The WC2026 bracket tracker uses the 32-bit anti-aliased RGBA PNG as the current game board truth.

Canonical runtime board:

`site/assets/playfield/r32_bracket_geometry_overlay.png`

Native board size:

`1536 × 1024`

## Behavior preserved

- Game 1 and Game 2 share the same game board image.
- The board is a fixed pixel-native logical plane.
- Every logical item must map to board pixels.
- Browser scaling may only scale the complete board plane as one unit.
- JPEG images are not geometry truth.
- Generated SVG/PNG assets are not geometry truth yet.

## Next implementation

Create pixel-native slot geometry for the R32 slots, then render and hit-test bracket items from those same pixel regions.
