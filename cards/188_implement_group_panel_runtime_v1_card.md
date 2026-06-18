# Card 188 — Implement Group Panel Runtime v1

## Intent

Upgrade the visible group panel from a standings-only stub into a local-data evidence surface opened from pick-menu group labels.

## Scope

- Keep the group panel local-data only.
- Use checked-in `site/data/current/group_standings.json`, `site/data/current/group_matches.json`, and `site/data/current/match_highlights.json`.
- Show full standings, qualification context, completed match results, upcoming match kickoff times, and source/capture status.
- Render completed matches with verified highlight URLs as external links that open in a new browser tab/window using `target="_blank"` and `rel="noopener noreferrer"`.
- Render completed matches without highlight URLs as static evidence, not broken or disabled buttons.
- Do not mutate bracket picks when opening or closing the group panel.
- Do not change third-place source-slot semantics in this card.

## Acceptance

- `model.getGroupContext(groupId)` returns entries, completed matches, upcoming matches, optional highlight data, and source metadata.
- `view.renderGroupPanel(groupContext)` renders full standings and match evidence.
- Completed matches show results as primary evidence.
- Incomplete matches show kickoff time, or `Time TBD` when no kickoff exists.
- Highlight links are optional and local-data-only.
- The group panel is visible above the board and pick menu layers.
- The runtime still verifies and packs.
