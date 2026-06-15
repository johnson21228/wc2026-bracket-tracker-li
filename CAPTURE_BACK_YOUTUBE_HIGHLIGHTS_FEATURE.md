WB_SESSION:
Capture YouTube Highlights Feature For WC2026 Bracket Tracker

Changed:
- Added optional YouTube highlight support as a governed match enrichment feature.
- Clarified that match highlights are not official result authority.
- Added LI rule for preferred highlight source order, required metadata, and Capture Back requirements.
- Added JSON schema and example match metadata for highlights.
- Added feature note, card, and prompts for implementing the static HTML UI.
- Preserved uploaded `workbench-li-template.pack(47).zip` as source artifact context for creating or continuing the repo from template.

Product behavior captured:
- The public site can become more alive over time by adding highlights per match.
- The WB keeps enrichment data separate from official tournament truth and player scoring.
- Each highlight update can be CB’d and included in the next static HTML release.

Files added:
- `li/world_cup/youtube_highlight_enrichment_rule.md`
- `data/schema/match_highlight_schema.json`
- `data/schema/match_with_highlight_example.json`
- `docs/features/youtube_highlights_feature_note.md`
- `cards/007_add_youtube_highlights_to_match_cards_card.md`
- `prompts/add_youtube_highlights_to_html.md`
- `prompts/capture_back_youtube_highlight_update.md`
- `tools/extract_youtube_id_note.md`

Next:
- Apply this overlay to the WC2026 Bracket Tracker LI repo.
- Continue with Game 1 Round-of-32 pick UI.
- Later add highlight UI to match cards and release the next static HTML.
