# Uniform SVG Gameboard Width Enhancement Rule

This is a reference LI rule for a possible future enhancement.

The uniform SVG gameboard width is governed by the SVG geometry model, not by browser-only scaling.

If the board needs to become narrower, the change must be made in the shared SVG/generator geometry authority and then projected into all derived artifacts:

- `site/assets/playfield/uniform_pick_card_gameboard.svg`
- `site/assets/playfield/uniform_pick_card_gameboard.png`
- `site/data/geometry/uniform_pick_card_gameboard_manifest.json`
- `site/data/geometry/uniform_pick_card_gameboard_manifest.js`

A narrower board must preserve the layered model:

1. bottom image/background layer
2. transparent SVG middle gameboard layer
3. manifest-driven hit regions
4. manifest-driven pick-card fills
5. menus/tooltips/overlays

A narrower board must preserve geometry integrity. The visible SVG slot rectangles, connector endpoints, hit targets, and pick-card placement must all derive from the same geometry model.

Do not create a narrower board by applying CSS compression to the rendered board while leaving the manifest unchanged. That creates drift between what the user sees and what the app can hit or fill.

The first narrowing pass should be conservative and reversible. It should keep the existing board model unless a later card explicitly changes it:

- 32 R32 slots
- 16 R16 slots
- 8 QF slots
- 4 SF slots
- 1 Final Four center card
- 61 visible pick-card records total

Game 1 and Game 2 must not diverge into separate board geometry systems. If a narrower board becomes the accepted board, both games should eventually consume the same regenerated manifest contract.
