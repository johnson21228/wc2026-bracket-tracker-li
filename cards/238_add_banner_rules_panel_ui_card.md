# Card 238: Add banner Rules panel UI scaffold

## Goal

Add a Rules button beside the developer-facing Game selector and display the rules for the selected active game in a scrollable panel.

## User story

As the developer, I want the banner Game selector to have an adjacent Rules button so I can preview Game 1 and Game 2 rules without wiring actual gameplay switching yet.

## Implementation notes

- Add a compact Rules button next to the existing developer Game selector.
- Add a scrollable rules panel with close behavior.
- Display Game 1 rules when Game 1 is selected.
- Display Game 2 rules when Game 2 is selected.
- Keep the selector and rules panel separate from board rendering, pick state, storage, scoring calculations, Supabase, routing, and data loading.

## Rules content

Game 1:

- Picks must be submitted before kickoff of the earliest third-round group-stage match.
- Some qualifiers may already be known at lock; many remain dependent on final group match results.
- Score 1 point per correctly predicted Round-of-32 team.

Game 2:

- Round scoring: R32 1, R16 2, QF 4, SF 8, Champion 16.
- Tiebreakers: Game 1 score, third-place pick, earliest valid Game 1 save timestamp before lock.

## Verification

`python3 tools/verify_wc2026_banner_rules_panel_ui.py`

The verifier checks:

- The banner includes a Rules button.
- The scrollable rules panel exists.
- Game 1 and Game 2 sections are present.
- Game 1 lock timing and Game 2 tiebreakers are visible in the HTML.
- Rules panel runtime is limited to UI open/close and active-section display.
- The verifier is registered in `make verify`.
