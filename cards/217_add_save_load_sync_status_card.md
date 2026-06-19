# Card 217: Add Save/Load/Sync Status and Local-to-Account Migration

## Intent

Make the storage mode understandable to players and protect local picks during sign-in.

## Scope

- Saved/unsaved state
- Local draft / account draft state
- Load from account
- Save local picks to account
- Keep local only
- Conflict messaging when local and account drafts both exist

## Acceptance

- Signing in does not silently erase local picks.
- The player can intentionally choose whether to save local picks or load account picks.
- Save status is visible.
