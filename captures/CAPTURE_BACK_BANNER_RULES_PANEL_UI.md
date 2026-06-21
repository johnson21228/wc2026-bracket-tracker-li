# Capture Back: Banner Rules Panel UI

## Intent

Add a Rules button beside the developer-facing Game selector and show a scrollable rules panel for the selected active game.

## Scope

This capture keeps the Game selector as UI scaffolding. The Rules button reads the selector's current visible state and displays either Game 1 or Game 2 rules text. It does not switch board behavior, scoring, storage, routes, Supabase state, data loading, or gameplay runtime.

## Rules shown

Game 1 rules explain:

- Pick the Round-of-32 field before the final group-stage round begins.
- Game 1 locks before kickoff of the earliest third-round group-stage match.
- Some Round-of-32 places may already be known by then, while many remain dependent on final group results.
- Scoring is 1 point for each correctly predicted Round-of-32 team.

Game 2 rules explain:

- Pick knockout winners through the bracket after the knockout bracket is available.
- Scoring escalates by round: 1, 2, 4, 8, and 16 points.
- Tiebreakers are Game 1 score, third-place pick, then earliest valid Game 1 save timestamp before lock.

## Runtime boundary

- The Rules button opens and closes a scrollable panel.
- The panel displays the rules for the currently selected Game selector value.
- Selecting Game 2 only changes the visible selector state and the rules text shown.
- No gameplay switching is implemented.

## Acceptance

- Banner includes a Rules button next to the developer Game selector.
- Rules panel opens and closes.
- Rules panel includes Game 1 and Game 2 rules sections.
- Active section follows the selected visible Game selector value.
- Existing board behavior remains unchanged.
- Verifier confirms the rules UI exists and remains unwired from gameplay switching.
