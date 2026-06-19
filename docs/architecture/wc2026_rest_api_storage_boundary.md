# WC2026 Storage Boundary

The site is being factored to support two storage modes with the same canonical pick-state model.

## Static/local mode

```text
Browser
  → static JSON files
  → BracketRepository
  → LocalStorageBracketStore
  → localStorage user bracket records
```

## Account-backed mode

The current recommended first backend is Supabase, not a custom REST server.

```text
Browser
  → Supabase client using browser-safe anon/publishable key
  → Supabase Auth session
  → Row Level Security
  → public.user_brackets.picks_json
```

The browser talks directly to Supabase because RLS is the security boundary. A service role key, database password, direct Postgres URL, or JWT secret must never be committed or exposed to the browser.

## Superseded REST sketch

A later custom API/server remains possible, but it is not the current first path. Earlier `/api/users/:userId/bracket` sketches should be treated as conceptual storage-boundary notes, not the active implementation target.

## Active remote target

The active remote target is documented in:

- `docs/backend/wc2026_supabase_shared_pick_sql_target.md`
- `source/sql/wc2026_supabase_shared_pick_schema_draft.sql`
- `source/sql/wc2026_supabase_shared_pick_rls_draft.sql`

The UI should not need to change when the storage adapter changes. The storage boundary remains:

```text
UI picks
  ↓
Canonical complete pick-state document
  ↓
BracketRepository
  ↓
LocalStorageBracketStore OR RemoteBracketStore
```
