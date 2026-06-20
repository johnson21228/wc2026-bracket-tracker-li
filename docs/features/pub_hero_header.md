# Pub hero header

The top app surface is the Game 1 hero header. It frames the site as a pub-friendly picking game rather than an implementation demo.

Required copy:

- eyebrow: `World Cup 2026`
- title: `FIFA Bracketeering`
- subtitle: `Scroll the game board below and make your picks.`

Required utility actions:

- `Clear picks`
- `Export picks`
- `Import picks`

Export writes a JSON snapshot of current picks. Import reads a JSON snapshot and routes it back through model validation so the checked-in game rules remain authoritative.
