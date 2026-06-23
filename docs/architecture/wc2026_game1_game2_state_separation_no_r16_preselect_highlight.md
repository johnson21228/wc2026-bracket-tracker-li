# WC2026 Game 1 / Game 2 State Separation and R16+ Highlight Ownership

Bracketeering has two related but distinct game states:

- Game 1 owns player picks.
- Game 2 owns FIFA-final / read-only resolved tournament truth.

Those states may be displayed on the same board, but they must not share visual selection authority.

R16+ Game 1 cells must not show pre-select highlight merely because a team is downstream of an R32 pick, inferred by candidate resolution, present in Game 2 resolved data, or affected by lifecycle-stage presentation. Pre-select highlight belongs to direct player interaction only.

Lifecycle stage remains presentation-only. It can affect board presentation and background, but it must not create pick-selection or preselect-highlight state.
