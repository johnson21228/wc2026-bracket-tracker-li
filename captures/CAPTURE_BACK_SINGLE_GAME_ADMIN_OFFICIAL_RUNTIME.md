# Capture Back: Single Game Admin_/official Runtime

## Problem

The repo still contained stale Game 1/Game 2 and Group/Knockout presentation gates after Bracketeering moved to a single connected game. That stale code caused admin/player pages to render group-only surfaces or hide R32/player picks despite Supabase being connected.

## Decision

Reconcile runtime to the current LI:

- Persist one game as `game1`.
- Treat legacy `game-2` as a bracket-board presentation alias only.
- Require Admin_/official Supabase R32 authority for player rendering.
- Allow connected admin editor to create the missing official row.
- Keep players read-only on R32 and editable for later winners.

## Verification

`tools/verify_wc2026_single_game_admin_official_runtime.py` encodes the runtime invariant and supersedes stale active-game gating verifiers.
