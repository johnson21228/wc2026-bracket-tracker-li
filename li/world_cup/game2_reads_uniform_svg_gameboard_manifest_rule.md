# Game 2 Reads Uniform SVG Gameboard Manifest Rule

Game 2 must share the same uniform SVG-derived gameboard geometry contract as Game 1, but migration must proceed in safe stages.

This stage is read-only:

- Game 2 may load `site/data/geometry/uniform_pick_card_gameboard_manifest.js`.
- Game 2 may validate the 61-slot board model.
- Game 2 may expose probe state for developer verification.
- Game 2 must not yet switch its visible board layer.
- Game 2 must not yet remap R32 seeded cards.
- Game 2 must not yet remap R16, QF, SF, Final Four, or advancement destinations.

Game 2 interpretation differs from Game 1:

- Game 1 interprets R32 slots as selectable prediction targets.
- Game 2 interprets R32 slots as seeded knockout starting positions.
- Game 2 will eventually use R16/QF/SF/Final Four manifest slots as advancement destinations.

No Game 2 runtime may invent independent bracket geometry after migration begins. Geometry must come from the uniform SVG generator/manifest chain.
