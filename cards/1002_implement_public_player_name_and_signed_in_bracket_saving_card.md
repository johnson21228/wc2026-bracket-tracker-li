# Card 1002: Implement public player name and signed-in bracket saving

## Context

Supabase Auth now works end-to-end.

The site has a signed-in identity UI, but it is still identity-only:

- Supabase Auth identifies the signed-in user.
- Anonymous/local play still uses browser local storage.
- Remote bracket writes are not enabled.
- Public player names are not yet stored.

The next implementation step is to add durable Supabase-backed player identity and bracket persistence.

## Product target

Signed-in Bracketeering players should be able to:

1. Set a public player name.
2. Save their bracket to Supabase.
3. Reload the site and recover their bracket from Supabase.
4. Keep anonymous local play working when signed out.

Later, players should be able to view other players’ picks when game rules allow.

## Data model target

Use two Supabase-owned model surfaces:

### profiles

Purpose:

- public player identity
- display name for shared picks / leaderboards
- avoid exposing raw auth email as public identity

Core fields:

- `id uuid primary key references auth.users(id)`
- `display_name text`
- `created_at timestamptz`
- `updated_at timestamptz`

### user_brackets

Purpose:

- durable bracket document storage
- one row per user / tournament / game
- JSON document storage for the canonical BracketDocument

Core fields:

- `id uuid`
- `user_id uuid references auth.users(id)`
- `tournament_id text`
- `game_id text`
- `bracket_json jsonb`
- `visibility text`
- `status text`
- `created_at timestamptz`
- `updated_at timestamptz`
- unique `(user_id, tournament_id, game_id)`

## Architecture boundary

Do not change the site’s abstraction to game data or picks.

The following remain conceptually unchanged:

- `BracketDocument`
- `picksBySlot`
- pick write pipeline
- R32 pick controller
- knockout pick controller behavior
- static match/team/bracket data
- anonymous local play

Add persistence behind existing seams.

## Proposed client seams

### AuthService

Already exists.

Responsible for:

- signed-in session
- private account email
- user id

### ProfileStore / SupabaseProfileStore

New seam.

Responsible for:

- read current user profile
- create/update public display name
- expose display name to the identity UI

### BracketStore / SupabaseBracketStore

Remote persistence seam.

Responsible for:

- save canonical BracketDocument for signed-in user
- load canonical BracketDocument for signed-in user
- do not own profile editing
- do not own view/controller behavior

## Core invariant

WRITE is private.

A signed-in user can write only:

- their own profile row
- their own bracket row

READ can be shared later when game rules allow it.

Initial implementation may keep shared reads disabled until public-picks UI is ready.

## UX target

When signed in and no public player name exists:

- prompt the user to enter a public player name
- explain that this is what other players may see later
- do not use email as public player name

When signed in and profile exists:

- show public player name in identity panel
- show account email as private login identity
- show bracket save/load status

When signed out:

- keep anonymous local play
- keep browser-local bracket behavior

## Acceptance checks

- Anonymous/local play still works when signed out.
- Supabase Auth sign-in/sign-out still works.
- Signed-in user can set/update public player name.
- Public player name is stored in Supabase profile data, not local-only state.
- Email is not shown as public player name.
- Signed-in user can save/load their bracket document from Supabase.
- Bracket save/load uses canonical BracketDocument shape.
- `picksBySlot` remains unchanged.
- Pick write pipeline remains unchanged.
- No automatic migration from anonymous local play to remote play occurs unless explicitly added later.
- RLS prevents users from writing other users’ profiles or brackets.
- `make verify` passes.
- `make pack` passes.
