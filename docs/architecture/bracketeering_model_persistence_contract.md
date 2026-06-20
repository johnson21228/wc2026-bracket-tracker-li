# Bracketeering Model Persistence Contract

## Purpose

This document defines the durable model seam between the Bracketeering GitHub Pages app and Supabase/Postgres.

The work is intentionally small and straightforward: the Pages app already has game state; Supabase only needs to persist the saved/submitted form of that state.

## Runtime vs durable model

The Pages JavaScript runtime model owns active play state while the user is interacting with the board:

- selected teams
- slot state
- advancement state
- draft/submitted/locked state after load
- any derived render state needed by the board

Supabase/Postgres owns durable persistence for saved bracket state:

- profile/public display identity
- saved bracket rows
- visibility/submission/lock metadata
- future shared pick views
- future scoring and leaderboard data

## Canonical persistence row

The durable `user_brackets` contract should include:

```text
user_id
 game_id
 picks_json
 visibility
 submitted_at
 locked_at
 created_at
 updated_at
```

`picks_json` is the bridge document. It should be the canonical bracket state document that can be loaded by the Pages runtime, saved by LocalStorageBracketStore, and saved by RemoteBracketStore/SupabaseBracketStore.

## Sharing rule

WRITE is private.
READ can be shared when game rules allow it.

Draft data is private by default.

Submitted/locked/public data may be readable by other players when the game rules allow it.

The target SQL/RLS design must therefore support:

- private owner writes
- private owner draft reads
- shared reads for eligible submitted/locked/public brackets

It must not assume private-only owner reads forever.

## Store boundary

The board/controller should work through BracketStore methods, not raw Supabase calls:

```text
loadBracket(gameId)
saveBracket(gameId, bracketState)
submitBracket(gameId)
listVisibleBrackets(gameId) later
```

Anonymous play remains backed by LocalStorageBracketStore.

Signed-in play can use RemoteBracketStore/SupabaseBracketStore behind the same interface.

<!-- CARD-227-CANONICAL-BRACKET-DOCUMENT-RUNTIME -->

## Card 227 runtime confirmation

The Pages runtime must use the canonical `BracketDocument` before Supabase persistence is introduced.

Required runtime fields are `schemaVersion`, `gameId`, `status`, `expectedPickCount`, `updatedAt`, and `picksBySlot`.

`CHAMPION` and `THIRD-PLACE-WINNER` are first-class runtime/model slots. Game 1 expected total: 64 picks. Game 2 expected total: 32 picks.

`user_brackets.picks_json` stores this same canonical `BracketDocument`; Supabase remains durable persistence only.

