# Game 1 Transparent SVG Middle Layer

This repair changes the Game 1 uniform board migration from an opaque SVG board replacement into the intended layered architecture.

The bottom layer remains the pub/background image. The SVG sits above it as transparent bracket linework and slot outlines. Game 1 then projects its R32 hit regions and filled pick cards from the same manifest that was generated from the SVG.

This removes the checkerboard/proof-title artifact and prevents the prior mismatch where the board visual used the new SVG while the R32 picks still used old PNG-era coordinates.

Current authority chain:

```text
tools/generate_uniform_pick_card_gameboard.py
  -> site/assets/playfield/uniform_pick_card_gameboard.svg
  -> site/assets/playfield/uniform_pick_card_gameboard.png
  -> site/data/geometry/uniform_pick_card_gameboard_manifest.json
  -> site/data/geometry/uniform_pick_card_gameboard_manifest.js
  -> Game 1 R32 hit/pick-card geometry
```

The SVG is geometry truth and transparent middle-layer presentation. The PNG is derived review/fallback output. The manifest is the runtime geometry contract.
