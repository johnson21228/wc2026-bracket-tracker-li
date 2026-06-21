# Capture Back: Remove Rules Panel Developer Note

## Intent

Remove the player-facing developer note from the Bracketeering Pub-Hub Rules panel.

The Rules panel should explain the player game, not expose implementation caveats such as the game selector being UI-only or not switching gameplay, scoring, storage, routes, Supabase state, data loading, or board rendering.

## Player-facing rule

Developer-only implementation caveats belong in LI/dev documentation, not in the Rules modal.

## Verification

tools/verify_wc2026_rules_panel_no_developer_note.py verifies that site/index.html no longer contains developer-only Rules panel caveats.
