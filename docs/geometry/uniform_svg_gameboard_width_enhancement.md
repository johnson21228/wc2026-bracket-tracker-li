# Uniform SVG Gameboard Width Enhancement

This document captures a possible future improvement: make the uniform SVG gameboard slightly narrower.

## Current issue
In browser review, the board can feel too wide. Some pick-card columns are near the viewport edges, and the overall bracket surface may benefit from a modest width reduction.

## Why this belongs in LI
The board is now governed by the SVG/generator/manifest chain. Width is therefore not just a visual CSS preference. It affects:

- visible SVG slot rectangles
- connector routing
- hit target rectangles
- pick-card placement
- the board viewBox and scaling plane

## Recommended approach
Make a narrower board by tuning geometry constants in `tools/generate_uniform_pick_card_gameboard.py`, then regenerate the SVG, PNG, and manifest together.

Avoid CSS-only squeeze transforms, because they can make visual geometry differ from runtime hit geometry.

## Suggested conservative target
A first pass could try:

- R32 slot width reduced by about 15–20%
- inner round slot width reduced by about 10–15%
- slightly tighter outer margins
- slightly tighter round columns
- unchanged 61-card model
- centered Final Four card
- preserved bottom-layer visibility

## Not part of this card
This card does not request the change now. It only preserves the enhancement idea for later.
