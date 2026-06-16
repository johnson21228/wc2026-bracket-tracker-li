# Shared 32-bit PNG game board source

This Workbench uses one shared runtime board image for Game 1 and Game 2:

`site/assets/playfield/r32_bracket_geometry_overlay.png`

The file is a 1536 × 1024 RGBA PNG. It is the current visual and geometry authority for the bracket board.

## Why PNG, not JPEG

The runtime board should be PNG because it preserves alpha, anti-aliased edges, and exact pixel boundaries without JPEG compression artifacts. JPEG references can be useful for human inspection, but they are not the game board truth.

## Pixel-native mapping

The game board has 1,572,864 native logical units:

`1536 × 1024`

Each logical unit is one source PNG pixel. Game 1 and Game 2 must map all slots, cards, hit targets, and advancement destinations to this native coordinate plane.

The page can scale the entire board plane for responsive display. It must not separately scale or guess the coordinates of controls and rendered bracket items.

## Next step

The next implementation step is to capture the R32 slot boxes from this PNG as pixel-native geometry data. That data should then drive both rendering and hit-testing.
