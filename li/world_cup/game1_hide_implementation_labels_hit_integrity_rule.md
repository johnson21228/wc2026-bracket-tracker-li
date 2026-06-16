# Game 1 Hidden Implementation Labels + R32 Hit Integrity Rule

Game 1 may carry implementation rule labels such as `3 C/D/F/G/H`, `1I`, or `2A` as data, tooltip/debug, and verification information, but those labels must not be rendered as visible UI inside the board during normal play.

The visible board should communicate selectability through slot fill, slot outline, hover/focus state, and pick-card affordance, not through raw implementation labels.

R32 hit testing must be driven by the same SVG-derived manifest geometry used to draw the transparent middle gameboard layer. The mapping from R32 visual slots to Game 1 rules is by slot position:

- positions 1–16 map to left-side R32 manifest slots sorted top-to-bottom
- positions 17–32 map to right-side R32 manifest slots sorted top-to-bottom

The rule attached to a slot is still the Game 1 R32 rule source. The manifest supplies geometry only. Menu choices must come from the slot rule under the pointer, with third-place pool slots opening third-place pool menus and winner/runner-up slots opening the appropriate group menus.
