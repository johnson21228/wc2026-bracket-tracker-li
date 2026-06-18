# Capture Back: Current Group Order Rendering

## Summary

Captured the rule that group-scoped team displays should use current standings order when standings are available.

## Runtime impact

The Model now exposes group teams in standings order for:

- R32 pick choice ordering
- grouped pick-menu sections
- group rail flag grids

The group panel already renders from standings entries and remains aligned with this contract.

## Verification

`tools/verify_wc2026_current_group_order_rendering.py` confirms the LI/docs/card/capture files, Makefile wiring, model helper usage, and Group A expected order `MEX, KOR, CZE, RSA`.
