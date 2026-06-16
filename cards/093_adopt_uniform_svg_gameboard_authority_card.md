# Card 093 — Adopt Uniform SVG Gameboard Authority

## Intent

Capture the new uniform pick-card gameboard as an SVG-first board authority candidate without immediately migrating Game 1 or Game 2 runtime surfaces.

## Why

The prior board assets carry varying pick-card sizes. The desired next board uses uniform pick-card size/shape from R32 through SF and a larger centered Final Four pick card.

## Done when

- The uniform SVG asset exists under `site/assets/playfield/`.
- The derived PNG exists under `site/assets/playfield/`.
- The manifest exists under `site/data/geometry/`.
- LI states that SVG is geometry authority and PNG is a derivative.
- The generator and verifier are available.
- Existing Game 1/Game 2 entrypoints are not switched by this CB.
