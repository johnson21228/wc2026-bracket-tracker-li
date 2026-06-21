# Capture Back: Floating Surface Dismissal Is View-Owned

## Intent

Add a clean, safe gesture for closing open floating UI surfaces.

## Scope

This is View-owned UI behavior only.

It closes:

- MVC pick menus
- MVC group panels
- R32 pick menu popovers

It does not change:

- controller pick rules
- bracket data
- BracketDocument storage
- Supabase seams
- current result JSON data

## Behavior

A pointer/tap outside an open floating surface dismisses it.

Escape also dismisses the open floating surface.

Clicks inside the menu or panel are ignored so buttons, links, highlights, and group-panel actions keep working.

## Implementation

A shared `FloatingSurfaceDismissal` service owns the DOM event pattern.

The MVC View wires it to close both the pick menu and group panel.

The R32 pick-menu layer wires it to close the R32 menu.

## Verification

`tools/verify_wc2026_floating_surface_dismissal_view_owned.py` verifies the shared service, View-owned wiring, R32 wiring, and absence of controller dependencies.
