# Capture Back: Group Stage later-round frame-only pick slots

## Intent

During Group Stage presentation, reduce bracket visual noise by showing filled picks only for Round of 32. Later-round pick slots remain visible as frames but do not display fills, slot labels, flags, team codes, or `Choose Winner`.

## Product rule

- Group Stage: render R32 filled picks normally.
- Group Stage: render R16, QF, SF, Final, Champion, and Third Place pick slots as frame-only.
- Knockout Stage: restore the normal filled pick rendering for all later rounds.
- Stored picks remain untouched.
- Pick validity, save/load, and pick pipeline remain unchanged.

## Verification

`tools/verify_wc2026_group_stage_hides_later_round_pick_fills.py`
