# Card 102 — Repair Game 1 Choice Legibility and Hit-Rule Integrity

## Intent

Make Game 1 chooser options readable and protect R32 hit-target menu integrity.

## Problem

Chooser option text can visually concatenate the team name and abbreviation, for example `FranceFRA`. Also, after moving Game 1 toward the SVG manifest board, R32 hit-target correctness must remain guarded so each selectable slot opens the right menu.

## Change

- Add LI for chooser option legibility.
- Render chooser rows with separate flag, team-name, abbreviation, and group spans.
- Add CSS spacing so team name and metadata cannot run together.
- Add verification that direct and third-place slot rules map to the intended eligible groups.

## Acceptance

- Team name and abbreviation have visible separation.
- Third-place rules remain group-pool filtered.
- Winner/runner-up rules remain single-group filtered.
- Existing Game 1 behavior remains intact.
