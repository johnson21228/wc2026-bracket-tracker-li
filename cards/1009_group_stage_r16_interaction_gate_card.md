# Card 1009: Gate R16+ Pick Interaction During Group Stage

## Intent

Make the Group Stage bracket presentation honest: if R16+ cells are visually frame-only, they must not behave like active pick targets.

## Problem

Current runtime hides R16+ fills during Group Stage but still allows the pointer cursor and pick menu invocation for R16+ cells.

## Acceptance Criteria

- During Group Stage, R16+ cells remain visible as frame-only cells.
- During Group Stage, R16+ cells do not receive active pickable styling.
- During Group Stage, R16+ cells do not open pick menus.
- During Group Stage, controller-level slot handling rejects R16+ menu invocation as a fail-safe.
- R32 picking is unchanged.
- Knockout Stage restores R16+ rendering and interaction.
- Existing model data and saved picks are not deleted or blocked.
