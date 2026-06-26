# Capture Back: Official R32 As Player Feeder Teams

## Problem

The game model has changed R32 ownership, but the bracket game itself has not changed.

The existing bracket already understands how picking works:

1. A slot resolves to a selected team.
2. A downstream winner slot gets its choices from its feeder slots.
3. A selected winner advances into the next downstream feeder path.

That bracket behavior must remain intact.

The only change is the source of selected teams for R32 slots.

Previously, normal players authored R32 occupants.

Now, Admin_/official authors R32 occupants. Normal players must see those R32 occupants as read-only official truth, and the existing bracket feeder system must treat those official occupants as the selected teams for R32.

## Rule

Official R32 occupants replace player-authored R32 picks as the source teams for the existing bracket propagation system.

The bracket’s existing feeder graph remains authoritative.

For any slot, choice generation must use the same feeder-slot mechanics already understood by the board.

The only ownership substitution is:

- old R32 selected-team source: player pick
- new R32 selected-team source: Admin_/official truth

Therefore:

- every R32 display slot resolves its selected team from Admin_/official truth;
- normal players cannot author, overwrite, or unlock R32 occupants;
- every R16 winner slot receives its choices from its two R32 feeder slots;
- when an R16 feeder slot is R32, that feeder’s selected team comes from Admin_/official truth;
- every later-round winner slot receives its choices from prior-round player winners, as before;
- player picking begins at R16;
- bracket advancement works as before;
- this change must not introduce a new bracket game or a parallel feeder system.

## Invariants

1. The board geometry, slot IDs, and feeder relationships remain the source for bracket flow.
2. Admin_/official owns R32 occupants.
3. Normal players see R32 occupants as read-only official truth.
4. R32 official occupants count as selected teams for the existing feeder-choice path.
5. R16 choices come from the official R32 feeder teams.
6. Later-round choices come from prior-round player winner picks, as before.
7. Normal player picks begin at R16.
8. Existing bracket winner propagation remains the behavior being preserved.
9. This is a source-ownership change for R32, not a new bracket game.
