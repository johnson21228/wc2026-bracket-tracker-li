# Card 042 — Repair Game 1 pub background and hit testing

## Intent
Make the pub JPEG background visibly participate in the Game 1 board while preserving the clickable Round-of-32 hotspots.

## Change
- Adds tunable opacity variables for pub background, board template, and wash layer.
- Keeps decorative layers non-interactive.
- Keeps hotspots on the highest gameplay layer.
- Adds a Show Hit Zones debug toggle for visual verification.
- Stores visual tuning values in local storage.
