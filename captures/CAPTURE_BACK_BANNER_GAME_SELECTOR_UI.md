# Capture Back: Banner Game Selector UI

## Intent

Add a developer-facing Game selector to the Bracketeering banner/header as UI scaffolding only.

## Scope

The selector lets a developer visually choose between Game 1 and Game 2 in the banner. It does not switch the active board, picks, scoring, storage, route, Supabase state, or data model.

## Runtime boundary

This capture intentionally keeps the behavior at the DOM/CSS level:

- Game 1 is checked by default.
- Game 2 can be selected visually.
- No JavaScript controller, model, storage, or board behavior consumes the selector yet.

The purpose is to reserve and verify the UI affordance before implementing game-mode behavior.

## Acceptance

- The banner includes a developer-facing Game selector.
- The selector includes Game 1 and Game 2 options.
- Game 1 is selected by default.
- Selecting Game 2 only changes the selected control state.
- Existing Game 1 board behavior remains unchanged.
- A verifier confirms the control exists and is not wired into runtime switching logic.
