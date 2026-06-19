# TODO: Repair Bracketeering Pub Export Completeness

## Problem

The Bracketeering Pub export path must export every pick the site knows about, not just a partial active pick object.

Observed user export:

- Filename: `braketeering-pub-picks-2026-06-19.json`
- App id: `wc2026.braketeeringPub.picks`
- Exported 43 picks total.
- R32 appears complete: all 32 R32 slots are present.
- Later knockout rounds are incomplete: only some R16/QF/SF picks appear.

This means the immediate issue is not that R32 export is half-empty. The export has all R32 picks, but it does not reliably include all later-round picks shown on the board.

## Suspected Cause

The current export path appears to serialize only the active MVC pick object. The site has used multiple durable pick stores during Game 1 development, including R32, R16, QF/SF, knockout, projection, and clean MVC stores.

Do not assume the visible board state and `wc2026.game1.cleanMvcPicks.v1` are identical.

## Acceptance Criteria

- Export filename uses `bracketeering`, not `braketeering`.
- Export app id uses `wc2026.bracketeeringPub.picks`, not `wc2026.braketeeringPub.picks`.
- Export includes every pick the site currently knows about.
- Export does not drop later-round picks that are visible on the board.
- Export merges or normalizes picks from all known Game 1 pick stores, including at minimum:
  - `wc2026.game1.cleanMvcPicks.v1`
  - `wc2026.game1.bracketPicks`
  - `wc2026.game1.r32.picks`
  - `wc2026.game1.r16.winnerPicks`
  - `wc2026.game1.qfSf.winnerPicks`
  - `wc2026.game1.knockoutPicks`
  - `wc2026.game1.r32ProjectionPicks.v1`
- Export includes a summary section with counts such as:
  - `exportedPickCount`
  - `activeMvcPickCount`
  - optional per-round counts: `r32`, `r16`, `qf`, `sf`, `final`, `champion`
- Verification fails if filename or app-id spelling regresses.
- Verification includes a localStorage fixture/simulation proving export merges all known pick stores into one stable export shape.

## Likely Files

- `site/js/mvc/controller.js`
- `site/js/mvc/model.js`
- `site/data/game1_bracket_pick_store.js`
- `tools/verify_wc2026_pub_hero_header.py`
- Possible new verifier:
  - `tools/verify_wc2026_export_all_picks.py`

## Implementation Notes

The export should collect all durable pick records that the site can use or display, normalize them to a stable `slotId: teamId` shape, then serialize that merged result.

The implementation should prefer the active MVC/current board state when duplicate slot ids exist, but it should not discard valid picks from legacy or auxiliary stores when those stores are still part of the current display/runtime path.

## Priority

High. This affects user trust in the export feature because the page can show picks that are not preserved in the exported file.
