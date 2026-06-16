# Shared Background Scrolls With Board Rule

Game 1 and Game 2 use a shared pixel-native game board plane. The pub/background layer must move with that plane.

The background is still not geometry truth. The board PNG remains the 1536 × 1024 pixel-native geometry authority. However, the background must be attached to the same board plane or a child layer of that board plane, not to the browser viewport.

Required invariant:

- The browser may scroll the page or board viewport.
- The background, board image, hit layer, and render layer scroll together as one stack.
- The background must not use `background-attachment: fixed`.
- The body/page may have a dark fallback color, but it must not be the active pub scene layer.
- Game 1 and Game 2 may differ in behavior, but their visual layer stack must preserve the same board-plane coordinate relationship.
