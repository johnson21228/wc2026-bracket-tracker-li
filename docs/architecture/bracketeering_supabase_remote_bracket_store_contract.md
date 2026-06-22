# Bracketeering Supabase remote bracket store contract

This document defines the future Supabase remote bracket store contract before implementation.

# Supabase remote bracket store contract before implementation

This rule defines the future Supabase remote bracket store contract before implementation.

It does not implement `SupabaseBracketStore`.

It does not apply Supabase SQL.

It does not change public Supabase dashboard state.

It does not change runtime site behavior.

## Core invariant

The site owns View and Controller behavior.

Supabase/Postgres provides durable Model persistence only.

Runtime code must access Supabase persistence through a store/repository/session seam, not directly from View or Controller code.

## Store boundary

The future remote store must conform to the same bracket store contract used by the local store:

- `loadUserBracket(userId)`
- `saveUserBracket(bracketDocument)`

The active session decides which store is authoritative.

Only the active store is authoritative.

Local mode and remote mode are separate storage modes.

There is no automatic merge, migration, or reconciliation between browser-local picks and Supabase picks.

## Remote storage target

The remote store targets the canonical Supabase table contract:

- one `user_brackets` row per player/game
- full canonical `BracketDocument` stored in `picks_json`
- private writes by owner
- shared reads only when game rules allow

Do not model one row per pick.

## Payload contract

The remote store saves and loads the full canonical `BracketDocument`.

The saved payload must preserve:

- `schemaVersion`
- `id`
- `userId`
- `tournamentId`
- `gameId`
- `status`
- `lifecycleState`
- `phaseLocks.r32LockedAt`
- `expectedPickCount`
- `createdAt`
- `updatedAt`
- `picksBySlot`
- legacy-compatible `picks`

The remote store must normalize loaded data through the canonical `BracketDocument` model before runtime use.

## R32 lock contract

The future Supabase implementation must preserve the R32 lock invariant.

After `phaseLocks.r32LockedAt` exists, R32 picks cannot be changed by the player.

This must be enforced in both places:

1. client-side model/session write path
2. Supabase/Postgres persistence policy or mutation guard

UI-only hiding is not sufficient.

## Error behavior

Remote save/load failures must not silently corrupt local state.

Remote errors should return or throw explicit failure information that the repository/session can surface.

A failed remote save must not be treated as a successful contest save.

Local browser mode must continue to work without Supabase.

## No direct UI Supabase access

View and Controller code must not call Supabase directly.

Supabase client calls belong behind the future remote store or service adapter.

The current identity surface may use Supabase Auth as a thin site-owned shell, but bracket persistence must remain behind the bracket store seam.

## Implementation boundary

This contract is a pre-implementation guard.

Allowed by this contract:

- LI/docs/verifier updates
- future `SupabaseBracketStore` implementation behind the store seam
- future repository/session wiring when explicitly scoped

Not allowed by this contract:

- direct Supabase calls from board View code
- direct Supabase calls from pick Controller code
- applying Supabase SQL as a side effect of this CB
- changing public Pages release posture
- merging unfinished remote persistence to `main`
