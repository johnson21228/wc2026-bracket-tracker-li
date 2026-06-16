# Game 1 R32 Pointer Rule Integrity

A browser review showed a Game 1 R32 chooser opening `Winner Group I` when the visible selected target was intended to be a best-third-place pool slot.

The failure pattern is likely a geometry/target mismatch after migrating Game 1 to the uniform SVG middle-layer board: the SVG slot, hit target, and menu rule can become adjacent but not identical.

This repair adds a pointer resolver. On click/tap, Game 1 projects the pointer into the board's native SVG coordinate system and chooses the R32 rule whose manifest-derived rectangle contains, or is nearest to, that point. If the DOM event target and resolved manifest slot disagree, the manifest/pointer result wins and a console warning records the correction.

The repair preserves:

- current SVG board presentation,
- current R32 slot-rule data,
- current pick-card rendering,
- current menu UI,
- Game 2 unmigrated state.
