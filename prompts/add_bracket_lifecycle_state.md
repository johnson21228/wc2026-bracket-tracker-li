# Prompt — Add bracket lifecycle state

Add explicit Game 1/Game 2 bracket lifecycle state to the WC2026 bracket tracker.

Requirements:

- Define canonical phases: `game1_r32_assignment`, `game1_knockout_prediction`, `game1_locked_for_scoring`, `game2_official_r32`, and `game2_knockout_live`.
- Preserve Game 1 R32 assignment picks separately from Game 1 `knockoutPicks`.
- Preserve Game 2 official-bracket `knockoutPicks` separately from Game 1 evidence.
- Expose a small runtime API that can answer what pick mode a slot should use.
- Do not replace the R32 menu in this patch.
- Do not overwrite Game 1 evidence when official Game 2 truth is loaded.
