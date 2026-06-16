# Use Site Pick Store Render Rule

For Game 1, every bracket choice must be storable and renderable through the site bracket pick store.

Invariant:

> The bracket cell is the storage key.

A menu selection must write to `wc2026.game1.bracketPicks[slotId]` and the render path must read from that same store before falling back to legacy round-specific buckets.

R16 must not depend on a separate hidden storage model to be visible.
