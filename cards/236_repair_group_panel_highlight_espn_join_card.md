# Card 236: Repair group panel highlight join by ESPN match ID

## Status

Ready to apply.

## Why

The live site data is correct, but the group panel did not render newly captured highlight links because the model joined highlights by Workbench `matchId` only.

## Change

Patch `site/js/mvc/model.js` so `getMatchHighlights` accepts a full match record and checks `match.espnMatchId` first, then falls back to `match.matchId`.

## Verification

Add `tools/verify_wc2026_group_panel_highlight_espn_join.py` and wire it into `make verify`.
The verifier checks:

- the model uses `match.espnMatchId` before `match.matchId` fallback;
- the stale `getMatchHighlights(match.matchId)` caller is gone;
- the four June 20/21 ESPN IDs exist in match and highlight data;
- `make verify` runs the dedicated verifier.
