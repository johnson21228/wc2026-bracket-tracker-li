# Game 1 Board-Attached Back Layer Rule

Game 1 must render its atmospheric back layer inside the same pixel-native board stack as the shared 1536 × 1024 game board.

The back layer is not geometry truth. It is visual atmosphere behind the transparent 32-bit RGBA board PNG. The board PNG remains the geometry authority.

Required invariant:

- Game 1 uses a board-attached back layer, not a fixed page background.
- The back layer, board PNG, hit targets, and rendered picks scroll together.
- The back layer must sit behind `site/assets/playfield/r32_bracket_geometry_overlay.png`.
- Game 1 logical items remain mapped to the shared pixel-native board plane.
- The page body may provide only a dark fallback color.
