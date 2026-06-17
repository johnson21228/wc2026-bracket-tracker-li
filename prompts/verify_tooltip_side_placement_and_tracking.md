# Verify Tooltip Side Placement and Tracking

Review Game 1 tooltip behavior.

Check that:

1. Tooltip appears beside the pick where possible.
2. Tooltip does not cover the underlying pick.
3. Tooltip stays open while moving from the pick into the tooltip.
4. Tooltip dismisses on outside tap/click or Escape.
5. Tooltip clickable action targets remain reachable.

Run:

    python3 tools/verify_wc2026_tooltip_side_placement_patch.py
    make verify
    make pack
