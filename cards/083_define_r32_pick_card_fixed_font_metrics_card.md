# Card 083 — Define R32 Pick Card Fixed Font Metrics

## Intent

Define and apply shared fixed font metrics for Round of 32 pick cards.

## Why

The R32 pick card must fit inside the board-defined slot. The team flag should be vertically dominant, and all team names should use consistent metrics rather than per-team scaling.

## Acceptance

- `li/world_cup/r32_pick_card_font_metrics_rule.md` exists.
- `docs/features/r32_pick_card_fixed_font_metrics.md` exists.
- Game 1 filled R32 cards use fixed metrics.
- The compact card hides slot-rule text.
- Team names can wrap to two lines.
- No per-team font-shrink function is required for compact R32 cards.
- Verification passes.
