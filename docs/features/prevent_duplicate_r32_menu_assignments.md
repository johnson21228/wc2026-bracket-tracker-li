# Prevent Duplicate R32 Menu Assignments

The R32 assignment surface treats each team as a unique entrant. A team already assigned to one R32 slot should not appear as an available choice for another R32 slot.

The exception is the slot currently being edited: its existing team remains available so the user can reopen the menu and keep the current value.

This feature applies to ordinary R32 menus and third-place candidate menus. It is implemented in two layers:

1. Menu display filtering hides duplicate choices.
2. Defensive selection blocking prevents a duplicate from being saved if it is triggered by stale DOM or touch-event timing.

This remains a frontend-local rule for the static Pages version. A future server-backed pool mode should enforce the same rule before saving `r32_assignments_json`.
