# CAPTURE BACK — Sign-in Panel Over Game Board

## Change
Promote the Supabase identity sign-in backdrop and panel to a topmost fixed browser overlay.

## Files
- `site/css/app.css`
- `cards/277_sign_in_panel_over_game_board_card.md`
- `li/world_cup/sign_in_panel_over_game_board_rule.md`
- `tools/verify_wc2026_sign_in_panel_over_game_board.py`

## Verification
`tools/verify_wc2026_sign_in_panel_over_game_board.py` confirms the identity panel z-index outranks board floating surfaces and remains fixed viewport chrome.
