# Shared Pixel-Native Game Board Source

This Workbench now treats the game board as one shared image-backed coordinate plane.

## Canonical board

- Asset: `site/assets/playfield/r32_game_board_hd.jpeg`
- Native size: 1536 × 1024
- Board unit: one native image pixel

## Rule

Game 1 and Game 2 use the same board image and the same coordinate system. Game behavior may differ, but geometry does not.

## Mapping

A logical item is valid only when it has a pixel definition on the canonical board. Examples:

- `game1.r32.slot01` maps to a native pixel rectangle on the board.
- `game2.r32.slot01` may reuse the same pixel rectangle with different game behavior.
- `game2.r16.slot01` maps to a later-round pixel rectangle on the same board.

## Display scaling

The page may scale the entire 1536 × 1024 board plane to fit the browser. Pointer coordinates must be converted back into native board pixels before hit testing.

## Not allowed

- A second image defining competing slot geometry.
- Independent CSS offsets that are not derived from board pixels.
- Page-percent or viewport-percent geometry as source truth.
- A logical bracket item that has no native pixel region.
