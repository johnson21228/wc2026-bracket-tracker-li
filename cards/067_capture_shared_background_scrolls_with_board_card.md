# Card 067 — Capture Shared Background Scrolls With Board

## Intent

Make the pub/background layer scroll with the board in both Game 1 and Game 2.

## Decision

The background belongs to the pixel-native board stack. It is not fixed to the browser viewport.

## Acceptance

- Game 1 opens with the pub/background moving with the game board.
- Game 2 opens with the pub/background moving with the game board.
- No runtime geometry uses the background as truth.
- Verify and pack pass.
