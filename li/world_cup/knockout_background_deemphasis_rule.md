# Knockout background deemphasis rule

The knockout pub background may be visually deemphasized only through presentation-layer CSS.

Do not lower opacity by editing or replacing `site/assets/board/knockout_pub_background.jpeg`.
Do not change gameplay, pick storage, official truth, or bracket geometry to tune background emphasis.

Required runtime invariant:
- `site/assets/board/knockout_pub_background.jpeg` remains the active board background.
- `.board-background-layer` owns the visual opacity.
