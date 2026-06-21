# Capture Back: Center Final Four Visual Only

## Intent

Repair the center Final Four board rendering so the internal geometry slot ID does not appear as a player-facing pick slot.

## Problem

The `CENTER-FINAL-FOUR` geometry slot was being rendered like a normal pick-slot button. On the gameboard this exposed the internal label `CENTER-FINAL-FOUR` over the large center bracket box.

## Change

`CENTER-FINAL-FOUR` / `FINAL_FOUR` is now treated as visual-only geometry:

- it remains in the SVG/geometry authority
- it is excluded from MVC pick-slot button rendering
- it is excluded from the pick-surface slot count
- the visible center Final Four box remains part of the board linework/background

## Verification

`tools/verify_wc2026_center_final_four_visual_only.py` verifies that the slot is filtered out of pick-surface rendering.
