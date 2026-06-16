# Capture Back — R32 Pick Card Runtime Safety Repair

The fixed-font-metrics pass crossed a boundary: a visual card typography change introduced invalid JavaScript and broke Game 1 pick rendering.

This capture back restores the boundary:

- R32 pick card / slot occupant card is the canonical term for the filled-slot visual object.
- Card fit and font metrics are visual concerns.
- Pick state, slot mapping, and data loading are runtime concerns and must not be damaged by visual changes.
- Display-name line breaking must not use raw newline characters inside JavaScript string literals.
