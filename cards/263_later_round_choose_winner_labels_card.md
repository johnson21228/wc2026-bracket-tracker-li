# Card 263: Later-round Choose Winner labels

## Goal

Make later-round empty bracket cells read as winner choices.

## Acceptance

- R32 empty cells retain “Choose Team.”
- R16 and later empty cells render “Choose Winner.”
- Runtime uses `playerFacingEmptyPickText(slot)`.
- No model/storage/pick ID changes.
