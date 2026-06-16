# Card 131: Use Site Pick Store to Hold and Render Bracket Choices

## Claim

The site bracket pick store should be used to hold and render choices for R16 and later bracket cells.

## Rule

- `li/world_cup/use_site_pick_store_render_rule.md`

## Acceptance Criteria

- `site/data/game1_bracket_pick_store.js` is loaded by Game 1.
- Menu selections write to `wc2026.game1.bracketPicks[slotId]`.
- R16 rendering reads from the unified site pick store first.
- QF/SF rendering reads from the unified site pick store first.
- Legacy R32/R16/QF/SF localStorage buckets remain migratable.
- A verifier protects the store/render contract.
