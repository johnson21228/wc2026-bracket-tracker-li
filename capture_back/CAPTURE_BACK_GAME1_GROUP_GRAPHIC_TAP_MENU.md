# Capture Back — Game 1 Group Graphic Tap Menu

Game 1 now uses the shared pixel-native board foundation and restores the liked tap-to-pick menu interaction.

The user taps an R32 slot. A group/team chooser opens with Group A–L chips and compact team graphic tiles. Assignments are stored in localStorage and export includes board metadata and slot pixel definitions.

This preserves the architecture:

```text
Shared board resources.
Separate Game 1 behavior.
No duplicate board geometry.
```
