# WC2026 Single Geometry Truth

The Bracketeering Hub board geometry has one canonical truth.

| Artifact | Role |
| --- | --- |
| `site/assets/playfield/uniform_pick_card_gameboard.svg` | Source-truth geometry |
| `site/data/geometry/uniform_pick_card_gameboard_manifest.json` | Generated/runtime projection |
| `site/assets/playfield/uniform_pick_card_gameboard.png` | Rendered visual derivative |

The runtime may consume JSON, but JSON is not an independent geometry truth.

CSS may style surfaces, but CSS is not canonical slot geometry.

View/controller/model code may render and activate cells, but must not invent geometry absent from the source-truth board geometry.

## Final Four impact

The existing single `FINAL_FOUR` center card is legacy/current behavior. The intended next geometry model is a center stack with explicit semifinal-winner and final-winner cells.

That work must begin from source-truth geometry, then update the generated manifest projection.
