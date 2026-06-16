# Game 1 Uniform SVG Board Layer

This change switches Game 1's visible board image from the previous PNG board layer to the new uniform SVG gameboard asset.

The purpose is to review the new board visual in the real Game 1 layered surface without yet moving hit targets or pick cards to the new geometry manifest.

## Preserved layers

The layered structure remains intact:

1. pub/background layer
2. visible gameboard layer
3. pick-card layer
4. hit-target layer
5. chooser/menu/tooltip UI

Only the visible gameboard image changes.

## New visible asset

```text
site/assets/playfield/uniform_pick_card_gameboard.svg
```

The derived PNG remains available for quick visual review:

```text
site/assets/playfield/uniform_pick_card_gameboard.png
```

## Deferred work

The following are intentionally not changed by this step:

- Game 1 pick-card placement
- Game 1 hit-target placement
- Game 1 chooser/menu behavior
- Game 2 board visual
- Game 2 slot geometry

A later CB should align Game 1 placement and hit testing to the manifest after the visible board switch is reviewed.
