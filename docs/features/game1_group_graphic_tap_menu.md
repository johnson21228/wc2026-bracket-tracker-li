# Game 1 Group Graphic Tap Menu

This restores the Game 1 tap-to-pick menu on top of the shared board surface.

The board remains the shared 1536 × 1024 RGBA PNG. Game 1 adds one assignment layer with 32 pixel-native R32 hit targets. Tapping a slot opens the grouped team chooser. The chooser uses Group A–L chips and compact team graphic tiles so the user can pick from the group menu rather than a plain unstructured list.

This does not alter Game 2. Game 2 remains separate board/advancement behavior.

Future work can replace the current generated graphic tiles with official flag art while preserving the same tap-menu contract.
