# Pixelated country flag background layer

The Game 1 playfield now supports a country-flag background layer behind the bracket board.

The layer uses the country flag data already embedded in the page team list. The selected flag is rendered as a generated SVG data URL, scaled up across the board, and displayed with pixelated/crisp image rendering at low opacity.

The layer is intentionally decorative and non-authoritative: it must never interfere with hit testing, drag/tap targets, slot labels, or pick visibility.
