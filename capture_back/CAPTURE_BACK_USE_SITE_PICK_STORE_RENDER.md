# Capture Back: Use Site Bracket Pick Store to Hold and Render Choices

## Summary

Game 1 now uses the site-owned bracket pick store as the first-class place to hold and render bracket selections.

## Decision

The bracket cell remains the storage key. Menu choice, R16 rendering, and later-round rendering use `wc2026.game1.bracketPicks` first, while legacy buckets remain as compatibility mirrors.

## Evidence

- `site/data/game1_bracket_pick_store.js`
- `site/game1/index.html`
- `tools/verify_wc2026_use_site_pick_store_render_patch.py`

## Invariant

A visible bracket selection must be recoverable from the site bracket pick store by slot id.
