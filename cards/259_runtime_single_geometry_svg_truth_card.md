# Card 259: Runtime single geometry SVG truth

## Status
Done

## Intent
Make the runtime board linework render from the same SVG authority used to derive the pick-card geometry manifests.

## Change
- Updated `site/js/services/assetPaths.js` so `svgGameboardDefinition` points to `assets/playfield/uniform_pick_card_gameboard.svg`.
- Added `tools/verify_wc2026_runtime_uses_single_geometry_svg_truth.py`.
- Wired the verifier into `make verify`.

## Acceptance
`make verify` must fail if runtime linework points back to stale `assets/board/gameboard.svg` instead of the playfield source-truth SVG.
