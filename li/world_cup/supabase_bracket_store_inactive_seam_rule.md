# SupabaseBracketStore inactive seam rule

`SupabaseBracketStore` may exist before it is activated.

Its presence is not a release signal.

## Runtime posture

The public Pages runtime remains local/browser-store active by default.

`SupabaseBracketStore` must not be imported by public runtime entrypoints until an explicit activation CB.

`BracketRepository` must not default to the Supabase store yet.

## Store contract

`SupabaseBracketStore` must implement:

- `loadUserBracket(userId)`
- `saveUserBracket(bracketDocument)`

The store targets `user_brackets`.

The store reads and writes `picks_json`.

The store saves the full canonical `BracketDocument`.

The store uses one row per signed-in `user_id,game_id`.

The upsert conflict target is `user_id,game_id`.

## Error contract

Remote load/save failures must throw explicit errors.

A failed remote save must not be treated as a successful contest save.

## Architecture boundary

View and Controller code must not call Supabase directly.

Supabase persistence belongs behind the store/repository/session seam.

## External boundary

This rule does not apply Supabase SQL.

This rule does not change Supabase dashboard state.

This rule does not merge to `main`.
