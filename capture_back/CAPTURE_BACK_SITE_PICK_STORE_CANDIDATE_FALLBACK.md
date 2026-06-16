# Capture Back: Site Pick Store Candidate Fallback

## Summary

Repair the Game 1 R16 menu candidate source after introducing the unified site bracket pick store.

## Decision

The unified site bracket pick store is preferred, but it must not make existing R32 picks invisible. R16 candidate resolution now checks the unified store, legacy R32 localStorage, current runtime `picks`, and manifest alias IDs.

## Evidence

- `site/game1/index.html`
- `tools/verify_wc2026_site_pick_store_candidate_fallback_patch.py`
