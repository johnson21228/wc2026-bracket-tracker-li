# Card 1014: Admin_/official results truth

## Purpose

Make `Admin_/official` the official result-truth source used by standings, scoring comparison, and read-only player board comparison.

## Rules

- `Admin_/official` owns official R32 entrants and official result winners.
- Player brackets own only player prediction picks.
- Standings must not use a player bracket as result truth.
- The official row must be excluded from player rankings.
- Partial official truth is valid during setup/testing.
- Static fallback must not override an existing Admin official row.

## Implementation notes

- `SupabasePlayerStandingsStore` reads player and official rows from `user_brackets`.
- It separates the `Admin_/official` row from player rows.
- It computes knockout score by comparing player picks to non-R32 official truth picks.
- Read-only board viewer rows carry `officialTruthPicksBySlot` and `officialResultsTruthSource` for comparison display.

## Verification

`tools/verify_wc2026_admin_official_results_truth.py` enforces the source boundary and prevents player rows from becoming official result truth.
