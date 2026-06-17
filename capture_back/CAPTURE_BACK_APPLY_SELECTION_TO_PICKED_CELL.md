# Capture Back: Apply Selection to Picked Cell

## Summary

Captured the runtime rule that a choice menu selection must be applied to the bracket cell that opened the menu.

## Decision

A knockout choice menu is an assignment surface. The opened bracket cell is the target. Selecting a team writes the selected team into that exact cell's storage, refreshes the shared knockout pick state, re-renders the pick layer, and closes the menu.

## Scope

- R16 selections write to `r16Picks[targetSlotId]`.
- Later knockout selections write to `advancementPicks[targetSlotId]`.
- Stored picks include `assignedSlotId` and `assignmentTargetSlotId`.
- Rendering is required after storage.

## Evidence

- `site/game1/index.html`
- `tools/verify_wc2026_apply_selection_to_picked_cell_patch.py`
