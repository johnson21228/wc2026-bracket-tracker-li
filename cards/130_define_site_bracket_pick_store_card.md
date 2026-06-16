# Card 130: Define Site Bracket Pick Store

## Claim

Game 1 needs one site-owned bracket pick store that can hold every pick by bracket cell id.

## Invariant

The bracket cell is the storage key.

## Store

- Runtime key: `wc2026.game1.bracketPicks`
- Site module: `site/data/game1_bracket_pick_store.js`

## Acceptance Criteria

- Site data defines R32, R16, QF, SF, and center/final area slot ids.
- Game 1 loads the store module before runtime assignment code.
- Store API can get/set/clear picks by slot id.
- Legacy R32/R16/QF-SF localStorage buckets can be migrated into the unified store.
