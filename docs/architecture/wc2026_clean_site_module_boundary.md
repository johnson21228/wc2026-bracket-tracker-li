# WC2026 clean site module boundary

The clean WC2026 site is intentionally separated from the legacy monolithic runtime.

## Shell

`site/new/index.html` provides only:

- HTML document shell
- CSS links
- preload hints
- app mount: `#wc2026-app`
- module entrypoint: `js/app.js`

## Modules

| Module | Responsibility |
| --- | --- |
| `js/app.js` | App entrypoint |
| `js/services/assetPaths.js` | Board truth-resource paths |
| `js/services/domMounts.js` | Required DOM mount lookup |
| `js/board/BoardShell.js` | Board viewport and native board plane |
| `js/board/BackgroundLayer.js` | Background image layer |
| `js/board/SvgGameboardLayer.js` | Future SVG definition layer |
| `js/board/GeometryLayer.js` | Future manifest observation layer |
| `js/model/PoolModel.js` | Future canonical multiplayer pool model |
| `js/controllers/Game1Controller.js` | Future Game 1 orchestration |
| `js/controllers/MenuController.js` | Future menu orchestration |

## Board truth resources

The site owns:

- `site/assets/playfield/game1_pub_options_background.jpeg`
- `site/assets/playfield/uniform_pick_card_gameboard.svg`
- `site/data/geometry/uniform_pick_card_gameboard_manifest.json`

Current visual checkpoint: background layer only.

Next visual checkpoint: render the SVG definition above the background, still without picks.

## Why this boundary exists

The legacy page accumulated rendering, storage, menu, and pick propagation code in one HTML file. The rebuild must prevent that pattern from recurring.

HTML is the shell. Modules own behavior.
