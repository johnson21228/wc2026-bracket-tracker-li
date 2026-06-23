# Capture Back: Supabase Profiles and Bracket SQL Applied

## Status

Applied in Supabase dashboard SQL Editor.

## Tables verified

- `public.profiles`
- `public.user_brackets`

## Current `public.user_brackets` shape

- `id uuid`
- `user_id uuid`
- `tournament_id text`
- `game_id text`
- `bracket_json jsonb`
- `visibility text`
- `status text`
- `created_at timestamptz`
- `updated_at timestamptz`

## Policy cleanup

Removed older draft `profiles` policies:

- `profiles_insert_own`
- `profiles_select_authenticated`
- `profiles_update_own`

## Final policy target

Profiles:

- public read of player display identity
- owner-only insert/update/delete

User brackets:

- owner-only read/insert/update/delete
- public read only for submitted/locked rows with `visibility = 'public'`

## Notes

An older empty draft `public.user_brackets` table using `picks_json` existed in Supabase. It had zero rows and was dropped before applying the canonical `bracket_json` target.
