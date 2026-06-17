# Card 127: Replace Stacked Knockout Assignment Wrappers

## Claim

The Game 1 knockout menu must have a single write/render authority.

## Problem

Multiple wrappers were competing to handle the same menu selection path, making it unclear whether the rendered team tile click was writing through the final storage/render path.

## Decision

Replace the stacked wrappers with `WC2026_KNOCKOUT_ASSIGNMENT_SURFACE`.

## Acceptance

- R16 menu opens beside the source cell.
- Team selection writes `r16Picks[slotId]`.
- QF/SF selection writes `advancementPicks[slotId]`.
- The selected cell re-renders immediately.
- Refresh preserves the selected knockout pick.
- Old competing wrapper markers are absent.
