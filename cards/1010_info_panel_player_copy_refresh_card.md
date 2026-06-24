# Card 1010: Info Panel Player Copy Refresh

## Goal
Refresh the Bracketeering info panel copy so it reads like a friendly player invitation instead of a dry rules panel, and add the Group Stage Picks lock behavior.

## Files
- `site/index.html`
- `site/js/config/gameLocks.js`
- `site/js/controllers/Game1R32PickController.js`
- `site/js/board/R32PickMenuLayer.js`
- `site/js/standings/PlayerStandingsSurface.js`
- `tools/verify_wc2026_banner_rules_panel_ui.py`
- `tools/verify_wc2026_rules_panel_no_developer_note.py`
- `tools/verify_wc2026_group_stage_pick_lock_gate.py`
- `captures/CAPTURE_BACK_INFO_PANEL_PLAYER_COPY_REFRESH.md`
- `Makefile`

## Acceptance
- Info panel includes Steve's friendly invitation and contact line.
- Info panel mentions the $50 prize.
- Info panel tells email joiners to check spam/junk.
- Info panel explains Group Stage Picks and Knockout Round Picks.
- Info panel explains Group Stage Picks are optional and used as a tiebreaker.
- Info panel explains Knockout Round Picks happen after the Round of 32 is determined.
- Info panel uses Group Stage Picks lock language.
- Round of 32 picks cannot be changed after Group Stage Picks lock.
- Player standings/results stay hidden until Group Stage Picks lock.
- Existing info-panel verifiers pass.
