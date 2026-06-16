# Shared 32-bit PNG Game Board Source Rule

The canonical runtime game board for the WC2026 bracket tracker is the 32-bit anti-aliased PNG at:

`site/assets/playfield/r32_bracket_geometry_overlay.png`

This PNG is the current geometry authority for both Game 1 and Game 2.

## Board coordinate system

The board is a fixed native pixel plane:

- width: 1536 px
- height: 1024 px
- color model: RGBA / 32-bit PNG

A game board logical unit is one native PNG pixel.

## Shared invariant

Game 1 and Game 2 must use the same board image and the same native pixel coordinate system.

Every logical game item must map to a pixel-defined region on this board, including:

- R32 chooser slots
- Game 1 pick hit targets
- Game 2 seeded bracket slots
- R16, quarterfinal, semifinal, final, and champion slots
- rendered bracket cards
- hit regions
- connector / advancement destinations

The browser may scale the entire 1536 × 1024 board plane for display, but it must not independently scale, offset, or approximate render and hit-test layers.

## JPEG and generated image posture

JPEG board images are not geometry truth because they do not preserve alpha and can introduce compression artifacts.

Generated SVG/PNG geometry may be produced later only after pixel-native geometry has been captured and accepted as truth. Until then, the 32-bit PNG is the authoritative game board.
