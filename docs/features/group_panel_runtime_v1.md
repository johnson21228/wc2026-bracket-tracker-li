# Group Panel Runtime v1

The group panel is an evidence surface for the pick menu. When a user sees a group label in a pick menu, clicking that label opens the panel for that group.

The panel explains the group source behind the pick choice without changing bracket state.

## Runtime contract

- The model owns group context.
- The view renders the panel.
- The controller opens/closes the panel.
- The runtime consumes local checked-in data from `site/data/current/`.
- No runtime scraping or remote standings calls are allowed.

## Panel content

The panel displays:

- group label
- source/capture status
- standings table
- qualification context
- completed matches
- upcoming matches
- optional verified highlight links when present in local data

## Match evidence rule

For each group match:

- If the match is completed, show the result as the primary evidence.
- If the match is not completed, show the scheduled kickoff time.
- If kickoff time is missing, show `Time TBD`.
- If a completed match has a highlight URL in the checked-in highlight model, render the completed match card as an external link.
- External highlight links open in a new browser tab/window with `target="_blank"` and `rel="noopener noreferrer"`.
- If no highlight URL exists, render the match as static evidence.
- The runtime must not invent highlight links.

## Pick safety

Opening and closing the group panel must not select a team, clear a pick, close the pick menu unexpectedly, or recompute bracket eligibility in the view.

## Deferred

Third-place source-slot semantics are intentionally out of scope for this card.
