# R32 Pick Card Slot Fit Rule

A filled Round of 32 pick card must fit inside the pixel-defined space assigned to its bracket slot.

## Authority

The source board geometry and the slot `boundsPx` are the authority for visible pick-card placement and size.

A pick card may not expand across connector lines, neighboring slots, or source-board labels in order to fit large typography. If a name is long, the card must adapt the text, not the slot geometry.

## Required behavior

- The visible card left, top, width, and height must be derived from the slot `boundsPx`.
- The flag should be as large as the slot height allows while preserving padding and legibility.
- The team name should fit within the remaining horizontal space.
- The card should reduce text size before falling back to truncation.
- The compact card should remain team-first: flag plus team name.
- Slot rule text belongs in the tooltip/details surface, not as competing visible card text.

## Boundary

Board Geometry owns slot bounds.
Tournament Data owns the flag and team name.
Game 1/Game 2 owns pick state.
UI Surface owns fitting the visible card within the board-defined slot.
