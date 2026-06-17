# Canonical Knockout Assignment Render Repair

The knockout choice menu is an assignment surface, not a detached chooser.

When a user taps a bracket cell such as `L-R16-01`, the menu must remember that cell as the target. When the user selects a team, the team is stored for that exact slot and rendered in that exact slot.

This repair adds a final render guarantee to the anchored menu assignment path. After writing to storage, it calls the normal render flow and then verifies that a pick card exists for the target cell. If the rendered cell is missing, it renders the target cell directly with the existing round-specific render function.
