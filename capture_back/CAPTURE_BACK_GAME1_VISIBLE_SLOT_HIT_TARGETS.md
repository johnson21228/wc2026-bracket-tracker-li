# Capture Back — Game 1 Visible Slot Hit Targets

Game 1 should not rely on pixels in the bracket PNG for interaction. The bracket PNG remains visual evidence only. The 32 pickable slots are represented by DOM hit targets layered above the pub background and bracket geometry.

This capture adds visible, nearly opaque slot surfaces so the player can see where to click/tap, while retaining a debug Show hit zones mode.
