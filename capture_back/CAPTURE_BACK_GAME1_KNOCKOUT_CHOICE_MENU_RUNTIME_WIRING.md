# Capture Back — Game 1 knockout choice menu runtime wiring

## Summary
Adds a runtime wiring layer so Game 1 R16/QF/SF winner-pick slots use resolved bracket contestants instead of falling through to the R32 group-eligibility choice path.

## Evidence
- Adds LI rule for knockout choice menu runtime wiring.
- Adds feature documentation and continuity card.
- Patches `site/game1/index.html` with a guarded runtime bridge.
- Adds verifier for the runtime wiring marker and essential functions.

## Non-goals
- Does not add Final/Champion picking.
- Does not change Game 2.
- Does not change R32 assignment eligibility rules.
