# Card 288: Single Game Admin_/official Runtime

## Goal

Remove stale two-game runtime authority and align MVC/Supabase behavior with the current one-game Bracketeering LI.

## Scope

- MVC runtime gates
- legacy presentation selector handling
- Supabase bracket store canonical game id
- Admin_/official missing-row create mode
- stale verifier supersession

## Done

`make verify` includes the single-game Admin_/official runtime verifier.
