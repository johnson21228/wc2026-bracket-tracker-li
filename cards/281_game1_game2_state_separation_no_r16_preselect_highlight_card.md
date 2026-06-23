# Card 281: Game 1 / Game 2 State Separation and No R16+ Preselect Highlight

## Intent

Capture the state ownership rule that prevents R16+ cells from showing pre-select highlight unless directly interacted with.

## Why

Game 1 player-pick state and Game 2 FIFA-final read-only resolved state are related, but they must not visually blur. R16+ inferred/candidate values should not look like active player selections.

## Acceptance

- Game 1 and Game 2 state ownership is documented.
- R16+ preselect highlight is interaction-owned only.
- Game 2 resolved state does not drive Game 1 highlight state.
- Lifecycle stage remains presentation-only.
- Existing R32 pick interaction remains valid.
