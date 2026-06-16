# Game 1 hide implementation labels and repair R32 hit-rule integrity

This change hides raw slot-rule labels from the board UI. Labels such as `3 C/D/F/G/H` are useful implementation/debug data, but when drawn over the board they can appear visually attached to the wrong neighboring card.

The change also reinforces the Game 1 R32 geometry contract:

- the SVG/manifest gives the hit/pick-card bounds
- Game 1 slot rules give the menu semantics
- R32 positions are mapped to manifest slots top-to-bottom by side
- third-place pool rules stay attached to their intended slot positions

This prevents a visible developer label near one card from implying that a neighboring selectable card has the same rule.
