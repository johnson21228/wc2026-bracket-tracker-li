# Shared Pub Background Layer

This capture separates two visual responsibilities:

1. **Background layer** — mood/environment behind the game board.
2. **Board geometry layer** — the 1536 × 1024 pixel-native board that owns slots, hit targets, item placement, and advancement regions.

The pub background should help the board feel like a game surface, but it is not geometry truth. Game 1 and Game 2 should both be able to render the same board over the same pub background without changing board coordinates.

Current background image:

- `site/assets/playfield/game1_pub_options_background.jpeg`

Current board image:

- `site/assets/playfield/r32_bracket_geometry_overlay.png`

Implementation note: page/body backgrounds may use viewport cover behavior, while board/hit/render layers must remain in the native board coordinate system.
