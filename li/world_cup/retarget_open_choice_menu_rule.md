# Retarget Open Choice Menu Rule

A pickable slot tap while a choice menu is open must be interpreted as a request to retarget the active menu to the newly tapped slot.

The implementation must preserve:
- board-attached positioning,
- picked-item anchoring,
- duplicate filtering for the new target,
- selection save/close behavior,
- outside non-pickable close behavior.
