# Game 1 knockout choice menu runtime wiring rule

Game 1 winner-pick slots must not use the R32 group-eligibility menu.

When a tapped slot is in R16, QF, or SF, the runtime must resolve exactly two feeding contestants and render those contestants as the choice menu. The runtime must support both manifest-native slot IDs, such as `L-R32-01`, and normalized logical IDs, such as `R32-1`.

The empty-set/waiting state is valid only when one or both feeding contestants are absent. It is not valid when the underlying contestant resolver can find both contestants.
