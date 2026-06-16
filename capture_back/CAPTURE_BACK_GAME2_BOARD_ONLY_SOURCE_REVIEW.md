# Capture Back — Game 2 Board-Only Source Review

## Captured decision

Game 2 should temporarily show only the shared game board image. This creates a clean review state for the source board before bracket items, hit targets, and advancement regions are mapped back onto the pixel-native plane.

## Files added or changed

- `site/game2/index.html`
- `li/world_cup/game2_board_only_source_review_rule.md`
- `docs/geometry/game2_board_only_source_review.md`
- `cards/063_game2_board_only_source_review_card.md`
- `capture_back/CAPTURE_BACK_GAME2_BOARD_ONLY_SOURCE_REVIEW.md`

## Verification

Run `make verify` and `make pack` after applying.
