# Single Game Admin_/official Runtime

This cleanup reconciles stale two-game presentation code with the current Bracketeering model.

- One persisted game id: `game1`.
- Legacy `game-2` means only “show the bracket board”.
- Admin_/official owns R32 occupants in a public locked/submitted Supabase row.
- Players cannot edit R32 occupants.
- Player picks use the existing dependency-map winner path after R32 is hydrated.
- Missing official R32 authority fails closed for players.
- Missing official R32 authority does not blank the signed-in admin editor; the connected admin can create the row.
