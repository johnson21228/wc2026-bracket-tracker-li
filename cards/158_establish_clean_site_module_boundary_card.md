# Card 158 — Establish clean site module boundary

## Intent

Establish the clean WC2026 site module boundary before adding more rendering behavior.

The clean site must not become another monolithic HTML implementation. The HTML file provides only base services:

- document shell
- preload hints
- stylesheet links
- app mount
- module entrypoint

Rendering and behavior belong in modules.

## Board truth resources

The clean site owns the board truth resource paths:

- background image truth: `site/assets/playfield/game1_pub_options_background.jpeg`
- gameboard SVG definition truth: `site/assets/playfield/uniform_pick_card_gameboard.svg`
- geometry manifest truth: `site/data/geometry/uniform_pick_card_gameboard_manifest.json`

The current render checkpoint still renders only the background layer.

The SVG and manifest are held as truth resources for the next rendering checkpoints.

## Module boundary

Clean site modules begin under:

- `site/new/js/services/`
- `site/new/js/board/`
- `site/new/js/model/`
- `site/new/js/controllers/`

## Acceptance

- `site/new/index.html` is shell-only.
- `site/new/js/app.js` is the module entrypoint.
- `site/new/js/services/assetPaths.js` owns truth-resource paths.
- `site/new/js/services/domMounts.js` owns mount lookup.
- `site/new/js/board/BoardShell.js` creates the board viewport/plane.
- `site/new/js/board/BackgroundLayer.js` renders the current background layer.
- `site/new/` contains no legacy storage reads.
- `site/new/` contains no legacy render bridge tokens.
- `tools/verify_wc2026_clean_site_module_boundary.py` passes.
