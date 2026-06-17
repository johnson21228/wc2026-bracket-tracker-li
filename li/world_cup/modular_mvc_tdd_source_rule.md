# Modular MVC/TDD Source Rule

## Purpose

The WC2026 Bracket Tracker should follow the modular architecture identified in the inventory review.

Do not preserve or introduce a monolithic HTML portability goal. An HTML entry point may exist, but it must not become the architectural target or the place where all rules accumulate.

## Rule

The application source should move toward clear model, view, and controller boundaries:

- **Model**: tournament facts, team data, group data, bracket geometry, slot definitions, pick state, scoring inputs, and persistence schemas.
- **View**: board rendering, menu rendering, flag/card rendering, visual states, layout, and review surfaces.
- **Controller**: user events, menu opening/closing, candidate resolution orchestration, pick application, dependent-pick clearing, and rerender coordination.

Tournament rules, geometry authority, choice eligibility, pick storage, and advancement logic must not be added directly to an HTML page as the default implementation path.

## TDD rule

Behavioral fixes should add or update a durable test before or alongside the fix.

Prioritize tests for:

- R32 slot-to-candidate rules
- third-place candidate pools
- knockout feeder resolution
- pick storage and export/import shape
- downstream invalidation after a changed pick
- Game 1 and Game 2 state separation
- geometry-slot coverage
- menu open/close state

## Release posture

The public site may remain static-hostable and GitHub Pages compatible, but that is a deployment property, not a source architecture goal.

The desired source structure is modular. If a build step is needed later, the Workbench should capture that build step and verify its output instead of reverting to monolithic source.

## Anti-drift rule

Do not add new LI, prompts, or cards that encourage a monolithic HTML implementation as a virtue.

When old Capture Back records mention static HTML releases, treat those as history, not as current architectural direction.
