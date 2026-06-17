# Delete Pick Button Graphic

Pick menus may include a control that removes an existing pick. Earlier prototype wording used "UnPick". The production-facing menu should instead render a compact delete graphic.

The patch normalizes existing removal controls in place. It does not change their event handlers or storage behavior. This keeps the action safe while improving the visible wording.

Expected behavior:

- Existing pick-removal controls no longer visibly say "UnPick".
- The control renders as a trash/delete graphic with a compact "Delete" label on wider screens.
- On narrow screens the icon remains visible and the text is visually hidden.
- Accessibility metadata says "Delete pick".
