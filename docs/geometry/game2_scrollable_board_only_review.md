# Game 2 Scrollable Board-Only Review

This review surface displays the shared R32 game board at native size: 1536 × 1024.

The browser page scrolls around the fixed-size board rather than scaling the board to fit the window. This supports pixel-native inspection and reinforces the current invariant:

> The board is the coordinate system. Display scaling is optional, but logical mapping begins in the native pixel plane.

Runtime behavior intentionally hidden in this mode:

- seeded R32 team cards;
- future bracket nodes;
- champion controls;
- pick ledger;
- randomize/initialize controls;
- any geometry overlays that could obscure the board source.

The next build step is to map logical Game 1 and Game 2 items onto pixel-defined regions of this board.
