# Async board shell startup rule

If the board shell creates any async layer, the app entrypoint must await board creation before querying or mounting it.

Required pattern:

- `async function startApp()`
- `const boardShell = await createBoardShell(...)`

Startup errors must render visibly rather than leaving the site as a black page.
