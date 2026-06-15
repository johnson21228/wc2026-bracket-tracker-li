WB_SESSION:
Capture Source-Adjacent Bracket Pod Layout

Changed:
- Captured the insight that results should be placed directly adjacent to their source games.
- Added LI rule preferring source-adjacent bracket pods over global spacer-based CSS alignment.
- Added feature note, implementation card, and prompt.

Decision captured:
- Current vertical spacing approach is too fragile.
- A better CSS model is nested pods:
  - R32 pair plus R16 result in one pod.
  - Two R16 pods compose into QF.
  - Two QF pods compose into SF.
  - SF pods compose into Final.
- This should improve visual clarity, screenshot readability, and bracket-state recovery.

Files added:
- `li/world_cup/source_adjacent_bracket_pod_layout_rule.md`
- `docs/features/source_adjacent_bracket_pods_note.md`
- `cards/015_replace_spacer_bracket_with_source_pods_card.md`
- `prompts/replace_spacer_bracket_with_source_pods.md`

Next:
- Apply overlay.
- Implement Card 015 as the next bracket layout iteration.
