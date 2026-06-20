# WC2026 Supabase Shared-Pick SQL Target

## Status

This is the canonical Bracketeering Pub Supabase target **before any SQL is applied**.

It supersedes the earlier private-only `user_brackets` assumption and the earlier `status`-only table sketch.

## Product invariant

```text
WRITE is private.
READ can be shared when game rules allow it.
```

## Tables

### `public.profiles`

Purpose: provide public player identity for shared pick views without exposing raw `auth.users.email`.

Expected columns:

- `id uuid primary key references auth.users(id) on delete cascade`
- `display_name text`
- `avatar_url text`
- `created_at timestamptz not null default now()`
- `updated_at timestamptz not null default now()`

Display names are optional at first, but if present should be bounded to a reasonable length. Browser UI must never use raw auth email as the public player name.

### `public.user_brackets`

Purpose: store one canonical pick-state JSON document per signed-in player per game.

Expected columns:

- `user_id uuid not null references auth.users(id) on delete cascade`
- `game_id text not null check (game_id in ('game1', 'game2'))`
- `picks_json jsonb not null default '{}'::jsonb`
- `visibility text not null default 'private' check (visibility in ('private', 'public', 'room'))`
- `submitted_at timestamptz`
- `locked_at timestamptz`
- `created_at timestamptz not null default now()`
- `updated_at timestamptz not null default now()`
- `primary key (user_id, game_id)`

`picks_json` stores the canonical pick-state document defined by `docs/architecture/wc2026_canonical_pick_state_storage_model.md`. Supabase stores the document; it does not define bracket geometry, slot layout, or advancement rules.

## RLS target

Enable Row Level Security on both tables.

Profile policies:

- signed-in users can read display profiles
- signed-in users can insert only their own profile row
- signed-in users can update only their own profile row

Bracket policies:

- owner can read their own bracket at any time
- other signed-in users can read brackets when `visibility = 'public'`, `submitted_at is not null`, or `locked_at is not null`
- owner can insert only their own bracket rows
- owner can update only their own unsubmitted and unlocked bracket rows
- delete is omitted for MVP unless an explicit bracket reset/delete behavior is designed

## Frontend consequences

Card 216 should implement account-backed save/load against this contract, not the superseded private-only contract.

- Anonymous players continue using localStorage.
- Signed-in players save/load `game1` and later `game2` through `RemoteBracketStore`.
- Draft rows default to `visibility = 'private'`.
- Submit/lock behavior writes `submitted_at` and/or `locked_at`.
- Shared player pick views are future-gated UI work, but the schema and RLS must not block them.

## Security boundary

Never commit or expose:

- service role key
- database password
- direct Postgres connection string
- JWT secret

Allowed browser/runtime configuration:

- Supabase project URL
- Supabase anon/publishable key

The browser-safe key is only safe when RLS is enabled and correct.

<!-- CARD-227-CANONICAL-BRACKET-DOCUMENT-RUNTIME -->

## Card 227 runtime confirmation

The Pages runtime must use the canonical `BracketDocument` before Supabase persistence is introduced.

Required runtime fields are `schemaVersion`, `gameId`, `status`, `expectedPickCount`, `updatedAt`, and `picksBySlot`.

`CHAMPION` and `THIRD-PLACE-WINNER` are first-class runtime/model slots. Game 1 expected total: 64 picks. Game 2 expected total: 32 picks.

`user_brackets.picks_json` stores this same canonical `BracketDocument`; Supabase remains durable persistence only.

