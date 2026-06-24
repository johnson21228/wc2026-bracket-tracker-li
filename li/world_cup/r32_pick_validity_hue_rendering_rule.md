# LI Rule: R32 Pick Validity Hue Rendering

Picked R32 cells must render validity as a filled-cell hue.

Required behavior:
- valid picked R32 cells render with a green hue
- invalid picked R32 cells render with a red hue
- invalid rendering wins if a cell is ever marked both valid and invalid
- validity hue is a filled rendering property
- Group Stage frame-only suppressed cells must not show red/green validity fill
- this rule must not affect pick validity computation or saved picks
- this rule must not restore R16+ fill during Group Stage

- The validity hue must color the filled cell background, not only the outline.
