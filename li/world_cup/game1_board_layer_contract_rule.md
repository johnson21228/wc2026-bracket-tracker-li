# LI Rule — Game 1 Board Layer Contract

Game 1 must preserve separation between visual board art and playable state.

- The background image is decorative.
- The transparent bracket PNG is decorative.
- The slot hit targets are DOM/runtime elements.
- The chooser is runtime logic filtered by the selected slot rule.

Do not restore a monolithic opaque board image as the primary play surface. Do not bake slot numbers, hit testing, or team choices into the bracket PNG.
