# Card 070 — Align Game 1 to Shared Pixel-Native Board

## Intent

Game 1 and Game 2 should use the same shared 1536 × 1024 32-bit RGBA PNG game board.

## Problem

Game 1 retained a reference to an older JPEG board asset, while Game 2 used the canonical PNG.

## Change

Patch Game 1 to reference:

```text
../assets/playfield/r32_bracket_geometry_overlay.png
```

and create the optional alias:

```text
site/assets/playfield/r32_game_board_hd.png
```

as a copy of the canonical PNG if it is missing.

## Guardrail

Do not alter Game 1 chooser logic or Game 2 board-only review behavior in this card.
