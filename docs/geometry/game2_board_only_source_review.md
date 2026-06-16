# Game 2 Board-Only Source Review

This review surface intentionally strips Game 2 back to the board image only.

The current Workbench decision is that the shared 32-bit anti-aliased PNG game board is the geometry authority. Before Game 2 renders bracket items, future nodes, hit targets, or advancement edges, the board itself must be inspectable without competing layers.

## Expected surface

`site/game2/index.html` should display only:

- the shared R32 game board image
- centered/scaled as one 1536 × 1024 pixel-native plane

It should not display:

- seeded team cards
- future node placeholders
- champion card
- toolbar buttons
- bracket item ledger
- percent-based placement approximations

## Next step after this review

Once the board image is accepted, the next implementation should define pixel-native board regions. Each logical item must map to a native pixel-defined region before it is allowed back onto the Game 2 surface.
