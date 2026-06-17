# Card 111 — Add Game 1 R16 Winner Picks

## Intent

Allow Game 1 to begin behaving like the long-lived bracket workspace captured by the unified Game 1/Game 2 lifecycle LI.

When both Round of 32 source teams are set for a Round of 16 match, the user may pick that match winner into the associated R16 slot.

## Scope

- Adds a first-order R16 winner-pick layer to Game 1.
- Uses the uniform SVG gameboard manifest for R16 slot bounds.
- Derives each R16 match from the paired R32 slots on the same side of the board.
- Stores R16 winner picks separately from R32 slot assignment picks.
- Keeps Game 2 unchanged.

## Non-scope

- Does not add QF/SF/Final Four picks yet.
- Does not replace official FIFA R32 truth.
- Does not score Game 1 or Game 2.
- Does not change the uniform SVG asset or manifest.
