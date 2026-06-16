# Game 1 Group Graphic Tap Menu Rule

Game 1 uses the shared 1536 × 1024 pixel-native board as its visual and geometric foundation.

When the user taps an R32 slot, Game 1 must open the group/team chooser menu, not a free-floating page panel. The chooser must preserve the liked interaction pattern:

- it opens from the tapped R32 slot interaction;
- it exposes Group A through Group L as visible menu chips;
- it filters visible teams by the active group;
- it renders team choices with a compact graphic tile and group metadata;
- it records assignments in localStorage;
- it keeps hit/render slot geometry in native board pixels.

The group menu is Game 1 behavior. It must not change Game 2 behavior.

The canonical board image remains:

```text
site/assets/playfield/r32_bracket_geometry_overlay.png
```
