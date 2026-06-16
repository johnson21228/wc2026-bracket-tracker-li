# Capture Back — Repo Hygiene Cleanup

## Reason

The site now has enough feature overlays that the repo root must be normalized before more game behavior is added. The previous pack included applied overlay working directories and `.DS_Store` files, and the root README described the latest overlay rather than the actual repo.

## Decision

Preserve the two-page site model:

- `index.html` remains the main tracker / Game 2 surface.
- `game1_playfield.html` remains the Game 1 Round of 32 chooser playfield.

Clean overlay residue from root and make verification enforce hygiene.

## Evidence

The verifier now checks required entry points, data files, playfield assets, README identity, `.DS_Store` absence, and absence of root overlay working directories.
