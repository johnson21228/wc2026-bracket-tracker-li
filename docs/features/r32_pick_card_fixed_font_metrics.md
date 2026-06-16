# R32 Pick Card Fixed Font Metrics

This feature locks the visual metrics for Round of 32 pick cards so all team names are rendered consistently.

The previous direction allowed the card to become too large or the name font to vary by team. That makes the game board harder to read and breaks the principle that the board-defined slot is the visual authority.

## Desired user-visible result

- Every filled R32 card stays inside its slot.
- The flag is nearly as tall as the card allows.
- The team name uses the same font size and line height for every team.
- Short names stay one line.
- Longer names wrap to two lines where necessary.
- Extended slot/team details remain in the tooltip or details surface.

## Current metric choice

The current 148 × 40 R32 slot metric uses a 34 × 32 flag box and a 14px bold team-name font with 14px line height and two-line wrapping.

This is intentionally not a per-team auto-fit system. The same metrics apply to Brazil, Canada, South Korea, Ivory Coast, Bosnia-Herzegovina, New Zealand, Saudi Arabia, and the rest of the 48-team field.
