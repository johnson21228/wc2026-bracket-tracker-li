# Card 039 — Create GitHub Pages Site Surface

## Intent

Create a clean deployable `site/` folder for the WC2026 bracket game site and stop using stale root HTML as the public surface.

## Changes

- Create `site/index.html` as a landing page.
- Create `site/game1/index.html` from the current Game 1 playfield.
- Create `site/game2/index.html` from the latest Game 2 bracket tracker release.
- Copy runtime dependencies into `site/assets/` and `site/data/`.
- Remove stale root `index.html` and root `game1_playfield.html`.
- Update verifier and Makefile for site-first deployment hygiene.
- Open the generated site pages after apply on macOS.

## Verification

`make verify` must pass and confirm the deployable entrypoints under `site/`.
