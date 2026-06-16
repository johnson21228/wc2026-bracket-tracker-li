# R32 Pick Card Single Tooltip and Name Fit

This feature tightens the Round of 32 pick-card rendering behavior after review of the Game 1 board.

Observed issue:

- A filled pick could show both a custom tooltip and the browser's native title tooltip.
- Longer display names could truncate even when the card visually had room to communicate the team name.

Desired behavior:

- One custom details surface is used for extended properties.
- Native browser title tooltips are suppressed for pick cards.
- The compact card shows a larger flag and a team name that fits when possible.
- The card remains clickable/tappable to change the pick.

Boundary:

- Pick card: team identity.
- Details surface: team/slot/rule explanation.
- Chooser menu: pick-changing workflow.
