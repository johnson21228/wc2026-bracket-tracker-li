# Capture Back — Pick Menu Runtime v2

## What changed

This Capture Back implements the Pick Menu LI in the clean MVC runtime.

The runtime now treats the pick menu as a model-described, board-attached interaction surface. The model returns grouped pick-menu data; the view renders grouped sections, clickable group labels, a clear-pick affordance near the top, and a prominent close button; the controller routes team selection, clear, close, and group-panel actions separately.

## Boundary

The browser runtime reads local checked-in data only. It does not scrape ESPN or any external standings page.

## Follow-up

The first group panel is intentionally functional and simple. A later UI polish pass may improve its table layout and visual design without changing the pick-menu action boundary.
