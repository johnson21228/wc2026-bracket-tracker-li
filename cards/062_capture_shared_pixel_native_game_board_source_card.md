# Card 062 — Capture Shared Pixel-Native Game Board Source

## Intent

Preserve the decision that both Game 1 and Game 2 use one shared high-definition game board image and one native 1536 × 1024 pixel coordinate plane.

## Acceptance

- `site/assets/playfield/r32_game_board_hd.jpeg` exists as the canonical board image.
- Runtime references to prior bracket board images are redirected to the canonical board image where practical.
- The LI states that every logical game item must map to a pixel-defined region on the shared board.
- Premature generated middle-layer truth artifacts are removed when they compete with the PNG/JPEG board authority.
- `make verify` and `make pack` pass after apply.
