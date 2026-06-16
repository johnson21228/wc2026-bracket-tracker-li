# Shared Background Scrolls With Board

This capture corrects the background relationship for the shared pixel-native board.

The pub background should be part of the game board stack, not a fixed browser background. When the user scrolls the native 1536 × 1024 board surface, the atmosphere, board PNG, control layer, and rendered items must all move together.

Layer order:

1. Board-attached pub/background layer
2. 1536 × 1024 RGBA game board PNG
3. Pixel-native hit/control regions
4. Rendered bracket items

The body only supplies a dark fallback color.
