# Editable Site Official Truth JSON

Official tournament truth is stored in `site/data/current/official_truth.json`.

The file preserves the same payload shape that the old Supabase Admin_/official row supplied: a canonical `picksBySlot` map keyed by bracket slot ID.

This makes migration safe because scoring and board code can continue to use the same slot-record contract. Only the source changes.

## Stored in the site

The site JSON stores official tournament truth:

- R32 occupants
- R16 winners
- R8/QF winners
- R4/SF winners
- R2/Final-side winners
- Champion

## Stored in Supabase

Supabase stores player-owned data:

- player identity/profile
- player bracket picks

## Computed

Standings are never stored as authority. The site computes standings from Supabase player picks and site-owned official truth.

Computed values include:

- Score
- Max Possible
- rank
- standings rows

## Partial updates

The JSON may be incomplete while the tournament is in progress. Unknown R32 occupants and unresolved knockout winners may be omitted. Missing official `teamId` means unresolved.
