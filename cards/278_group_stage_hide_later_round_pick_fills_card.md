# Card 278: Group Stage later-round frame-only pick slots

## Goal

During Group Stage presentation, do not render filled pick-slot content after Round of 32. Later-round pick slots should remain visible as frames only.

## Acceptance criteria

- R32 filled picks still render during Group Stage.
- R16 and later pick slots render as frame-only during Group Stage.
- Frame-only slots do not show fill, flag/code, slot label, or `Choose Winner`.
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
