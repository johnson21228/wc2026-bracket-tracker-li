# Track R32 pick buttons rule

The Game 1 R32 pick layer must make pickability observable.

Each rendered R32 slot button should expose pickability state in DOM data attributes and should render a visible pre-select highlight before selection.

The view may track hover, focus, and click state, but it must not become the source of legality. The controller remains the authority for:

- slot enabled state
- menu candidate contents
- pick validation
- duplicate prevention
- write-back to the Game 1 R32 projection pick model
