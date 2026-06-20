# Card 230 — Define Supabase-backed identity UI surface for Bracketeering site

## Purpose

Define the minimal site-owned identity/status UI surface needed to connect Bracketeering to Supabase Auth and Supabase/Postgres persistence without building a custom login/profile system.

## Context

Bracketeering is preparing to connect the Pages site to Supabase Auth and Supabase/Postgres persistence.

Completed prerequisites:

- Card 227: runtime uses canonical `BracketDocument`
- Card 228: site saves `BracketDocument` through a repository/store seam
- Card 229: Supabase SQL/RLS target finalized against canonical `BracketDocument`

## Important clarification

This card is not a custom authentication system.

Supabase owns the hard identity/auth machinery:

- sign up / sign in
- sessions
- current authenticated user
- `auth.uid()`
- secure linkage to Postgres RLS

The Bracketeering site owns only a thin identity/status surface that lets the player see and control whether the current `BracketDocument` is anonymous/local or signed-in/Supabase-backed.

## Product direction

Add an upper-right identity/status surface to the site.

Minimal unsigned state:

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

## Core data path

The UI surface exists to prove and control this path:

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

## Architecture invariant

```text
Same BracketDocument. Different store.
```

Signed out:

```text
BracketRepository → LocalStorageBracketStore
```

Signed in:

```text
BracketRepository → SupabaseBracketStore
```

The controller and board should not know whether persistence is localStorage or Supabase.

## Required boundaries

- Do not build custom auth.
- Do not build a full profile/account-management system.
- Do not build public player-pick views yet.
- Do not let board/menu/controller code call Supabase directly.
- Do not make Supabase own View or Controller behavior.

## Site UI owns

- sign-in button placement
- signed-in display/status
- save status display
- sign-out action
- optional local-to-account import prompt
- user-facing explanation of local vs signed-in persistence

## Supabase owns

- authentication
- session
- auth user id
- Postgres persistence
- RLS enforcement
- profile row used for public display name

## Acceptance

- The Workbench clearly defines the upper-right identity/status surface.
- The UI surface is scoped as a thin shell around Supabase Auth.
- Anonymous localStorage play remains supported.
- Signed-in play is described as Supabase-backed `BracketDocument` persistence.
- The UI surface does not become a custom login/profile system.
- The architecture continues to preserve:
  - Pages owns View/Controller/runtime model.
  - Supabase owns Auth/Postgres/RLS/persistence.
  - `BracketRepository` owns the save/load boundary.
