# Site Bracket Pick Store Rule

Game 1 must treat every bracket cell as a store address.

## Rule

The bracket slot id is the storage key.

All Game 1 bracket picks should be representable in one unified map:

    wc2026.game1.bracketPicks[slotId]

R32, R16, QF, SF, final, and champion cells are not separate storage concepts. They are bracket cells with different rounds.

## Static Site Boundary

The site may define the storage contract and runtime API. User picks persist in browser localStorage unless a backend or export/import persistence flow is added later.
