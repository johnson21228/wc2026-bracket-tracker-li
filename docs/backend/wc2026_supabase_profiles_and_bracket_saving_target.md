# WC2026 Supabase Profiles and Bracket Saving SQL Target

This is the reviewed SQL target for crossing from identity-only Supabase Auth into durable Bracketeering persistence.

## Tables

### `public.profiles`

Owns public player identity.

It stores:

- `id`
- `display_name`
- timestamps

It does not store auth email.

### `public.user_brackets`

Owns durable bracket documents.

It stores one canonical BracketDocument JSON row per:

- user
- tournament
- game

The pick abstraction remains unchanged. The canonical document continues to contain `picksBySlot`.

## RLS boundary

WRITE is private.

Users can write only:

- their own profile row
- their own bracket rows

READ can be shared later when game rules allow it.

The target includes a public-read policy for submitted/locked public bracket rows, but the default row visibility is `private`.

## Not included yet

This SQL target does not add:

- leaderboard views
- public pick comparison UI
- automatic anonymous-to-remote migration
- profile creation trigger on `auth.users`

Profile creation is intentionally client-driven at first, to avoid adding an auth trigger before the first persistence loop is tested.
