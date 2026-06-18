# Card 159 — Promote pub background truth asset

## Intent

Move the legacy-discovered pub background image into the clean site's board-truth resource structure and render the background layer from that promoted asset.

The old visual foundation used:

- `site/assets/playfield/game1_pub_options_background.jpeg`

The clean site should render from the board-truth asset path:

- `site/assets/board-truth/backgrounds/pub_background.jpeg`

## Boundary

This card does not add:

- SVG rendering
- manifest rendering
- pick rendering
- menu behavior
- player state
- localStorage

## Acceptance

- `site/assets/board-truth/backgrounds/pub_background.jpeg` exists.
- The promoted asset matches `site/assets/playfield/game1_pub_options_background.jpeg` byte-for-byte.
- `site/new/js/services/assetPaths.js` uses the promoted background path.
- `site/new/js/board/BackgroundLayer.js` renders the promoted background layer.
- `tools/verify_wc2026_pub_background_truth_asset.py` passes.
