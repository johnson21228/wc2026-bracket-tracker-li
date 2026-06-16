# Card 063 — Game 2 Board-Only Source Review

## Intent

Reset Game 2 to a board-only review surface so the shared PNG game board can be accepted as visual and coordinate authority before logical items are reintroduced.

## Change

Replace the Game 2 runtime page with a minimal page that renders only the shared pixel-native board image.

## Acceptance

- `site/game2/index.html` opens to a board-only surface.
- No seeded teams, future nodes, controls, ledgers, or guessed placement layers appear.
- `make verify` passes.
- `make pack` passes.

## Next card

Capture pixel-native board regions and map each logical Game 2 item to a pixel-defined region.
