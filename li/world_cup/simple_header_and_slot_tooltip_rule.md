# Simple Header And Slot Tooltip Rule

## Purpose

The static HTML site should be immediately understandable to casual users.

The top of the page should not over-explain the Workbench. The public UI should be simple.

## Header rule

Use a simple title such as:

```text
World Cup 2026 Bracket Builder
```

or:

```text
World Cup Bracket Pool
```

## Instruction rule

The top instructions should be short and action-oriented.

Suggested text:

```text
Drag teams into the bracket. Scroll sideways to see the full bracket.
```

Optional second line:

```text
Use Export State to save or share your picks.
```

## Workbench explanation rule

Workbench source/history/governance belongs in the repo and optional About/Details sections, not in the primary page header.

## Round-of-32 tooltip rule

Each Round-of-32 slot should have a tooltip that explains how the team is assigned.

Examples:

```text
Winner Group A
Runner-up Group B
Best third-place team from Groups C/D/E/F
```

## Tooltip storage rule

Tooltip text should be stored with the slot rule data, not hard-coded only in HTML.

Example:

```json
{
  "slotId": "R32-M1-A",
  "label": "Winner Group A",
  "tooltip": "This slot is assigned to the winner of Group A after group-stage results are official.",
  "status": "pending"
}
```

## UX rule

The tooltip should appear through at least one browser-native mechanism, such as the `title` attribute.

Later versions may add custom tooltip styling, but the first implementation may use native browser tooltips.

## Acceptance

- The page title is shorter and clearer.
- Instructions tell the user to drag/drop and scroll.
- Round-of-32 slots expose tooltip text.
- Tooltip data is preserved in exported/imported state.
