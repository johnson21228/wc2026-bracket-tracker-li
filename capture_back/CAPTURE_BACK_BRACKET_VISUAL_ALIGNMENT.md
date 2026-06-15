WB_SESSION:
Capture Bracket Visual Alignment Rule

Changed:
- Captured requirement that R16 and later rounds should be vertically aligned with their R32/later source matches.
- Added LI rule for bracket visual alignment.
- Added schema for source alignment mapping.
- Added feature note, card, and prompt.

Decision captured:
- R16 slots should sit centered between the two R32 matches that feed them.
- QF slots should sit centered between the two R16 slots that feed them.
- SF slots should sit centered between the two QF slots that feed them.
- Final should align from SF source slots.
- The bracket should be screenshot-friendly and visually recoverable.

Files added:
- `li/world_cup/bracket_visual_alignment_rule.md`
- `docs/features/bracket_visual_alignment_note.md`
- `cards/011_align_knockout_rounds_to_source_matches_card.md`
- `prompts/align_knockout_rounds_to_source_matches.md`
- `data/schema/bracket_round_source_alignment_schema.json`

Next:
- Apply overlay.
- Implement with Card 010/simple header and Card 011/bracket alignment in the next static HTML release.
