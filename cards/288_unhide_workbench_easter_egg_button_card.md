# Card 288 — Unhide Workbench Easter Egg Button

## Intent

Restore the Workbench / Easter egg floating button as a visible player-facing control.

## Product decision

The Workbench panel is again reachable from the Bracketeering UI. The previous hidden-button decision is superseded by this card.

## Acceptance

- The `workflow-floating-button` entry point is visible.
- The button is not marked `hidden`.
- The button is not `aria-hidden="true"`.
- The button is not removed from keyboard tab order.
- The Workbench panel code remains available and wired.
