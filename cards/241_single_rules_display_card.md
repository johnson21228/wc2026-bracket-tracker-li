# Card 241: Single Rules Display

## Goal

Make the Rules modal a single player-facing Bracketeering Pub-Hub explanation instead of separate Game 1 and Game 2 displays.

## Scope

- Replace selector-driven Rules sections with one rules section.
- Remove `Showing Game 1 rules` / `Showing Game 2 rules`.
- Remove `data-rules-panel-section` usage from the Rules panel.
- Simplify the Rules panel runtime so it opens and closes only.
- Explain the Dev Game View selector as a development preview tool.
- Encourage current viewers to play Game 1 and simulated Game 2.
- Preserve the selector itself for development preview of the board.
- Preserve the no-developer-note invariant.

## Verification

Run:

- `python3 tools/verify_wc2026_banner_rules_panel_ui.py`
- `python3 tools/verify_wc2026_rules_panel_no_developer_note.py`
- `make verify`
