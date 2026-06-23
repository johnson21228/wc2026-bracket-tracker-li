# Capture Back: Group Stage hide later-round pick fills

## Intent

During Group Stage presentation, reduce bracket visual noise by showing filled pick slots only for Round of 32. Later-round pick fills should not render until Knockout Stage presentation.

## Product rule

- Group Stage: render R32 filled picks.
- Group Stage: suppress filled rendering for R16, QF, SF, Final, Champion, and Third Place.
- Knockout Stage: render all filled picks normally.
- Stored picks remain untouched.
- Pick validity, save/load, and pick pipeline remain unchanged.

## Verification

`tools/verify_wc2026_group_stage_hides_later_round_pick_fills.py`
