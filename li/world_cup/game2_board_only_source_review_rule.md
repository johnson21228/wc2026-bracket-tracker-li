# Game 2 Board-Only Source Review Rule

Game 2 may enter a board-only review state when the Workbench is validating the shared pixel-native game board source.

In this state, `site/game2/index.html` must show only the shared game board image. It must not render seeded teams, bracket items, future nodes, chooser controls, storage controls, ledgers, panels, or guessed geometry overlays.

The purpose is to verify the current visual authority before mapping logical items onto pixels.

The board-only surface still preserves the same native game-board coordinate system:

- Source image: `site/assets/playfield/r32_bracket_geometry_overlay.png`
- Native width: `1536`
- Native height: `1024`
- Display behavior: the complete plane may scale as one unit, but no game item may be independently positioned during this review state.

No Game 2 logical item should be reintroduced until it can be mapped to a pixel-defined region on this shared board.
