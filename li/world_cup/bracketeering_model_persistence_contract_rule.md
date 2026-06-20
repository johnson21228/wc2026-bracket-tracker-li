# Bracketeering Model Persistence Contract Rule

The Bracketeering backend migration must be treated as a model-persistence seam, not a frontend rewrite.

## Rule

Before Supabase SQL is applied or RemoteBracketStore is implemented, the Workbench must preserve the durable bracket model contract that moves between the Pages runtime model and Supabase/Postgres.

## Required contract

The durable `user_brackets` model must include:

- `user_id`
- `game_id`
- `picks_json`
- `visibility`
- `submitted_at`
- `locked_at`
- `created_at`
- `updated_at`

## Runtime boundary

GitHub Pages remains the View/Controller/runtime Model surface. Pages JavaScript owns the active `bracketState` while the player is using the board.

Supabase/Postgres provides durable Model persistence for saved/submitted bracket state.

## Security / sharing invariant

WRITE is private.
READ can be shared when game rules allow it.

Draft picks are private by default; draft rows are not shared. Submitted picks and locked picks may become shared-readable when game rules allow it. Future shared pick views require owner-write/shared-read RLS, not private-only RLS forever.

## Store boundary

Supabase APIs must stay behind the BracketStore / RemoteBracketStore boundary as much as practical. Board click handlers, pick menus, and advancement logic should not call raw Supabase APIs directly.

<!-- CARD-227-CANONICAL-BRACKET-DOCUMENT-RUNTIME -->

## Card 227 runtime confirmation

The Pages runtime must use the canonical `BracketDocument` before Supabase persistence is introduced.

Required runtime fields are `schemaVersion`, `gameId`, `status`, `expectedPickCount`, `updatedAt`, and `picksBySlot`.

`CHAMPION` and `THIRD-PLACE-WINNER` are first-class runtime/model slots. Game 1 expected total: 64 picks. Game 2 expected total: 32 picks.

`user_brackets.picks_json` stores this same canonical `BracketDocument`; Supabase remains durable persistence only.

