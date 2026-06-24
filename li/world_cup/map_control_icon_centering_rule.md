# Map Control Icon Centering Rule

Player-facing map control marks must be geometric icons owned by the View/CSS layer. Do not rely on font glyph metrics for the `+`, `−`, or info mark inside the circular controls.

The control buttons must keep accessible labels and existing runtime data hooks. The icon spans are decorative and must be `aria-hidden`.

This rule is visual polish only; it must not change board zoom behavior, info-panel behavior, or gameplay state.
