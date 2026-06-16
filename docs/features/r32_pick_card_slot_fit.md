# R32 Pick Card Slot Fit

This feature prevents filled Round of 32 pick cards from visually escaping the gameboard-defined bracket slot.

The card should be constrained to the slot rectangle, with the flag using the available vertical height and the team name fitted into the remaining width. This keeps the bracket readable and preserves the gameboard as the geometry authority.

Expected result:

- cards no longer stretch across bracket connectors
- flags are vertically prominent within the card
- names such as `Ivory Coast` and `South Korea` fit without crowding neighboring slots
- extended rule text remains in tooltip/details UI rather than the compact card
