# Capture Back — Make opensite Target

## Prompt

Add a Makefile command that opens the WC2026 site with a local server for browser testing.

## Capture

The repo now has developer convenience targets:

- `make opensite`
- `make stopsite`

`make opensite` stops an existing local server on port `8000`, starts `python3 -m http.server 8000 -d site`, records a PID/log in `/tmp`, and opens `http://localhost:8000`.

`make stopsite` stops the saved PID or any process listening on port `8000`.

## Boundary

This is a repo-dev convenience patch only. It does not alter bracket model behavior, pick menu behavior, group standings data, or site runtime source rules.
