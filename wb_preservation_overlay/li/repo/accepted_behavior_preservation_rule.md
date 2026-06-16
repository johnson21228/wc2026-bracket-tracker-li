# Accepted Behavior Preservation Rule

A Capture Back that modifies a file associated with an accepted behavior must preserve that behavior unless the user explicitly approves deprecation or replacement.

## Rule

When a behavior has been accepted as working, it becomes part of the repository's living contract. Future overlays that touch related files must do one of the following:

1. Preserve the behavior and provide evidence.
2. Explicitly deprecate the behavior with user approval.
3. Fail verification or stop before mutation.

## Required CB evidence

Any CB touching a behavior-bearing file should include:

- accepted behaviors impacted by the change;
- behaviors preserved;
- behaviors intentionally changed;
- behaviors not touched;
- verification evidence for the preserved behaviors.

## WC2026 examples

Accepted behaviors include:

- Game 1 has a layered board: pub/background image, transparent bracket geometry, DOM hit targets.
- Game 1 has 32 clickable Round-of-32 hotspot buttons.
- Game 1 tap menu only offers teams eligible for the selected slot rule.
- Decorative visual layers do not intercept pointer events.
- Game 2 uses fixed/official Round-of-32 seed truth, while Game 1 picks become comparison/tiebreaker metadata.

## Product lesson

This repository records that Workbench verification should evolve beyond file/token checks toward behavior-preservation checks and registry-level impact analysis.
