WB_SESSION:
Capture Remove Sidebar-Bracket Gap

Changed:
- Captured the desired layout direction from the latest screenshots.
- The left team well and bracket should be adjacent with only a small gutter.
- Added LI rule, feature note, card, and prompt.

Decision captured:
- The large horizontal gap is not wanted.
- The current target is a compact split-screen:
  `narrow team well | bracket surface`
- The bracket should start close to the team well.
- This supports the compact flag-only bracket item direction.

Files added:
- `li/world_cup/remove_sidebar_bracket_gap_rule.md`
- `docs/features/remove_sidebar_bracket_gap_note.md`
- `cards/026_remove_sidebar_bracket_gap_card.md`
- `prompts/remove_sidebar_bracket_gap_from_html.md`

Next:
- Apply overlay.
- Implement the CSS/HTML layout change in the next static release.
