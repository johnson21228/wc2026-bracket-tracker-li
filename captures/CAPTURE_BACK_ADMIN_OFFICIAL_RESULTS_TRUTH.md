# Capture Back: Admin_/official results truth

## Intent

`Admin_/official` is the source of official results truth for WC2026 Bracketeering.

## Invariant

- R32 entrants are official `Admin_/official` entrant truth.
- Official results and resolved winners are `Admin_/official` result truth.
- Player brackets hold player predictions only.
- Scoring compares player predictions against `Admin_/official` truth.

## Runtime boundary

The Supabase standings store reads both player rows and the `Admin_/official` official row from `user_brackets`. The official row is normalized as an Admin truth document and is not rendered as a player standings participant. Player rows are scored against the official truth picks by slot.

Partial official truth is allowed during setup/testing. Missing official winner slots simply do not score yet. The static JSON fallback remains a local/dev fallback only when an admin source is unavailable; it must not override an existing `Admin_/official` row.

## Viewer boundary

The read-only player board viewer receives the official truth picks separately from the player picks. It may show official result feedback for comparison, but it does not treat any player row as official truth.

## Non-goals

- No Supabase schema change.
- No admin UI.
- No player edit UX change.
- No group-stage player picks.
