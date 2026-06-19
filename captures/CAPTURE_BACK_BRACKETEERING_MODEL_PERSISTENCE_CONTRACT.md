# Capture Back: Bracketeering Model Persistence Contract

## Intent

Preserve the next narrow Bracketeering backend step before Supabase SQL is applied: confirm the durable Model data contract that moves between the GitHub Pages runtime and Supabase/Postgres persistence.

This is not a frontend rewrite and not a Supabase learning exercise. It is a small model-persistence seam task in the Bracketeering Workbench.

## Core boundary

- GitHub Pages owns the View, Controller, and runtime game state while the player interacts with the board.
- Pages JavaScript owns the live `bracketState` object while playing.
- Supabase/Postgres owns durable persistence for saved/submitted bracket state.
- Supabase access should remain behind the BracketStore / RemoteBracketStore boundary.

## Card captured

Card: Confirm Bracketeering Model Persistence Contract

Goal:
Define the saved bracket model that moves between the Pages app and durable storage.

Scope:
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

Acceptance:
- Bracketeering WB has a clear durable model contract.
- Supabase SQL target matches that contract.
- No private-only owner-read assumption remains as the final target.

## Model invariant

WRITE is private.
READ can be shared when game rules allow it.

Meaning:
- A player can create/update only their own bracket.
- Draft picks are private by default.
- Other players may read submitted/locked/public brackets only when the game rules allow it.
- No player can edit another player's picks.
- No player can edit locked picks unless a deliberate game rule reopens them.

## Implementation note

The next implementation should be small because both subtasks focus on the same seam:

1. The durable bracket model shape.
2. The store boundary that moves that model between Pages and persistence.

The board/controller code should not learn Supabase table names, RLS policy names, or auth implementation details.
