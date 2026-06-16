# Card 052 — Restore Game 1 Group-Filtered Tap Menu

## Intent
Restore the Game 1 on-tap chooser behavior after page resets. A clicked Round-of-32 slot must only show teams from the group or groups referenced by that slot rule.

## Contract
- `1A` shows Group A only.
- `2F` shows Group F only.
- `3 A/B/C/D/F` shows Groups A, B, C, D, and F only.
- The chooser never falls back to all teams when the slot rule contains a group constraint.
