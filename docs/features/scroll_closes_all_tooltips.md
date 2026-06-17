# Scroll Closes All Tooltips

Game 1 now treats scrolling as a tooltip-dismiss gesture.

Tooltips explain a target at the current viewport position. Once the board scrolls, the tooltip may no longer sit near its target or may compete with other surfaces.

The scroll-close behavior only affects tooltip surfaces. It does not clear selected picks, active menu state, or bracket storage.
