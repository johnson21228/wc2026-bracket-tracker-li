# Capture Back — Uniform SVG Gameboard Manifest Authority Repair

This Capture Back repairs the authority pipeline introduced for the uniform SVG gameboard.

It clarifies that the SVG is source truth for geometry, the PNG is a derived review artifact, and the JSON manifest is the app-readable projection of the SVG geometry.

It also aligns the verifier with the current reviewed board model:

- R32: 32
- R16: 16
- QF: 8
- SF: 4
- FINAL_FOUR: 1
- Total: 61

This CB does not migrate Game 1 or Game 2 to the new board yet.
