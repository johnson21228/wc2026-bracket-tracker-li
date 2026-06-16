# Game 2 Scrollable Pixel-Native Board Review Rule

Game 2 may enter a board-only source-review mode where the shared game board image is rendered at its native pixel size.

For this mode:

- the board plane is 1536 × 1024 CSS pixels;
- the board image is not fit-to-window, squeezed, stretched, or independently scaled;
- the page is allowed to scroll horizontally and vertically;
- the board image remains the only visible gameplay surface;
- no seeded teams, controls, ledgers, or advancement nodes should obscure the board.

This mode exists to review the source game board before logical items are mapped to pixel-defined regions.
