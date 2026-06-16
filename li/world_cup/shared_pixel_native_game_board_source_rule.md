# Shared Pixel-Native Game Board Source Rule

Game 1 and Game 2 must share one canonical high-definition game board image as the source board surface.

The board image defines a fixed native coordinate system of 1536 × 1024 board units. One board unit equals one native image pixel.

Every logical item used by either game must map to a pixel-defined region on this shared board plane before it is considered valid runtime geometry. This includes R32 slots, later-round slots, rendered bracket cards, hit targets, connectors, and advancement destinations.

The browser may scale the complete board plane as a single unit for display. It must not independently scale, offset, guess, or percent-position hit/render geometry outside the shared pixel-native board coordinate system.

Current canonical board asset:

- `site/assets/playfield/r32_game_board_hd.jpeg`

Legacy/generated board images should not remain as competing geometry authorities. If compatibility paths are needed, they must be treated as aliases only, not as separate sources of truth.
