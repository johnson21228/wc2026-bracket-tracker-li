# Card 154 — Implement Game 1 Canonical Pick State Model

## Intent

Implement the canonical JavaScript model for Game 1 pick state before making further UI, rendering, menu, highlight, or persistence changes.

This card follows:

- `li/world_cup/game1_pick_state_model_first_rule.md`
- `li/world_cup/game1_pick_state_authority_rule.md`
- `cards/152_consolidate_game1_pick_state_authority_card.md`
- `cards/153_capture_game1_pick_state_model_first_insight_card.md`

## Problem

Game 1 currently has several overlapping pick stores and render wrappers. The page can render stale R16/QF/SF picks because downstream render paths can read old stored values without validating feeder picks.

The code has partial state APIs, but it does not yet have one canonical model that owns:

- pick storage
- pick validity
- slot pickability
- renderable picks
- clear/reset behavior

## Required Model

Implement a canonical model exposed as:

```js
window.WC2026_GAME1_PICK_STATE = {
  load,
  save,
  clear,
  getPick,
  setPick,
  clearPick,
  getSourceSlotIds,
  isPickValid,
  isSlotPickable,
  getRenderablePicks,
  inspect
};
```

## Canonical Storage

Canonical storage key:

```text
wc2026.game1.bracketPicks
```

Legacy stores may be read for migration or written as compatibility mirrors, but they must not remain independent authorities.

Legacy/mirror stores include:

- `wc2026.game1.r32.picks`
- `wc2026.game1.r16.winnerPicks`
- `wc2026.game1.qfSf.winnerPicks`
- `wc2026.game1.knockoutPicks`
- `picks`
- `r16Picks`
- `advancementPicks`
- `window.game1KnockoutPicks`

## Pick Data Shape

Each canonical pick should include:

```json
{
  "slotId": "L-R16-01",
  "round": "R16",
  "teamId": "USA",
  "abbr": "USA",
  "name": "United States",
  "flagEmoji": "🇺🇸",
  "sourceSlotIds": ["L-R32-01", "L-R32-02"],
  "pickedAt": "2026-06-16T23:45:00-04:00",
  "storeContract": "wc2026-game1-canonical-pick-state-v1"
}
```

Required fields:

- `slotId`
- `round`
- team identity: `teamId`, `abbr`, `name`, `flagEmoji`
- `sourceSlotIds` for downstream picks

## Validity Rules

R32 picks are valid if they contain a team.

Downstream picks are valid only if all feeder picks exist and are valid.

- R16 requires both source R32 picks.
- QF requires both source R16 picks.
- SF requires both source QF picks.
- Final / Champion requires feeder picks.

## Required Implementation Phases

### Phase 1 — Add the model without rerouting UI

Add the model in JS and expose it as `window.WC2026_GAME1_PICK_STATE`.

The model should:

- load canonical state
- normalize existing legacy state into canonical shape
- save canonical state
- validate downstream picks
- return renderable picks
- clear all canonical and mirror state

Do not change R32 hit testing in this phase.

### Phase 2 — Add verifier

Add:

```text
tools/verify_wc2026_game1_canonical_pick_state_model.py
```

Verifier should require:

- model marker exists
- `WC2026_GAME1_PICK_STATE` exists
- required API function names exist
- canonical storage key exists
- downstream validity functions exist
- short-term R16 hardcoded hold is disabled or absent
- no new late DOM scrub is introduced

### Phase 3 — Manual model test hook

Expose debug helpers:

```js
window.WC2026_GAME1_PICK_STATE.inspect()
window.WC2026_GAME1_PICK_STATE.clear()
```

## Acceptance Criteria

After this card:

- `window.WC2026_GAME1_PICK_STATE` exists.
- Model can load current picks from canonical storage.
- Model can clear all Game 1 pick state.
- Model can answer whether a slot is pickable.
- Model can answer whether a stored downstream pick is valid.
- Model can return renderable picks without stale R16/QF/SF data.
- Existing R32 hit testing still works.
- Verifier passes.
- No UI/rendering refactor is required yet, except enough to expose the model safely.

## Non-goals

Do not yet rewrite all rendering.

Do not yet rewrite all menus.

Do not add another visual scrub.

Do not add another `renderPicks` wrapper unless it is explicitly part of model exposure and verifier-guarded.

## Next Card

After this model exists and verifies:

```text
Card 155 — Route Game 1 Rendering Through Canonical Pick State Model
```
