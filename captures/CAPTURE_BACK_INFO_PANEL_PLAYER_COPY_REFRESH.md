# Capture Back: Info Panel Player Copy Refresh

## Change
Updated the player-facing Bracketeering info panel copy.

## Intent
Make the info panel friendlier and clearer for invitees:
- Explain that this is Steve's hobby project.
- Mention the $50 winner prize.
- Encourage players to join.
- Warn email users to check spam/junk for verification.
- Explain the two game parts: Group Stage Picks and Knockout Round Picks.
- Clarify that Group Stage Picks are optional and used as a tiebreaker.
- Keep the red-pick conflict explanation visible.
- End with a friendly reminder to have fun and use group buttons for standings.

## Verification
- `python3 tools/verify_wc2026_banner_rules_panel_ui.py`
- `python3 tools/verify_wc2026_rules_panel_no_developer_note.py`
- `make verify`
- `make pack`
