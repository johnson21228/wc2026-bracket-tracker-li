# FIFA R32 extraction / logic / geometry bridge rule

The FIFA-shaped Game 1 board must keep extraction evidence, FIFA logic, board geometry, and rendering separate.

Requirements:

- Source images belong under `source/images/`.
- Human-reviewed extraction records belong under `source/text/`.
- FIFA R32 logical slot identity belongs under `site/data/model/`.
- Board geometry belongs under `site/data/geometry/gameboard_manifest.json`.
- The bridge map may connect FIFA slot IDs to geometry slot IDs.
- Rendering may consume the bridge map but must not become source authority.
- Player picks must not be mutated by slot-map rendering.
