# Game 1 R32 Assignment Layer Rule

Game 1 uses the shared pixel-native board image as its geometry authority.

The board plane is fixed at 1536 × 1024 native board units. One board unit equals one native PNG pixel. The browser may scroll the full plane, but Game 1 must not independently scale, offset, or approximate the slot geometry.

Game 1 behavior is distinct from Game 2 behavior:

- Game 1 lets the user assign teams into the 32 Round of 32 slots.
- Game 2 starts from a seeded bracket and advances winners.

Game 1 may render chooser and pick state above the shared board, but every R32 slot control must be mapped to a native pixel rectangle on the shared board.

The canonical shared board image is:

```text
site/assets/playfield/r32_bracket_geometry_overlay.png
```

The Game 1 assignment layer must preserve the invariant:

```text
logical R32 assignment slot -> pixel-defined board region -> hit target -> rendered pick
```

No Game 1 assignment slot may be positioned by viewport percent, guessed CSS offsets, or a separate game-specific geometry image.
