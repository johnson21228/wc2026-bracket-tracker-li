# Card 155 — Route Game 1 Rendering Through Canonical Pick State Model

## Intent

Route Game 1 stored knockout rendering and patch/adornment reads through the canonical pick-state model introduced by Card 154.

This card must not rewrite menus.

## Background

Card 154 added:

```js
window.WC2026_GAME1_PICK_STATE
```

The next bug surface is rendering. Some render paths still read storage directly or use legacy mirrors. That allows stale R16/QF/SF picks to appear even when the canonical model should reject them.

## Required Rule

Rendering may not decide truth from localStorage, `r16Picks`, `advancementPicks`, or `window.game1KnockoutPicks`.

Rendering must ask the canonical model:

```js
window.WC2026_GAME1_PICK_STATE.getPick(slotId)
window.WC2026_GAME1_PICK_STATE.isPickValid(slotId)
```

## Required Scope

Patch only:

- stored knockout render bridge
- R16 stored render reads
- advancement stored render reads
- patch/adornment card relabel reads

Do not rewrite the menu system in this card.

## Acceptance Criteria

- Stored R16 rendering uses `WC2026_GAME1_PICK_STATE`.
- Stored QF/SF/Final/Champion rendering uses `WC2026_GAME1_PICK_STATE`.
- `patchStoredKnockoutCards` does not read localStorage directly.
- Patch/adornment code only patches labels for valid canonical picks.
- Existing R32 hit testing still works.
- Menu opening behavior is unchanged by this card.
- Verifier passes.

## Non-goals

- No menu rewrite.
- No new visual scrub.
- No new independent storage authority.
- No replacement of the entire bracket renderer.

## Next Card

Card 156 should route menu pickability/current-pick behavior through the canonical model if needed.
