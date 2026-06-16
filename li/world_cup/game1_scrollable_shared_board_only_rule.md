# Game 1 Scrollable Shared Board-Only Rule

Game 1 may enter a board-only review mode to confirm that it sits on the same pixel-native board plane as Game 2.

In this mode, Game 1 must show the shared 1536 × 1024 RGBA board PNG and board-attached background, with no visible chooser, pick cards, or independent geometry.

The board source is:

```text
site/assets/playfield/r32_bracket_geometry_overlay.png
```

Game 1 behavior remains conceptually separate from Game 2 behavior. This rule only aligns the review surface and shared board resource. Game 1 chooser logic may be reintroduced later as a layer over the same pixel-native board.
