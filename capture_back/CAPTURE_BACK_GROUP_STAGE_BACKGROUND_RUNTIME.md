# Capture Back: Group-stage pub background runtime selection

## Summary

The visible site background has been switched back to the group-stage pub image for the current group-stage picking surface.

## Runtime authority

- `site/index.html` preloads `assets/board/pub_background_game1.jpeg`.
- `site/js/mvc/view.js` renders `assets/board/pub_background_game1.jpeg`.

## Boundary

The knockout pub/calendar background remains checked in for later knockout-mode work, but it is not the default runtime background in the current group-stage surface.

## Verification

`tools/verify_wc2026_group_stage_background_runtime.py` checks active runtime references, retained assets, LI/docs/card/capture evidence, and Makefile wiring.
