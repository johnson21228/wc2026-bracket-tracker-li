# Card 1006 — Replace persistent local storage pill with account save action target

## Intent

Make account-backed persistence a first-class product action without making remote storage the live gameplay engine.

## Product rule

Gameplay remains local-first:

- every pick updates local browser state immediately
- normal play does not write to Supabase on every pick
- account persistence is an explicit `Save Picks` action
- no always-visible `Playing locally` pill
- no local-to-remote migration yet
- no load/overwrite behavior yet

## Scope

- Remove the persistent local storage status pill.
- Add a compact account save action target near the login/account chrome.
- Show `Save Picks` as the product affordance.
- Wire the action to one explicit Supabase `saveUserBracket` call for signed-in users.
- Preserve hidden dev Supabase remote test mode.
- Keep View and Controller free of Supabase bracket persistence calls.

## Verification

- `tools/verify_wc2026_account_save_action_target.py`
- Save Picks performs one explicit account save and does not load/overwrite local picks.
- full `make verify`
- `make pack`


## Signed-in persistence refinement

Make signed-in account persistence the primary save/load surface:

- signed out remains local-only until login
- signed in checks for saved account picks
- if no local picks exist, saved account picks may load automatically
- if local picks exist too, the UI shows explicit `Load Saved`
- no silent overwrite of local picks
- Save Picks remains an explicit account write
