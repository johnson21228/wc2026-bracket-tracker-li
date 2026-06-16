# Game 1 Visible Slot Hit Targets Rule

Hit testing for Game 1 must be implemented in the HTML/JS interaction layer, not by relying on opaque pixels in the middle-layer PNG.

The middle-layer bracket image may provide visual geometry only. Slot visibility, pick state, and click/tap behavior belong to the runtime DOM hit target layer. Decorative layers must use `pointer-events: none`; hit targets must remain above them with `pointer-events: auto`.
