# Bracketeering Supabase identity UI surface

## Summary

Bracketeering should have an upper-right identity/status surface, but it should remain a thin site-owned shell around Supabase Auth.

The site is not building a custom or fancy login system. Supabase owns authentication, sessions, `auth.uid()`, and the secure link to Postgres RLS.

The site owns the visible surface that tells the player whether the current bracket is anonymous/local or signed-in/Supabase-backed.

## UI placement

```text
Top-left:  Bracketeering Pub / game title / navigation
Center:    Game board
Top-right: Identity/status surface
```

## Initial states

Anonymous state:

```text
[Sign in to save]
```

Signed-in draft state:

```text
Steve ▼
Saved
Draft
```

Signed-in submitted state:

```text
Steve ▼
Submitted
```

Signed-in locked state:

```text
Steve ▼
Locked
```

## Data purpose

The identity surface exists to prove this data path:

```text
User signs in
→ Supabase Auth provides current user id
→ site loads or creates that user’s canonical BracketDocument
→ user makes a pick
→ BracketRepository.save(document)
→ SupabaseBracketStore.save(document)
→ user_brackets.picks_json
→ reload restores the same BracketDocument
```

## Store routing

Same `BracketDocument`. Different store.

Signed out:

```text
BracketRepository → LocalStorageBracketStore
```

Signed in:

```text
BracketRepository → SupabaseBracketStore
```

The board and pick controllers should not know which store is active.

## What Supabase owns

- sign up / sign in
- session state
- current authenticated user
- `auth.uid()`
- Postgres tables
- RLS policies
- the profile row used for public display name

## What the site owns

- upper-right sign-in/status placement
- display of signed-in identity label
- display of save status
- display of bracket status: draft / submitted / locked
- sign-out action
- optional local-to-account import prompt
- messaging that explains local vs signed-in persistence

## Explicit non-goals

- Do not build custom auth.
- Do not build full account management.
- Do not expose raw auth email as the primary public identity.
- Do not build public player-pick views in this step.
- Do not let board/menu/controller code call Supabase directly.
- Do not make Supabase own View or Controller behavior.

## Relation to completed cards

- Card 227 made the runtime use canonical `BracketDocument`.
- Card 228 made the site save `BracketDocument` through a repository/store seam.
- Card 229 finalized SQL/RLS around canonical `BracketDocument` persistence.
- Card 230 defines the site UI surface that will let the signed-in user activate the Supabase-backed path.
