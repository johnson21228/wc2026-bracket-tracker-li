# Game 2 Bracket Geometry Slots

Game 2 now has an explicit slot geometry model. The R32 seed creates bracket items, and each bracket item carries a `slotId`. The runtime looks up that slot in `site/data/game2_bracket_geometry_slots.json` and renders the item in the slot's percent-based box.

This is the transition layer between today's image-defined board and a future truth-geometry board.
