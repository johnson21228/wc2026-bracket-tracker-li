# Card 246: Floating Surface Dismissal Is View-Owned

## Goal

Allow a tap/click outside an open pick menu or group panel to close it safely.

## Design

This is View-owned behavior.

The controller continues to own pick state and pick rules. The View owns transient floating UI dismissal.

## Acceptance

- Clicking outside an open MVC pick menu closes it.
- Clicking outside an open MVC group panel closes it.
- Clicking outside an open R32 pick menu closes it.
- Clicking inside a menu or panel does not close it prematurely.
- Escape closes open floating surfaces.
- No controller dependency is introduced.

## Verification

Run:

- `python3 tools/verify_wc2026_floating_surface_dismissal_view_owned.py`
- `make verify`
