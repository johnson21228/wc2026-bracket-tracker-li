# WC2026 Supabase Shared-Pick SQL Target

## Status

This is the canonical Bracketeering Pub Supabase target **before any SQL is applied**.

It is now finalized against:

- Card 227 canonical `BracketDocument` runtime
- Card 228 `BracketDocument` save seam before Supabase
- Card 229 SQL/RLS finalization

The SQL remains a draft file until it is intentionally applied in the Supabase dashboard and captured as dashboard evidence.

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

Purpose: store one canonical `BracketDocument` per signed-in player per game.

Expected columns:

- `user_id uuid not null references auth.users(id) on delete cascade`
- `game_id text not null check (game_id in ('game1', 'game2'))`
- `picks_json jsonb not null`
- `visibility text not null default 'private' check (visibility in ('private', 'public', 'room'))`
- `submitted_at timestamptz`
- `locked_at timestamptz`
- `created_at timestamptz not null default now()`
- `updated_at timestamptz not null default now()`
- `primary key (user_id, game_id)`

`picks_json` stores the same canonical `BracketDocument` used by the Pages runtime and localStorage save seam. Supabase stores the document; it does not define bracket geometry, slot layout, menu rules, controller behavior, or advancement rules.

Required top-level `picks_json` fields:

- `schemaVersion`
- `gameId`
- `status`
- `expectedPickCount`
- `updatedAt`
- `picksBySlot`

The SQL target checks that `picks_json.gameId` matches the row `game_id`, and that the document status is one of `draft`, `submitted`, or `locked`.

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
- owner can update only their own existing unlocked bracket rows
- delete is omitted for MVP unless an explicit bracket reset/delete behavior is designed

## Submit/lock update correction

The owner update policy must not require `submitted_at is null` and `locked_at is null` in `WITH CHECK`.

That older shape blocks the normal lifecycle update that sets `submitted_at` or `locked_at`.

The finalized shape is:

```text
USING: owner may update their own existing row while old locked_at is null
WITH CHECK: resulting row must still belong to the same owner
```

A database trigger enforces finality:

- if the old row is locked, no update is allowed
- if the old row is already submitted, `picks_json`, `user_id`, and `game_id` cannot change
- if `locked_at` is set while `submitted_at` is null, the trigger fills `submitted_at`

This lets the browser perform normal draft save, submit, and lock transitions while preventing post-finality bracket rewriting.

## Frontend consequences

Card 216 should implement account-backed save/load against this contract, not the superseded private-only contract.

- Anonymous players continue using localStorage.
- Signed-in players save/load `game1` and later `game2` through `SupabaseBracketStore` behind the repository seam.
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

## Sequencing

```text
Runtime BracketDocument: complete
Local save seam: complete
SQL/RLS finalization: this card
Supabase dashboard apply: next explicit step
SupabaseBracketStore: after SQL apply
```
