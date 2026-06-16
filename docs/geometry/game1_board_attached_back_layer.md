# Game 1 Board-Attached Back Layer

This capture makes Game 1 use an explicit visual back layer behind the shared pixel-native board image.

Layer order for Game 1:

1. Board-attached pub/background layer
2. Optional wash layer
3. Shared 1536 × 1024 RGBA game board PNG
4. Game title / labels
5. Pixel-native hit targets and rendered picks

The back layer must scroll with the board because it belongs to the board surface, not to the browser viewport.
