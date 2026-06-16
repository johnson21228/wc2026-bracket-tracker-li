# Uniform SVG Gameboard Authority Rule

The uniform pick-card gameboard SVG is the geometry truth for the next shared WC2026 bracket board family.

## Authority stack

`site/assets/playfield/uniform_pick_card_gameboard.svg` is the source-truth geometry artifact.

`site/data/geometry/uniform_pick_card_gameboard_manifest.json` is the app-readable projection of that SVG geometry.

`site/assets/playfield/uniform_pick_card_gameboard.png` is a rendered visual derivative for review, fallback, and export.

The SVG is not merely artwork. It defines the board coordinate system, pick-card rectangles, connector linework, round placement, Final Four center-card placement, board viewBox, and aspect ratio.

## Source-truth rule

Do not treat the PNG as geometry truth.

Do not hand-maintain the manifest independently from the SVG geometry.

When board geometry changes, the SVG and manifest must remain synchronized. The verifier must compare the SVG pick-card rectangles to the manifest records.

## Layer contract

The existing layered board architecture remains in force:

1. Bottom layer: decorative pub/background/world-cup texture. It is decorative only.
2. Gameboard layer: generated/reviewed SVG bracket board and derived PNG.
3. Interaction layer: transparent hit regions mapped to the SVG/manifest geometry.
4. Pick-card layer: rendered picks placed above the gameboard using manifest slot rectangles.
5. Overlay/UI layer: menus, tooltips, chooser, debug labels, and scoring state.

## Both-game geometry rule

Game 1 and Game 2 must share the same SVG-derived board geometry contract when migrated to this board family.

Game 1 may interpret R32 slots as qualifier-prediction slots.

Game 2 may interpret R32 slots as seeded knockout slots.

Neither game may invent independent slot geometry.

## Current board model

The current uniform board model intentionally has 61 pick-card records:

- R32: 32
- R16: 16
- QF: 8
- SF: 4
- FINAL_FOUR: 1

The `FINAL_FOUR` record is one special center Final Four pick card, not two finalist cards plus a champion card.

R32 through SF pick-card slots use uniform standard card dimensions.

The center Final Four pick card is special. It may be taller and wider than standard cards, remains centered in the board, and still receives visible connector linework behind it.

## Migration posture

This rule establishes the asset pipeline and geometry authority only. It does not require Game 1 or Game 2 to switch immediately.

Legacy board assets remain valid until a later migration CB intentionally points pages at this SVG/manifest family.
