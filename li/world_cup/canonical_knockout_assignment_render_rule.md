# Canonical Knockout Assignment Render Rule

A knockout choice menu is the assignment surface for the bracket cell that opened it.

The canonical assignment path is:

1. opening cell becomes the assignment target
2. selected team is normalized with assignment metadata
3. selected team is stored under the target slot id
4. target slot is rendered with the selected team
5. menu closes

A later wrapper may not bypass this path or turn the menu into a detached chooser.
