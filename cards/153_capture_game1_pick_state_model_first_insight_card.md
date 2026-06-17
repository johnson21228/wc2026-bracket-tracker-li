# Card 153 — Capture Game 1 Pick State Model-First Insight

## Intent

Capture the architectural insight from the stale R16/QF/SF rendering problem:

Game 1 must be repaired model-first. UI and rendering must derive from canonical pick state, not from scattered localStorage keys or render wrappers.

## Background

The site accumulated multiple stores:

- `wc2026.game1.r32.picks`
- `wc2026.game1.r16.winnerPicks`
- `wc2026.game1.qfSf.winnerPicks`
- `wc2026.game1.knockoutPicks`
- `wc2026.game1.bracketPicks`
- `picks`
- `r16Picks`
- `advancementPicks`
- `window.game1KnockoutPicks`

This created stale downstream state. R16/QF/SF render paths could find old stored picks and render them even after Clear picks or after feeder picks were missing.

## Captured Insight

Build the data model first.

Then make UI, rendering, menus, highlights, and Clear picks obey the model.

## Required Rule

No downstream pick may render, highlight, or become pickable unless its feeder picks exist and are valid.

## Next Implementation Card

Create a follow-up code card to introduce:

```js
window.WC2026_GAME1_PICK_STATE
```

with:

- `load`
- `save`
- `clear`
- `getPick`
- `setPick`
- `clearPick`
- `getSourceSlotIds`
- `isPickValid`
- `isSlotPickable`
- `getRenderablePicks`

## Acceptance Criteria

This card is complete when the LI rule, feature doc, and card exist and future work can cite them before changing Game 1 pick/render/menu behavior.
