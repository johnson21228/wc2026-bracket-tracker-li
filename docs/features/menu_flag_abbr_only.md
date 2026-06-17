# Menu Flag + Abbreviation Only Rendering

The menu item rendering is normalized to match the R32 compact visual language. Instead of verbose country names, menu options render only a flag and a three-letter code.

This is a presentation-layer patch. It preserves menu option elements and their data attributes so existing event delegation and pick storage continue to work.

## Invariant
A menu option is a team identity control, not a text paragraph. Its visible rendering should be compact enough for mobile and board play.

## Expected behavior
- The board slot opens a choice menu.
- Menu rows show flag + code only.
- Selecting a row still writes the same pick.
- Long third-place menus still scroll internally.
- Board-attached menus remain attached during board scroll.
