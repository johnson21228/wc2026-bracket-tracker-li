# Card 068 — Capture Game 1 Board-Attached Back Layer

## Intent

Ensure Game 1 has a visible back layer behind the transparent shared game board.

## Decision

Game 1 uses a board-attached pub/background layer inside the same board stack as the 1536 × 1024 RGBA board PNG.

## Acceptance

- Game 1 opens with the pub/background visible behind the board PNG.
- The background scrolls with the board.
- Game 1 hit targets and rendered picks remain above the board.
- Verify and pack pass.
