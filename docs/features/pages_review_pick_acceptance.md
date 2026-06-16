# Pages Review Pick Acceptance

The public review build must be operable, not merely served.

This repair adds a defensive client-side acceptance layer for the unified bracket board. When a reviewer chooses a team from a menu, the selection is written to:

- `wc2026.game1.bracketPicks`
- `wc2026.game1.r32.picks` for R32 slots
- `wc2026.game1.r16.winnerPicks` for R16 slots
- `wc2026.game1.qfSf.winnerPicks` for downstream slots

The repair is intentionally review-facing. It does not replace the long-term canonical pick transaction model. It guarantees that the Pages URL can be reviewed on iPhone while the underlying storage/render code is consolidated.
