# Gameboard Group Button Rail Rule

The gameboard must provide a persistent group-button rail across the bottom of the board.

The rail must include one group tile button for each World Cup group, ordered Group A through Group L.

Each group tile must show the group label at the top and the four team flags for that group below the label in a 2×2 square flag grid. The 2×2 flag grid is required so the tile reads as a whole-group evidence entry point, not as four separate team-pick actions.

The entire group tile is one button. Individual flags inside the tile are decorative group evidence and must not select teams, clear picks, or mutate bracket advancement state.

Activating a group tile opens the shared group panel for that group. The group panel opened from the rail must use the same model/controller/view path as the group panel opened from a pick-menu group label.

The group rail must be spread evenly along the bottom of the gameboard and centered as a full set. If all twelve group tiles cannot fit comfortably in one row in a future responsive layout, the rail may wrap into multiple centered rows while preserving Group A through Group L order.

Each group tile button must have an accessible label such as “Open Group C panel: Brazil, Morocco, Haiti, Scotland.”

The model owns the group rail data. The view renders the centered bottom rail and the 2×2 flag grid. The controller opens the shared group panel. The runtime must use local checked-in group data only and must not scrape ESPN or any external site at runtime.
