# Capture Back — Clean site module boundary

## Change

Established the module boundary for the clean WC2026 site.

## Added/updated clean site structure

- `site/new/index.html`
- `site/new/css/app.css`
- `site/new/css/board.css`
- `site/new/js/app.js`
- `site/new/js/services/assetPaths.js`
- `site/new/js/services/domMounts.js`
- `site/new/js/board/BoardShell.js`
- `site/new/js/board/BackgroundLayer.js`
- placeholder module directories:
  - `site/new/js/model/`
  - `site/new/js/controllers/`

## Added governance

- `cards/158_establish_clean_site_module_boundary_card.md`
- `li/world_cup/clean_site_module_boundary_rule.md`
- `docs/architecture/wc2026_clean_site_module_boundary.md`
- `tools/verify_wc2026_clean_site_module_boundary.py`

## Boundary

`site/new/index.html` is shell-only.

Board rendering now lives in modules. Current render layer remains background-only while the SVG and manifest are held as truth resources for follow-up layers.
