# Capture Back: Game 1 / Game 2 State Separation and No R16+ Preselect Highlight

## Context

Bracketeering has two related but distinct game states:

- Game 1: player picks
- Game 2: FIFA-final / read-only resolved tournament bracket

The runtime must not visually blur those states. In particular, R16+ cells should not show pre-select or highlight behavior merely because a team is downstream, inferred, a candidate, or resolved in Game 2.

## Product correction

Game 1 and Game 2 state ownership must remain strongly separated.

Pre-select highlight is an interaction state, not an inferred bracket state.

## Desired behavior

### R32 Game 1 cells

- May show active pick/menu preselection when the player is choosing a team.
- May show selected state after the player picks.

### R16+ Game 1 cells

- Must not show pre-select highlight until the player directly opens/interacts with that pick cell.
- Must not look selected merely from inferred advancement.
- Must not receive hover/preselect styling from Game 2 resolved bracket state.

### Game 2 cells

- Remain read-only.
- May render FIFA-final assignments as read-only truth.
- Must not drive Game 1 pick-highlight state.

### Lifecycle stage

- Remains presentation-only.
- Must not create selection/highlight state for R16+ cells.

## Acceptance

- Game 1 and Game 2 state ownership is explicitly documented in LI.
- R16+ cells do not show pre-select highlight unless directly interacted with.
- Game 2 read-only resolved bracket state does not create Game 1 highlight state.
- Lifecycle stage remains presentation-only.
- Existing R32 pick interaction still works.
- `make verify` and `make pack` pass.
