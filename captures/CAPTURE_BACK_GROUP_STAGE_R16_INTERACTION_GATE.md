# Capture Back: Group Stage R16+ Interaction Gate

## Problem

During Group Stage presentation, R16+ bracket cells are visually suppressed as frame-only cells, but they can still be interacted with.

Observed behavior:
- R16+ fill/label/team rendering is hidden during Group Stage.
- The cursor still changes to a pointing hand over R16+ cells.
- Clicking an R16+ cell still invokes the pick menu.

This creates a mismatch between the visual state and interaction state.

## Current verified code truth

The current View gate suppresses only visible pick fill through `shouldSuppressPickFillForSlot`.

But interaction remains active because pickable slots still get the pickable class and click handler.

The controller gate currently allows all slots through `slotAllowedForActiveGame`.

## Desired behavior

During Group Stage:
- R32 slots remain pickable.
- R16+ slots are frame-only.
- R16+ slots do not show pointer cursor.
- R16+ slots do not invoke the pick menu.
- R16+ direct controller actions are blocked even if a click/event reaches the controller.

During Knockout Stage:
- R16+ slots regain normal rendering and interaction.

## Product rule

Group Stage is not merely a visual suppression state for R16+ cells. It must also suppress R16+ pick-menu affordance and invocation.

This is an interaction gate, not a data/model gate:
- Existing R16+ picks may still exist in the model.
- Future-round picks may still be computable.
- But while Group Stage presentation is active, the player-facing UI must not advertise or open R16+ pick menus.

## Verification target

Add/extend verifier coverage proving:
- Group Stage R16+ fill suppression remains.
- Group Stage R16+ pick-menu interaction is blocked.
- `.is-pickable` is not applied to suppressed R16+ slots.
- Click handler does not invoke pick menu for suppressed R16+ slots.
- Controller has a backstop gate.
- Knockout Stage restores R16+ interaction.
