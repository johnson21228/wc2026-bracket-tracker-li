# Supabase identity UI surface rule

Bracketeering may include an upper-right identity/status surface, but it must remain a thin site-owned shell around Supabase Auth.

## Rule

The site must not implement custom authentication or a full profile system. Supabase owns authentication, session state, `auth.uid()`, Postgres persistence, and RLS enforcement.

The site owns only the visible identity/status surface:

- sign-in button placement
- signed-in display label
- save status
- bracket status: draft / submitted / locked
- sign-out action
- optional local-to-account import prompt

## Runtime invariant

Same `BracketDocument`. Different store.

Signed out:

```text
BracketRepository → LocalStorageBracketStore
```

Signed in:

```text
BracketRepository → SupabaseBracketStore
```

Board views and pick controllers must not know whether persistence is localStorage or Supabase.

## Non-goals

- no custom auth
- no full account-management surface
- no public player-pick views yet
- no raw auth email as public display identity
- no direct Supabase calls from board/menu/controller code
- no Supabase-owned View or Controller behavior
