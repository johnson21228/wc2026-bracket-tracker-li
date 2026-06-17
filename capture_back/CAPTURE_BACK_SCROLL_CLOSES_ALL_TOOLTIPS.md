# Capture Back: Scroll Closes All Tooltips

## Summary

Scrolling the Game 1 board now closes tooltip surfaces.

## Decision

A tooltip is contextual to a pointer/focus moment. Once the view scrolls, the anchor position is no longer stable enough to keep the tooltip open.

## Rule

Scrolling, wheel movement, or touch movement must close all tooltip surfaces without changing the active pick or menu selection state.

## Evidence

- `site/game1/index.html`
- `tools/verify_wc2026_scroll_closes_all_tooltips_patch.py`
