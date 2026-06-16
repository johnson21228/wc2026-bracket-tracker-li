# Card 064 — Make Game 2 Board-Only Review Scrollable

## Intent

Display the shared game board at native pixel size so the Workbench can inspect the actual 1536 × 1024 board without fit-to-window scaling.

## Change

Game 2 board-only mode now renders the board as a fixed 1536 × 1024 plane inside a scrollable page.

## Acceptance

- `site/game2/index.html` shows only the board image.
- The board is rendered at 1536 × 1024 CSS pixels.
- The page scrolls if the viewport is smaller than the board.
- `make verify` passes.
