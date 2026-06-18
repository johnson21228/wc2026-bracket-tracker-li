# Card 204: Publish group-stage pub background as runtime background

## Intent

Use the group-stage pub image as the visible board background for the current site surface.

## Change

- Point the page preload to `assets/board/pub_background.jpeg`.
- Point the MVC board background layer to `assets/board/pub_background.jpeg`.
- Preserve the knockout pub background asset for later knockout-mode work.
- Add LI, feature docs, capture back evidence, and a verifier.

## Acceptance

- Runtime preload and rendered board background agree.
- The active runtime background is the group-stage pub background.
- The knockout background remains present but is not the default runtime image.
- `make verify` runs the new verifier.
