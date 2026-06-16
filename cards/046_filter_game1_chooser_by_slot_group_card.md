# Card 046 — Filter Game 1 Chooser by Slot Group

## Intent
When a player clicks a Round-of-32 slot, the chooser must only offer teams from the group or groups named by that slot rule.

## Change
- Direct rules such as `1A` or `2F` show only Group A or Group F teams.
- Third-place rules such as `3 A/B/C/D/F` show only teams from those listed groups.
- The chooser displays the active group filter in the modal text.
- The duplicate JavaScript state block is removed if present so the page can parse.
