# Public Multi-User Play Rule

The WC2026 Bracketeering Pub site may evolve from a local-only static game into an invite-ready public play surface, but it must do so through explicit storage boundaries and without breaking the current site.

## Public play target

A player can receive a public site address, open it, sign in, make picks, save picks, submit picks, return later from another device, and eventually see scoring or leaderboard results.

## Required modes

The site must support these modes as explicit product states:

- anonymous local draft
- signed-in saved draft
- submitted bracket
- locked bracket

Anonymous local play remains valid during and after the multi-user transition unless a replacement is intentionally implemented and verified.

## Backend posture

The first invite-ready backend should be inexpensive and hosted. The preferred first implementation is:

- static frontend hosting
- Supabase Auth for identity
- Supabase Postgres for user bracket documents
- Row Level Security for user-owned access
- no custom always-on server for the MVP

A custom API server, payment system, private pool system, and full admin dashboard are not required for the first invite-ready version.

## Storage ownership

The backend stores user-owned bracket documents. It does not own visual geometry, gameboard rendering, or bracket UI behavior. The site model layer owns bracket derivation and validation.

## Site-running invariant

The site-running invariant is mandatory for this LI.

Every step toward public play must preserve a running local/static site. A change may add a new storage mode, login surface, or backend adapter only when the existing local-mode site can still load, render, and save picks through verified behavior.
