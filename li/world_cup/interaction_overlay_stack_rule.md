# Interaction Overlay Stack Rule

Card 209.

Interactive inspection surfaces must render above board-frame controls.

## Rule

The board may have lower-frame controls such as the group button rail, and it may have transient inspection surfaces such as the R32 pick menu and the group standings panel. The transient inspection surfaces are the top interaction layers.

Layer order, from back to front:

1. board background and rendered bracket cells
2. bottom frame controls, including the group button rail
3. pick menu layer
4. group standings panel layer

The group standings panel must be above the pick menu when both are present. The pick menu and group panel must be above the bottom frame controls so that a bottom rail button, group flag tile, or frame element cannot cover or intercept a menu/panel.

## Pointer behavior

The layer containers may be non-interactive, but their visible popovers must accept pointer events. This keeps the board from gaining accidental hit targets while preserving click/tap behavior on the popover controls.

## Boundary

This rule does not change which teams are eligible for a slot. It only defines visual and hit-test stacking for already-open interaction surfaces.
