# Card 265: Floating board surfaces above overlay controls

## Status

Implemented

## Problem

The login control and other fixed app overlay chrome can visually sit above a pick menu or group panel.

## Decision

Pick menus and group panels are transient board-owned floating surfaces and should render above fixed app overlay controls while open.

## Verification

`tools/verify_wc2026_floating_board_surfaces_above_overlay_controls.py`
