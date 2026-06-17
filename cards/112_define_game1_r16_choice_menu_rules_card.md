# Card 112 — Define Game 1 R16 Choice Menu Rules

## Intent
Define the rule authority for Game 1 Round of 16 winner-pick menus before additional runtime behavior is added.

## Rule
An R16 pick is not chosen from all teams or from group eligibility rules. It is chosen only from the two resolved teams in the two R32 source slots that feed that R16 slot.

## Acceptance
- Every R16 slot has exactly two R32 source slots.
- The R16 choice menu opens only when both source R32 slots have assigned teams.
- The choice menu presents exactly those two teams.
- R16 picks are stored separately from R32 assignment picks.
- The R16 destination slot records which source team advanced.
- The rule is written as LI before deeper R16/QF/SF/Final Four behavior is added.

## Status
Reference/rule card. Runtime may be patched separately after this rule is accepted.
