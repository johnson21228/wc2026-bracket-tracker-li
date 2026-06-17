# Card 122: Anchor Knockout Choice Menu Assignment

## Claim

A knockout choice menu assigns a selected team to the bracket cell that opened it.

## Problem

The menu can show the correct candidate teams but still feel detached from the bracket cell it is supposed to fill. Selection may fail if the active slot is stale or unclear.

Tooltips may also remain visible while the menu is open, creating competing surfaces.

## Decision

Implement an anchored knockout choice menu assignment rule:

- open the menu adjacent to the bracket cell
- close all tooltips when the menu opens
- store the opening cell as the assignment target
- write the chosen team directly into that cell

## Acceptance Criteria

- Tapping `L-R16-01` opens the menu beside `L-R16-01`.
- Menu subtitle identifies that the menu assigns the bracket cell.
- Tooltip surfaces close when the menu opens.
- Choosing a team writes that team into the opening cell.
- R16 assignment writes to `r16Picks[slotId]`.
- QF/SF/final assignment writes to `advancementPicks[slotId]`.
- Verifier confirms anchored menu markers and explicit assignment writes.

## Files

- `site/game1/index.html`
- `tools/verify_wc2026_anchored_knockout_choice_menu_patch.py`
- `capture_back/CAPTURE_BACK_ANCHORED_KNOCKOUT_CHOICE_MENU_ASSIGNMENT.md`
- `docs/features/anchored_knockout_choice_menu_assignment.md`
- `li/world_cup/anchored_knockout_choice_menu_assignment_rule.md`
- `prompts/verify_anchored_knockout_choice_menu_assignment.md`
