# 50% zoom floating-surface placement

The board can now be zoomed out to 50%. At that scale, a menu that used to fit beside or below a button may collide with the bottom rail, fall outside the visible board area, or appear behind controls.

The runtime now treats pick menus and group panels as floating surfaces with a common safe-area rule. Each surface is positioned from rendered screen coordinates using `getBoundingClientRect()`, then clamped inside a visible safe rectangle. The safe rectangle excludes bottom controls, including the group rail.

## Manual QA

1. Open the site.
2. Set board zoom to 50%.
3. Open a left-side R32 pick menu.
4. Open a right-side R32 pick menu.
5. Open a lower-board pick menu near the bottom controls.
6. Open a group panel from the group rail.
7. Open a group panel from a group link inside a pick menu.
8. Confirm every surface is fully visible, scrolls internally if needed, and appears in front of bottom controls.

## Invariant

Bottom controls may remain visible, but pick menus and group panels must be above them in the overlay stack while open.
