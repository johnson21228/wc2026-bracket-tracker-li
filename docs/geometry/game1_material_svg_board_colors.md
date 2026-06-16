# Game 1 Material SVG Board Colors

This capture tunes the transparent SVG middle-layer board away from white technical linework and toward the sampled warm material palette.

Layer intent:

1. Bottom pub/image layer remains visible.
2. Uniform SVG middle layer shows the whole bracket using transparent background, dark brown linework, and tan slot fills.
3. R32 pick-card targets use stronger translucent tan fill to indicate selectability in Game 1.
4. Hit targets and selected pick cards sit above the SVG.
5. Menus and tooltips sit above all board layers.

Sampled color targets:

```text
Pick-card slot fill: #816A51
Bracket linework and outlines: #542C23
```

Authority chain:

```text
tools/generate_uniform_pick_card_gameboard.py
-> site/assets/playfield/uniform_pick_card_gameboard.svg
-> site/data/geometry/uniform_pick_card_gameboard_manifest.json
-> site/assets/playfield/uniform_pick_card_gameboard.png
```

The SVG and manifest remain the only source of Game 1 board geometry. Game 1 must not invent separate R32 placement geometry.
