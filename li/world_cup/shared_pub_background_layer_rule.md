# Shared Pub Background Layer Rule

Game 1 and Game 2 may share the same pixel-native game board image, but that board is not the page background.

The shared background layer is the environmental/atmospheric layer behind the board. The bracket board PNG remains the geometry authority; the background must not define hit testing, slot positions, advancement geometry, or rendered bracket item positions.

The current shared background source is:

- `site/assets/playfield/game1_pub_options_background.jpeg`

The current shared board source is:

- `site/assets/playfield/r32_bracket_geometry_overlay.png`
- `site/assets/playfield/r32_game_board_hd.png`

Required invariant:

- The background can scale/cover/fill the viewport.
- The board remains a fixed 1536 × 1024 pixel-native plane.
- Hit testing and rendering map to the board pixels, not the background pixels.
- The board may be transparent so the background shows through.
