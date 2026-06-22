# Mouse double-click board zoom

The gameboard is moving toward a gesture-owned play surface. This feature adds a low-risk map-like gesture:

- mouse double-click on empty board space zooms in around the pointer
- pick buttons, group buttons, menus, panels, banner controls, rules controls, links, inputs, and zoom controls are excluded
- touch double-tap is not intercepted
- the existing `zoomBoardAroundPoint(...)` path performs the scale change so board clamping, select synchronization, and menu dismissal remain shared

This feature complements mouse drag-pan. It does not change pick logic, storage, scoring, Supabase, BracketDocument, Game 1/Game 2 data, or result data.

## Interaction contract

Double-click is a board gesture only when it starts on empty board/navigation surface. If it starts on an interactive control, that control remains responsible for the interaction.

Touch behavior remains unchanged in this feature. Touch pan/pinch, if desired, should be handled in a later dedicated gesture controller Capture Back.
