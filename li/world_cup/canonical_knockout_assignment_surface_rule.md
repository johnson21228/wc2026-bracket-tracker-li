# Canonical Knockout Assignment Surface Rule

A knockout choice menu is not merely a floating chooser. It is the assignment surface for the bracket cell that opened it.

Only one canonical runtime path may own knockout menu assignment. Competing wrappers that separately intercept assignment, storage, and rendering must be removed or made subordinate to the canonical path.

The canonical path must write to round-specific storage and render the selected team in the opening bracket cell.
