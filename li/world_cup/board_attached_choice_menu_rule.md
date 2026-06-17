# Board-Attached Choice Menu Rule

Choice menus must be anchored to the bracket board surface.

Rules:

- Board scroll must not dismiss a choice menu.
- Board scroll should move the menu with the board.
- Menu scroll should remain internal when a long menu has more candidates than fit on screen.
- A choice menu may close on selection, outside tap, explicit close, or switching to another slot.
- Scroll-close behavior may remain for explanatory tooltips, but must not close pick/choice menus.

This rule protects phone and iPad browsers where a tap can be followed by touchmove, scroll, or visual viewport adjustment events.
