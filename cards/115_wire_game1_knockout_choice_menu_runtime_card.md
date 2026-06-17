# Card 115 — Wire Game 1 knockout slots to resolved contestant choice menu

## Intent
Make Game 1 knockout winner slots open a two-contestant choice menu when the two feeding contestants are already known.

## Scope
- R16 slots choose between the two feeding R32 picks.
- QF slots choose between the two feeding R16 winner picks.
- SF slots choose between the two feeding QF winner picks.
- Existing R32 group/team choice behavior remains unchanged.
- Game 2 remains unchanged.

## Acceptance
- Command-line resolver tests continue to pass.
- Runtime candidate resolution supports manifest slot IDs and normalized slot IDs.
- A tapped ready knockout slot does not fall through to the R32 group-eligibility menu.
- Empty/waiting state is used only when a feeding contestant is actually missing.
