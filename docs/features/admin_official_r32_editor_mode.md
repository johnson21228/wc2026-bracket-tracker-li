# Admin official R32 editor mode

## Invariant

Only Admin_/official may edit R32 occupant slots.
All players mirror Admin_/official R32 occupant truth.

## Rule

R32 occupant slots are official truth fields, not normal player picks. The public player board continues to hydrate R32 from the Supabase `Admin_/official` bracket document and refuses normal player R32 authoring.

A separate explicit Admin_/official editor mode may reopen R32 slot menus for the official row only:

- `?adminOfficialR32Editor=1` enables Admin_/official R32 editor mode.
- In that mode, R32 choices are available so the official truth document can be authored.
- R32 edits are written to the Supabase `Admin_/official` row with `bracket_kind = official`.
- The saved records are R32 entrant records with `source = Admin_/official` and `authority = Admin_/official`.
- Normal players still cannot edit R32 slots.
- Normal players continue to see exactly the Admin_/official R32 truth, including partial truth.

## Non-goals

- Do not allow normal players to author R32.
- Do not let static JSON or localStorage masquerade as public R32 truth.
- Do not change player-owned R16++ picks.
- Do not create a broad admin dashboard.

## Expected behavior

Admin_/official authors R32.
Players mirror R32.
Players author R16++.
