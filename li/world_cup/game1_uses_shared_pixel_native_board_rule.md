# Game 1 Uses Shared Pixel-Native Board Rule

Game 1 and Game 2 must use the same canonical 1536 × 1024 32-bit RGBA game board PNG as their board geometry source.

Canonical runtime board:

```text
site/assets/playfield/r32_bracket_geometry_overlay.png
```

Optional alias, when present:

```text
site/assets/playfield/r32_game_board_hd.png
```

Game 1 may keep its own behavior layer: R32 chooser, group filtering, user pick storage, and visible hit targets. Game 2 may keep its own behavior layer: seeded bracket, advancement picks, and final-four custom presentation. But neither game may use a separate board image, separate board coordinate system, or independently guessed visual geometry.

The board image defines the shared pixel-native coordinate plane:

```text
width: 1536 px
height: 1024 px
mode: RGBA / alpha-capable PNG
```

The browser may scroll or scale the full board stack as a whole, but the background layer, board PNG, hit/render layers, and logical items must remain attached to the same board plane.
