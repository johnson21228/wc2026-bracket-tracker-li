# Card 193: Refine Group Button Rail Subtle Visual State

## Intent

Make the bottom group button rail visually quiet until the user interacts with a group tile.

## Rule

Group rail tiles are secondary inspection controls. They should be discoverable without competing with the bracket board.

## Acceptance

- At rest, `.group-rail-tile` has opacity below `1`.
- On hover, focus-visible, active, or `.is-active`, `.group-rail-tile` becomes fully opaque.
- The visual state change is CSS-only.
- The change does not alter controller routing, view placement, group panel anchoring, or data model behavior.
- `make verify` runs a dedicated verifier for the subtle visual state.
