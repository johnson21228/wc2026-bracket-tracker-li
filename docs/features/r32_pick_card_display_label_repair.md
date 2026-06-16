# R32 Pick Card Display Label Repair

This repair separates three related concepts that were being blurred:

- full team name
- compact pick-card label
- source/data code

For the Round of 32 pick card, the compact card face should use the three-letter label only. Tooltips/details should show the full team name and can explain the compact label as `Card label`, not as an ambiguous `Code` field.

Example:

- Card face: `🇨🇮 CIV`
- Tooltip title: `Ivory Coast`
- Tooltip detail: `Card label: CIV`

This avoids trying to fit long team names into small board-defined slot rectangles while still making the full team name available to the user.
