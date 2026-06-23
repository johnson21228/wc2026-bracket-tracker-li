# Game 1 / Game 2 State Separation and No R16+ Preselect Highlight Rule

Game 1 and Game 2 state must remain separate.

Game 1 owns player pick state.
Game 2 owns FIFA-final read-only resolved state.

Game 2 resolved state must not mark Game 1 cells as selected, preselected, highlighted, or interactively active.

For R16+ Game 1 cells, pre-select highlight is allowed only when the player directly opens or interacts with that specific pick cell. It must not come from downstream inference, candidate resolution, current lifecycle stage, or Game 2 resolved bracket truth.

R32 Game 1 pick interaction may still show active selection/preselection while the player chooses a team.

Lifecycle stage remains presentation-only and must not create selection or highlight state.
