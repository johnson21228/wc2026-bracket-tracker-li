# Game 1 Reads Uniform SVG Gameboard Manifest Rule

Game 1 must be able to read the uniform SVG gameboard manifest before it migrates to the new visible gameboard.

The current geometry authority chain is:

- `tools/generate_uniform_pick_card_gameboard.py` defines the generated board geometry model.
- `site/assets/playfield/uniform_pick_card_gameboard.svg` is the visual geometry authority.
- `site/data/geometry/uniform_pick_card_gameboard_manifest.json` is the app-readable geometry contract derived from the same model.
- `site/assets/playfield/uniform_pick_card_gameboard.png` is a derived review/fallback artifact.

Game 1 may load the manifest as a non-visible, validation-only dependency. Loading the manifest does not migrate the board.

Until an explicit migration card switches the Game 1 board layer, Game 1 must continue to render its existing visible board asset. The manifest read is only a runtime contract probe.

The probe must verify, without changing the UI:

- the manifest exists and is parseable;
- the native board size is 1536 by 1024;
- the board model contains 61 pick-card slots for the current model;
- round counts are R32 = 32, R16 = 16, QF = 8, SF = 4, FINAL_FOUR = 1;
- every slot has a pixel bounds record;
- Game 1 does not invent geometry independently of the manifest.

The manifest may be exposed to local file review through a generated JavaScript shim, but the JSON manifest remains the app-readable geometry contract and the shim is a derived convenience artifact.
