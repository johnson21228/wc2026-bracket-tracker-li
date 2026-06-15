# Simple Header And Slot Tooltips Note

## UI refinement

The public page should start simply.

Recommended top:

```text
World Cup 2026 Bracket Builder

Drag teams into the bracket. Scroll sideways to see the full bracket.
Use Export State to save or share your picks.
```

The Workbench story is important, but it should not crowd the user-facing top of the site.

## Slot tooltips

Round-of-32 bracket slots should explain what kind of team goes there.

Example:

```text
Winner Group A
```

Tooltip:

```text
This slot is assigned to the winner of Group A after group-stage results are official.
```

This helps because the bracket may be partially known before team assignments are resolved.

## First implementation

Use the HTML `title` attribute for the first version.

Later implementation can use styled tooltips.
