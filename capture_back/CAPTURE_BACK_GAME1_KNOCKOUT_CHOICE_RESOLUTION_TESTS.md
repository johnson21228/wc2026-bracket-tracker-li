# Capture Back — Game 1 knockout choice resolution tests

This capture adds a test rule and harness for Game 1 knockout choice menus.

The key invariant is that knockout menus are not group menus. They must resolve two contestants from the bracket path that feeds the selected slot.

Runtime behavior is still intentionally minimal; this capture exists to make the missing empty-menu condition observable.
