# Card 209: Capture interaction overlay stack

## Intent

Ensure pick menus and group panels always appear above the bottom group rail/frame, and ensure group panels appear above pick menus.

## Changes

- Add LI for interaction overlay stacking.
- Add feature documentation.
- Add CSS z-index tokens and layer rules.
- Add verifier wired into `make verify`.

## Acceptance

- The group rail remains below transient interaction surfaces.
- Pick menu layers render above bottom-frame controls.
- Group panel layers render above pick menus.
- Pointer events are preserved on visible popovers.
