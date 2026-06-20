# Canonical BracketDocument Runtime Rule

Bracketeering runtime must use the canonical `BracketDocument` shape before Supabase persistence is introduced.

Required fields:

- `schemaVersion`
- `gameId`
- `status`
- `expectedPickCount`
- `updatedAt`
- `picksBySlot`

The durable slot model must include first-class `CHAMPION` and `THIRD-PLACE-WINNER` slots.

Game 1 expected pick count is 64 when R32 entrant picks and all winner picks, including third-place winner, are stored.

Game 2 expected pick count is 32 when R32 entrants are fixed/given and only winner picks, including third-place winner, are stored.

Supabase stores this document later in `user_brackets.picks_json`; Supabase does not own View, Controller, geometry, pick menus, or advancement logic.

## Card 228 same document different store rule

The runtime must use the same canonical `BracketDocument` for local anonymous play and future signed-in persistence. LocalStorage and Supabase are different stores, not different game models.
