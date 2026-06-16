# Card 058 — Capture Game 2 Shared Bracket Plane

## Intent
Correct the mismatch between the middle-layer bracket PNG and the logical placement of Game 2 bracket items.

## First-order rule
The geometry image, slot guides, and bracket items must all live in the same `bracketPlane` coordinate frame.

## Why
The earlier Game 2 page placed the PNG using one inset and item logic using another inset. That made logical geometry disagree with visual geometry before slot tuning could even begin.

## Acceptance
- Game 2 has one shared `bracketPlane`.
- The geometry PNG is inside that plane.
- Slot guides are inside that plane.
- Bracket items are inside that plane.
- Slot coordinates are percent-of-bracketPlane.
- Game 1 is untouched.
