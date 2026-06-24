# Capture Back: Info Panel Player Copy Refresh

## Change
Updated the player-facing Bracketeering info panel copy and added Group Stage Picks lock behavior.

## Intent
Make the info panel friendlier and clearer for invitees:
- Explain that this is Steve's fun hobby project.
- Mention the $50 winner prize.
- Encourage players to join.
- Warn email users to check spam/junk for verification.
- Explain the two game parts: Group Stage Picks and Knockout Round Picks.
- Clarify that Group Stage Picks are optional and used as a tiebreaker.
- Keep the red-pick conflict explanation visible.
- Explain that Knockout Round Picks happen after the Round of 32 is determined.
- Use lock-time language for Group Stage Picks.
- Explain that Round of 32 picks cannot be changed after the Group Stage Picks lock.
- Hide player standings/results until Group Stage Picks lock.

## Verification
- `python3 tools/verify_wc2026_banner_rules_panel_ui.py`
- `python3 tools/verify_wc2026_rules_panel_no_developer_note.py`
- `python3 tools/verify_wc2026_group_stage_pick_lock_gate.py`
- `make verify`
- `make pack`
