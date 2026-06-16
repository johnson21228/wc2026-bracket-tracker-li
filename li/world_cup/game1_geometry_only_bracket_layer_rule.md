# Game 1 Geometry-Only Bracket Layer Rule

The Game 1 middle board layer must be a transparent image containing only bracket geometry. Slot numbers and team identities are runtime/data concepts and must not be baked into the middle board art.

The layer order is:

1. pub/background image
2. transparent bracket geometry overlay
3. runtime hit targets and picks
4. chooser/modal UI

Decorative layers must use `pointer-events: none`; runtime hit targets must remain clickable above them.
