# WC2026 async BoardShell startup

The gameboard outline layer fetches and parses SVG, so board construction is async.

The app entrypoint must await `createBoardShell` before calling `querySelector` on the returned board shell.
