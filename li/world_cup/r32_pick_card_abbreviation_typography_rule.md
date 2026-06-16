# R32 Pick Card Team Abbreviation Typography Rule

A filled R32 pick card is a slot-bound visual object. Its compact face must use the team flag plus the three-letter team abbreviation.

## Authority

The board slot rectangle remains the layout authority. The card must not grow beyond the slot to satisfy typography.

## Compact face

The compact R32 pick card face must render:

- flag
- team abbreviation, exactly three uppercase letters

It must not render the full team name on the card face.

## Typography

All R32 pick cards must use the same typography for the team abbreviation:

- same font family stack
- same font size
- same font weight
- same line height
- same letter spacing

The abbreviation is fixed-length, so per-team font fitting is no longer needed. Runtime code must not shrink or grow the abbreviation per team.

## Slot fit

The flag should be as large as the slot height allows without being clipped. The abbreviation should remain vertically centered and unclipped. Padding, gap, border, shadow, and radius must be chosen so the card fits inside the pixel-defined slot.

## Details surface

The tooltip/details surface may show the full team name and the team abbreviation. It must not use the word `Code` for the team abbreviation.
