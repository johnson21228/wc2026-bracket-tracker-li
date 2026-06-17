# WC2026 Bracket Tracker LI

Modular World Cup 2026 bracket game site and Workbench LI repo.

This repo currently preserves two separate game surfaces:

- `index.html` — main bracket tracker / Game 2 knockout bracket surface
- `game1_playfield.html` — Game 1 Round of 32 chooser playfield

The repo is intentionally modular-source-first: HTML entry points, JavaScript, JSON data, source evidence, cards, LI rules, tests, and release snapshots are kept together so the game can evolve through Capture Back without losing intent. Static hosting is a deployment property, not a page-concentrated source architecture goal.

## Verify

```bash
make verify
```

## Pack

```bash
make pack
```

The pack target excludes generated packs, Git internals, macOS metadata, and applied overlay working directories.

## Hygiene expectation

Applied overlay folders should not remain at the repo root. Capture Back records belong under `capture_back/`, cards under `cards/`, feature notes under `docs/features/`, rules under `li/`, and release snapshots under `releases/`.

## Deployable Site Surface

The public website lives in `site/` so the repo root can remain the Workbench / LI control surface.

- `site/index.html` — public landing page
- `site/game1/index.html` — Game 1 Round of 32 chooser board
- `site/game2/index.html` — Game 2 bracket tracker
- `site/assets/` and `site/data/` — site-local runtime dependencies

Preferred GitHub Pages deployment is to publish `site/` through GitHub Actions.
