# Pick Menu Group Panel Link Rule

## Rule

Any pick menu that displays group-qualified World Cup choices must preserve visible group context.

A pick menu must not flatten all teams into an ungrouped list when the choice source is group-based. It must collect choices by group, show the group label for each group collection, and make the group label an interactive affordance that opens the group standings panel for that group.

## Applies to

- Round-of-32 slot pick menus.
- Third-place slot pick menus.
- Any future bracket, standings, or prediction surface that offers choices derived from a World Cup group.

## Required behavior

1. The model provides the group identity for each group-derived choice.
2. The view renders group-derived choices collected under a visible group label, such as `Group A`.
3. The group label is clickable/tappable.
4. Activating the group label opens the group standings panel for that same group.
5. The group standings panel is the shared context surface for group details; the pick menu does not duplicate the full table unless explicitly designed to do so.
6. Keyboard and pointer users must be able to trigger the group label affordance.

## R32 pick menu behavior

For a direct group slot such as `1A` or `2C`, the pick menu should display the applicable group label and show the candidate choices inside that group context.

For a third-place source slot such as `3RD A/E/H/I/J`, the pick menu should collect possible choices by their source groups. Each group label opens that group’s standings panel.

If the third-place source has already been resolved to a single group, the menu should still show that resolved group label so the user can inspect the source standings.

## MVC boundary

- The model owns choice eligibility and group identity.
- The view owns grouped rendering, visible group labels, and the clickable affordance.
- The controller owns the event that opens the group standings panel for the selected group.
- The site runtime reads local checked-in model data; it must not scrape ESPN or other live pages from inside the browser.

## Source boundary

The group standings panel may be refreshed during Capture Back from a source URL such as the ESPN FIFA World Cup standings page, but the pick menu consumes only normalized WB model data.

## Anti-patterns

- Do not render group-derived pick choices as a single ungrouped list.
- Do not hide the group label behind only a tooltip.
- Do not make group labels merely decorative text.
- Do not wire the group label to an external standings URL from the browser runtime.
- Do not duplicate ESPN/FIFA scraping logic inside the pick menu.
