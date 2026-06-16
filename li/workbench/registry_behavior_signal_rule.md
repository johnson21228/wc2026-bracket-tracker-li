# Registry Behavior Signal Rule

When a Workbench discovers a reusable process lesson, it should capture that lesson as a registry-visible signal so future registry review can update the Workbench product itself.

## Signal pattern

A registry signal should include:

- source Workbench name;
- observed failure or regression;
- accepted product lesson;
- suggested Workbench or Registry feature;
- affected verification pattern;
- follow-up repo or product work.

## Current signal

The WC2026 Bracket Tracker discovered that page replacement overlays can regress accepted behavior unless the Workbench stores those behaviors as durable contracts and checks them before and after mutation.

This should feed into the Workbench Registry and Workbench Product Builder as a product requirement:

> Registry should track accepted capabilities per repo and require CB overlays to preserve impacted behaviors or explicitly deprecate them.
