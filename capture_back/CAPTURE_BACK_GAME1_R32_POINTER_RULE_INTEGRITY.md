# Capture Back — Game 1 R32 Pointer Rule Integrity

This CB repairs a chooser mismatch after Game 1 adopted the uniform SVG gameboard layer.

The chooser now resolves the clicked/tapped R32 rule from manifest-derived board coordinates. If the DOM event target and the pointer-resolved slot differ, the pointer-resolved manifest slot wins.

This protects best-third-place pool slots from opening adjacent winner/runner-up menus.
