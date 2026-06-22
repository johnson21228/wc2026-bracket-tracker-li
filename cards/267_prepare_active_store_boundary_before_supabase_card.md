# Card 267 — Prepare active store boundary before Supabase

Prepare the Bracketeering Pages runtime for separate local and future Supabase-backed bracket modes.

Acceptance:
- `BracketDocument` includes phase-level R32 lock metadata.
- A local/remote active store/session seam exists.
- Local mode remains the active implemented persistence mode.
- Remote mode is reserved for later `SupabaseBracketStore` work.
- Local and remote pick contents are not merged, migrated, reconciled, or required to match.
- R32 picks cannot mutate after `phaseLocks.r32LockedAt` exists.
- Supabase SQL is not applied.
