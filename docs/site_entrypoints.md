# WC2026 Site Entrypoints

The deployable website lives under `site/`.

## Public pages

- `site/index.html` — public landing page for the bracket games.
- `site/game1/index.html` — Game 1 Round of 32 chooser board.
- `site/game2/index.html` — Game 2 bracket tracker surface.

## Runtime dependencies

The site folder carries its own runtime dependencies:

- `site/assets/` — images and visual assets required by site HTML.
- `site/data/` — JSON data required by current or future site HTML.

Root-level HTML files are not deployment entrypoints. In particular, stale root `index.html` and loose root `game1_playfield.html` should not be used as the public site surface.

## GitHub Pages posture

Preferred deployment posture is to publish the `site/` folder through GitHub Actions. This keeps the Workbench repo root available for LI, cards, capture-back records, source material, tools, and history while keeping the public website small and explicit.

- Game 1 middle layer: `site/assets/playfield/r32_bracket_geometry_overlay.png` is the live geometry-only alpha overlay.

## GitHub Pages root redirect shim

GitHub Pages may require a root `index.html` for branch-root publishing. In that case, the root page is only a redirect shim to `site/`. Runtime CSS, JavaScript, data, and assets remain governed by `site/`.
