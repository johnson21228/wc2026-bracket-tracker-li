# Game 1 Geometry-Only Bracket Layer

Game 1 uses three visual/interaction layers:

1. Pub JPEG background layer.
2. Transparent bracket geometry PNG layer.
3. Runtime hit targets, picks, and chooser modal.

The geometry PNG is a full-size alpha-channel asset. It must not contain baked-in slot numbers, team names, flags, or pick state.
