# Card 287 — Capture Group B Complete Results

## Goal
Update the current World Cup group-stage data now that Group B has completed its final matchday.

## Changes
- Mark Switzerland 2-1 Canada final.
- Mark Bosnia-Herzegovina 3-1 Qatar final.
- Recalculate Group B standings.
- Refresh the provisional third-place table so Bosnia and Herzegovina is represented as Group B's third-place team.
- Add a score-only evidence artifact for the June 24 Group B capture.

## Verification
`tools/verify_wc2026_group_b_complete_results.py` checks the two final match rows, Group B standings, third-place table state, evidence artifact, capture note, card, and Makefile integration.
