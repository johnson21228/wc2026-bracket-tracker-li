# Capture Back — Group Panel Runtime v1

## Change

Implemented a first runtime version of the group panel as a visible evidence surface opened from pick-menu group labels.

## Runtime boundary

The browser runtime reads checked-in model data only. It does not fetch, parse, or scrape ESPN at runtime.

## Behavior

The group panel presents:

- group header and close affordance
- source/capture status from the local normalized snapshot
- standings table with rank, team, MP, W, D, L, GF, GA, GD, points, and qualification context
- completed match evidence with results
- upcoming match evidence with kickoff time, or `Time TBD` when kickoff is missing
- optional highlight links when present in `site/data/current/match_highlights.json`

Completed match highlight behavior:

- If a completed match has a highlight URL in local checked-in data, the match evidence card renders as an external link.
- The link opens in a new browser tab/window using `target="_blank"` and `rel="noopener noreferrer"`.
- If no highlight URL exists, the completed match renders as static evidence.
- The runtime must not invent highlight links.

Opening or closing the panel does not select, clear, or mutate bracket picks.

## Deferred

This card intentionally does not change third-place menu semantics or FIFA third-place source-slot allocation.

## Verification

Added `tools/verify_wc2026_group_panel_runtime_v1.py` and wired it into `make verify`.
