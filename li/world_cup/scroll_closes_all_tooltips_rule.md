# Scroll Closes All Tooltips Rule

When the Game 1 board scrolls, all tooltip surfaces must close.

This includes:

- scroll events
- wheel movement
- touch movement used for scrolling

The close action must not clear bracket picks or change the active menu selection target.

A tooltip is contextual to its anchor. Scrolling invalidates that visual context.
