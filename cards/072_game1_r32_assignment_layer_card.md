# Card 072 — Restore Game 1 R32 Assignment Layer

## Intent

Restore the Game 1 interaction layer after the board-only alignment work.

## Change

Game 1 now uses the shared 1536 × 1024 RGBA board image and renders 32 native-pixel R32 assignment targets above it.

## Acceptance

- Game 1 opens as a scrollable board surface.
- The visible board image is `site/assets/playfield/r32_bracket_geometry_overlay.png`.
- The user can tap an R32 slot and assign a team.
- Assignments persist in localStorage.
- Game 2 remains separate.
- `make verify` passes.
