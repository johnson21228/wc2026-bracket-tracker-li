# R32 Pick Card Font Metrics Rule

Round of 32 pick cards must use fixed shared font metrics chosen against the complete 48-team display-name set.

## Rule

The board slot rectangle is the geometry authority. The pick card must not grow to fit a team name.

The card renderer must choose one shared card-name font size, line height, padding, gap, and flag box size that works for the full tournament team-name set.

## Required behavior

- The flag should be as large as the slot height permits while preserving card padding and border.
- The team name must fit inside the remaining width using the same font metrics for all teams.
- Team names may wrap to two lines when necessary.
- Long names should use approved display breaks, not per-team font-size shrinking.
- The compact card should not show slot-rule metadata on the card face; that belongs in tooltip/details.
- The compact card must remain inside the slot `boundsPx` supplied by the board/rule data.

## Current Game 1 R32 metric target

For a 148 × 40 pixel slot:

- card box: exactly slot bounds
- horizontal padding: 6px
- vertical padding: 3px
- flag box: 34px wide, 32px high
- gap: 6px
- team-name font size: 14px
- team-name line height: 14px
- maximum lines: 2

These metrics are chosen so all current 48 team display names can be represented without changing font size per team.

## Boundary

Tournament Data owns the team display names.
UI Surface owns the card metrics and approved display breaks.
Board Geometry owns the slot rectangle.
Game 1 and Game 2 own pick state, not card sizing.
