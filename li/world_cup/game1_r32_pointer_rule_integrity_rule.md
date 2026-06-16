# Game 1 R32 Pointer Rule Integrity Rule

When Game 1 uses the uniform SVG gameboard manifest, the chooser rule must be selected from the manifest slot under the pointer.

The visible R32 slot, its hit target, its rendered pick card, and the chooser menu must resolve to the same `slotId` and slot rule.

This prevents off-by-one or neighboring-target errors where a user taps a visible third-place pool slot but the menu opens for an adjacent group-winner slot.

Requirements:

- Game 1 R32 hit testing must resolve against `boundsPx` or `hitRegionPx` from `SLOT_RULES` after uniform SVG manifest projection.
- If a DOM target and pointer geometry disagree, pointer geometry wins.
- The selected chooser rule must expose its `slotId`, `slotRule`, `slotRuleLong`, `position`, and `eligibleGroups` in debug attributes.
- Third-place pool slots must open third-place pool menus, never adjacent winner/runner-up menus.
- This repair does not change the official slot-rule order or Game 2.
