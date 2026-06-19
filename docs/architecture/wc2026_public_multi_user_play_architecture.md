# WC2026 Public Multi-User Play Architecture

## Goal

Move the Bracketeering Pub site from local-only play toward an invite-ready public site where players can sign in, save picks, submit brackets, and later see scoring.

## Invite-ready definition

The site is invite-ready when a player can:

1. open a public site address
2. sign in or create an account
3. make Game 1 and/or Game 2 picks
4. save picks to their account
5. return from another browser/device and recover picks
6. submit a bracket
7. see that the bracket is submitted or locked

Leaderboard and private pools are valuable later features, but they are not required to prove invite-ready storage.

## Architecture

```text
Site UI
  ↓
Game model / pick logic
  ↓
Canonical pick-state JSON
  ↓
BracketRepository
  ↓
LocalStorageBracketStore OR RemoteBracketStore
  ↓
Browser localStorage OR hosted auth/database
```

## Backend strategy

The inexpensive MVP backend should avoid a custom server. The recommended first backend is:

- Supabase Auth
- Supabase Postgres
- Row Level Security
- static frontend hosting

The browser can call Supabase directly with a public anon key. The service role key must never be committed or exposed to the browser.

## Data strategy

The backend stores two JSON documents per user:

- `game1` pick state
- `game2` pick state

This is intentionally simpler than a normalized pick row table. The bracket has a small bounded number of picks, and full-document save/load matches the existing local/export workflow.

## Site-running invariant

Every public-play change must preserve the current local/static site behavior until the new behavior is intentionally promoted. The local storage path is not throwaway; it is the anonymous mode, offline fallback, and migration source.

## Phased delivery

1. Capture storage model and public-play LI.
2. Route current local storage through canonical pick-state JSON.
3. Define remote store contract.
4. Add account UI shell.
5. Add Supabase backend setup docs and schema.
6. Implement Supabase remote store.
7. Add local-to-account migration and save/load status.
8. Add submit/lock behavior.
9. Add invite-ready verification.
10. Add scoring and leaderboard later.
