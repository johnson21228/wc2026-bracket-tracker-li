# Capture Back — Unhide Workbench Easter Egg Button

The Workbench / Easter egg floating button is restored as a visible player-facing control.

This supersedes the prior hidden-button card. The Workbench panel remains available from the UI through the floating button.

Invariants:
- visible floating Workbench/Easter egg button
- keyboard-reachable entry point
- no `hidden`, `aria-hidden="true"`, or `tabindex="-1"` on the entry button
- panel code remains wired
