# Card 066 — Capture Shared Pub Background Layer

## Intent

Keep the pub/background image as a shared atmospheric layer behind the transparent game board for both Game 1 and Game 2.

## Decision

The pub background is not geometry. The 1536 × 1024 RGBA board PNG remains the geometry authority.

## Acceptance

- Game 1 opens with the board over the pub background.
- Game 2 opens with the board over the pub background.
- Verify and pack pass.
- Board coordinate logic remains pixel-native to the board image.
