# Card 187 — Add Make opensite target

## Intent

Add a small developer convenience target that opens the WC2026 bracket tracker site through a local HTTP server instead of `file://`.

## Reason

The site uses JavaScript modules and checked-in JSON model data. Browser testing should happen through a local server so module imports and data fetches behave like the deployed site.

## Scope

- Add `make opensite` to stop any existing local server on port 8000, start `python3 -m http.server 8000 -d site`, and open `http://localhost:8000`.
- Add `make stopsite` to stop the server later.
- Write the PID and log to `/tmp` so the target is easy to reason about.
- Add a verifier so this repo-dev affordance stays available.

## Acceptance

- `make opensite` exists.
- `make stopsite` exists.
- The site is served from `site/` on port 8000.
- The target opens `http://localhost:8000`.
- Verify includes the opensite target verifier.
