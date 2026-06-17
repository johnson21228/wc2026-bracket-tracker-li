# Game 1 knockout choice menu runtime wiring

Game 1 now has a runtime boundary between R32 assignment choices and knockout winner choices.

R32 choice menus are governed by slot eligibility groups. Knockout choice menus are governed by the contestants already present in the bracket path feeding the tapped slot.

- R16 choice = two teams assigned to the feeding R32 slots.
- QF choice = two winners picked in the feeding R16 slots.
- SF choice = two winners picked in the feeding QF slots.

This repair exists because the resolver tests can prove contestants exist while the UI can still show an empty-set state if a tap falls through to the older R32 choice path or uses mismatched slot IDs.
