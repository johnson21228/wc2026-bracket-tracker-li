# Site Bracket Pick Store

Game 1 now has a site-owned pick store contract.

The store does not make a static site write back into a repository file. Instead, the site owns the slot list, storage key, and API shape. Runtime picks persist in browser `localStorage` under one unified key:

    wc2026.game1.bracketPicks

Every bracket cell is addressable by its slot id:

    L-R32-01
    L-R16-01
    L-QF-01
    L-SF-01
    CENTER-FINAL-FOUR

This replaces the mental model of separate R32/R16/QF/SF buckets with one map keyed by bracket cell.
