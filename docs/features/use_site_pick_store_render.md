# Use Site Bracket Pick Store to Hold and Render Choices

Game 1 now treats `wc2026.game1.bracketPicks` as the first-class runtime store for bracket selections.

The cell ID is the storage key:

- `L-R32-01`
- `L-R16-01`
- `L-QF-01`
- `L-SF-01`

Menu selections write to this store. Render passes read this store before falling back to the older round-specific buckets.

This converts the bracket from separate R32/R16/QF/SF buckets into a single slot-keyed model while keeping legacy compatibility during transition.
