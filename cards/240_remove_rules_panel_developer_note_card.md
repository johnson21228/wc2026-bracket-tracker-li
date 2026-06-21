# Card 240: Remove Rules Panel Developer Note

## Goal

Keep the Bracketeering Pub-Hub Rules panel player-facing by removing the developer note about the temporary UI-only game selector.

## Scope

- Remove the developer-note heading and paragraph from site/index.html.
- Preserve the Game 1 / Game 2 selector itself.
- Preserve the current Game 1 and Game 2 rules text.
- Add verification that the developer note does not return to the player-facing Rules panel.

## Verification

Run python3 tools/verify_wc2026_rules_panel_no_developer_note.py and make verify.
