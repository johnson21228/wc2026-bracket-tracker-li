# Card 124: Apply Selection to Picked Cell

## Claim

When a user chooses a team from a knockout choice menu, the selected team must be applied to the bracket cell that opened the menu.

## Problem

The menu can display candidate teams, but display alone is incomplete. The menu selection must have a clear write target and must render the result in the bracket cell.

## Acceptance Criteria

- The menu has a target bracket cell.
- Selecting a team writes to the target cell's storage key.
- R16 targets write to `r16Picks[targetSlotId]`.
- QF/SF/final targets write to `advancementPicks[targetSlotId]`.
- Stored picks include `assignedSlotId` and `assignmentTargetSlotId`.
- The shared `window.game1KnockoutPicks` state is refreshed.
- `renderPicks()` is called after write.
- `closeMenu()` is called after render.
- A verifier protects the assignment markers.

## Manual Test

Tap `L-R16-01`, choose a team, and confirm that exact cell renders the chosen team.
