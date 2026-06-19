# Card 222: Confirm Bracketeering Model Persistence Contract

## Goal

Define the saved bracket model that moves between the Pages app and durable storage.

## Context

Bracketeering is served from GitHub Pages. The Pages site owns the View, Controller, and runtime JavaScript Model while the player is interacting with the board.

Supabase/Postgres should provide durable backend Model persistence only. It should not change the fact that the board/controller code works through a storage boundary rather than raw database calls.

No Supabase SQL has been applied yet. This card must be completed before SQL setup is treated as final.

## Scope

- Identify the canonical `bracketState` JSON shape.
- Identify required persisted fields:
  - `user_id`
  - `game_id`
  - `picks_json`
  - `visibility`
  - `submitted_at`
  - `locked_at`
  - `created_at`
  - `updated_at`
- Confirm draft vs submitted vs locked meaning.
- Confirm that draft data is private by default.
- Confirm that shared reads apply only when visibility/submission/lock rules allow.

## Required durable fields

`user_brackets` should persist, at minimum:

- `user_id` — owner identity, normally `auth.uid()` in Supabase.
- `game_id` — durable game key such as `game1` or `game2`.
- `picks_json` — canonical bracket state document from the Pages runtime model.
- `visibility` — sharing state such as `private`, `public`, or future room/pool visibility.
- `submitted_at` — null for draft, set when the player submits.
- `locked_at` — null while editable, set when game rules lock edits.
- `created_at` — row creation time.
- `updated_at` — row update time.

## Draft / submitted / locked meaning

- Draft: `submitted_at is null`; owner can save/update; other players cannot read by default.
- Submitted: `submitted_at is not null`; owner has intentionally entered picks; shared reads may become eligible when visibility/game rules allow.
- Locked: `locked_at is not null`; normal owner edits stop; shared reads may become eligible when visibility/game rules allow.

## Core invariant

WRITE is private.
READ can be shared when game rules allow it.

This means owner-write/shared-read RLS is the target, not private-only owner-read RLS forever.

## Acceptance

- Bracketeering WB has a clear durable model contract.
- Supabase SQL target matches that contract.
- No private-only owner-read assumption remains as the final target.
- The plan remains narrow: define the model data seam before implementing save/load.
- The board/controller will use the BracketStore boundary rather than raw Supabase APIs.
