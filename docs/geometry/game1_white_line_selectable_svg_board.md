# Game 1 White-Line Selectable SVG Board

This capture repairs the first transparent SVG middle-layer board presentation.

The prior transparent SVG restored behavior, but the board did not yet read as a gameboard over the bottom image. This update makes the bracket linework and slot outlines white, and gives Game 1 R32 selectable targets a translucent fill.

Layer intent:

1. Bottom image/pub/flag layer remains visible.
2. Uniform SVG middle layer shows the full bracket structure with transparent background.
3. R32 selectable targets are visible through SVG fill properties.
4. Hit targets and rendered pick cards sit above the SVG.
5. Menus and tooltips sit above all board layers.

Authority chain:

```text
Generator geometry constants
-> site/assets/playfield/uniform_pick_card_gameboard.svg
-> site/data/geometry/uniform_pick_card_gameboard_manifest.json
-> site/assets/playfield/uniform_pick_card_gameboard.png
```

The SVG and manifest remain the only source of Game 1 board geometry. Game 1 must not invent separate R32 placement geometry.
