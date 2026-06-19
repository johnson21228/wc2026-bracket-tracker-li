# Card 216: Implement Supabase Remote Bracket Store

## Intent

Connect signed-in users to hosted bracket storage using the canonical pick-state document and the shared-pick SQL target from Card 215.

## Scope

- Supabase client setup using browser-safe configuration only
- auth session read/write
- save/load `game1` and `game2` bracket documents through `public.user_brackets.picks_json`
- default draft rows to `visibility = 'private'`
- keep localStorage fallback for anonymous/local play
- no custom server
- no service role key, database password, direct Postgres URL, or JWT secret in the repo

## Remote store contract implications

`RemoteBracketStore` should treat Supabase as a document store for the canonical pick-state JSON:

- `loadGameState(gameId)` reads the current user's row for `game1` or `game2`.
- `saveGameState(gameId, pickState)` upserts the current user's row while it is unsubmitted and unlocked.
- `submitGameState(gameId)` sets `submitted_at` and prevents normal further edits.
- shared-read queries are intentionally deferred or feature-gated, but the client must not assume remote rows are private forever.

## Acceptance

- A signed-in user can save Game 1 and Game 2 pick states.
- A signed-in user can reload from another browser/device and recover picks.
- Anonymous local play still works.
- Remote save/load targets the Card 215 schema: `profiles`, `user_brackets`, `visibility`, `submitted_at`, and `locked_at`.
- Shared player pick views remain future UI work, but the implementation does not block them.
