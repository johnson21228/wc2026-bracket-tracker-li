# SupabaseBracketStore inactive seam

`SupabaseBracketStore` is now implemented as a service module, but it is not active in public runtime.

The public Pages app still defaults to local/browser storage.

## Implemented module

`site/js/services/SupabaseBracketStore.js`

Exports:

- `SupabaseBracketStore`
- `createSupabaseBracketStore`

Store methods:

- `loadUserBracket(userId)`
- `saveUserBracket(bracketDocument)`

## Persistence target

The store targets the canonical Supabase `user_brackets` table.

It writes one row per signed-in player/game:

- `user_id`
- `game_id`
- `picks_json`
- `visibility`

`picks_json` stores the full canonical `BracketDocument`.

The upsert conflict target is `user_id,game_id`.

## Inactive boundary

This implementation is intentionally inactive.

It is not imported by:

- `site/js/app.js`
- `site/js/services/BracketRepository.js`
- `site/js/mvc/view.js`
- `site/js/controllers/Game1R32PickController.js`

`BracketRepository` remains local-store active by default.

## Safety boundary

This work does not apply Supabase SQL.

This work does not change Supabase dashboard state.

This work does not switch public Pages to remote persistence.

This work does not merge to `main`.

View and Controller code must not call Supabase directly.
