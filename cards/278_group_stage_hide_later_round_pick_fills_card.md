# Card 278: Hide later-round pick fills during Group Stage presentation

## Goal

During Group Stage presentation, do not render filled pick slots after Round of 32. This keeps the player-facing board focused on group-stage setup while preserving all stored picks.

## Acceptance criteria

- R32 filled picks still render during Group Stage.
- R16 and later filled picks do not render during Group Stage.
- R16 and later filled picks render again during Knockout Stage.
- The change is rendering-only.
- No stored picks are deleted.
- No pick write path is gated.
- Game 2 resolved R32 rendering remains available.

## Files

- `site/js/mvc/view.js`
- `tools/verify_wc2026_group_stage_hides_later_round_pick_fills.py`
- `docs/features/group_stage_hide_later_round_pick_fills.md`
- `captures/CAPTURE_BACK_GROUP_STAGE_HIDE_LATER_ROUND_PICK_FILLS.md`
