# Game 1 R32 Assignment Layer

This feature restores Game 1 behavior on top of the shared pixel-native board surface.

Game 1 now presents the same scrollable 1536 × 1024 board plane used by Game 2, then adds one lightweight assignment layer above it. The layer creates 32 Round of 32 slot controls using native pixel coordinates.

The user can tap a numbered R32 slot, choose a team, and store that assignment in browser localStorage. Export produces a JSON record that includes board metadata and slot assignments.

This does not change Game 2. It keeps the architecture split:

```text
Shared:
  board image
  pixel-native coordinate plane
  board-attached background model

Game 1:
  R32 chooser
  team assignment storage

Game 2:
  seeded bracket and advancement behavior
```

The current slot map is a first runtime map for the generated uniform-slot board. Future work can move the slot definitions out of the HTML and into a shared `site/data/board/` geometry file.
