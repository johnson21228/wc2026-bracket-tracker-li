# Card 096 — Switch Game 1 Board Layer to Uniform SVG

## Intent

Let Game 1 display the new uniform SVG gameboard asset inside the existing layered playfield without moving pick-card or hit-target geometry yet.

## Scope

- Use `site/assets/playfield/uniform_pick_card_gameboard.svg` as the Game 1 visible board image.
- Preserve the existing pub/background layer.
- Preserve the existing pick-card layer.
- Preserve the existing hit-target layer.
- Preserve the manifest-read probe from Card 095.
- Do not switch Game 2.

## Acceptance

- `site/game1/index.html` references the uniform SVG as the visible board geometry image.
- Game 1 still loads the uniform manifest shim.
- Game 1 still exposes the manifest probe.
- Game 2 does not reference the uniform SVG board visual.
- Verifiers pass.
