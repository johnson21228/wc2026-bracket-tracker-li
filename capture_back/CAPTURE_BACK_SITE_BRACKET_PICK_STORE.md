# Capture Back: Site Bracket Pick Store

## Summary

Adds a site-owned Game 1 bracket pick store contract.

## Decision

The bracket cell slot id is the storage key. Game 1 now has a single site data module that names every bracket pick slot and exposes one localStorage-backed runtime API:

- `wc2026.game1.bracketPicks`
- `window.WC2026_GAME1_BRACKET_PICK_STORE`
- `window.WC2026_GAME1_BRACKET_PICK_STORE_API`

## Boundary

This is still a static site. The site can define the storage contract and runtime API, but browser picks persist in `localStorage` unless a backend or export/import file workflow is added later.

## Evidence

- `site/data/game1_bracket_pick_store.js`
- `site/data/schema/game1_bracket_pick_store_schema.json`
- `site/game1/index.html`
- `tools/verify_wc2026_site_bracket_pick_store_patch.py`
