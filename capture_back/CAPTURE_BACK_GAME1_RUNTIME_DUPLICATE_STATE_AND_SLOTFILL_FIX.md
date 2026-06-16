# Capture Back — Game 1 Runtime Duplicate State and Slot Fill Fix

Game 1 hit testing failed because the reset page contained a stale duplicate top-level STORAGE_KEY/state/activeSlot block. This repair removes the stale block, requires exactly one STORAGE_KEY declaration, and normalizes the visible slot fill control to `slotFillOpacity`.
