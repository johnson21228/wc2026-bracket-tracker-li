# Game 1 Shared Board Alignment

This patch aligns Game 1 with the current shared board architecture.

Before this rule, Game 1 could still reference an older JPEG board image while Game 2 referenced the canonical PNG. That creates visual drift because JPEG and PNG are different source artifacts.

The correction is small and deliberate:

- Game 1 must display `site/assets/playfield/r32_bracket_geometry_overlay.png`.
- Game 2 already displays `site/assets/playfield/r32_bracket_geometry_overlay.png`.
- The optional `r32_game_board_hd.png` alias may be created as a byte-for-byte copy of the canonical PNG for human-friendly naming.
- Game 1 chooser logic is not changed.
- Game 2 board-only review logic is not changed.

The shared model is:

```text
board-attached background
shared 1536 × 1024 RGBA board PNG
pixel-native hit/control/render layers
separate game behavior
```
