# Prompt — Switch Game 1 Board Layer to Uniform SVG

Patch Game 1 so the visible board layer uses `site/assets/playfield/uniform_pick_card_gameboard.svg`, while preserving all existing layers above and below it.

Do not migrate Game 1 hit targets or pick cards to the uniform manifest yet. Keep the manifest read-only probe. Do not switch Game 2.

Verify that the board visual switched and the runtime contract probe still exists.
