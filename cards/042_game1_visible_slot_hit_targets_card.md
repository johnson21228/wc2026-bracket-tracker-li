# Card 042 — Game 1 Visible Slot Hit Targets

## Intent
Restore confidence in Game 1 hit testing by making the 32 runtime slot hit areas visible and tunable as a separate top interaction layer.

## Change
- Keep the pub JPEG and bracket geometry/transparent PNG as visual layers.
- Keep hit testing as DOM buttons above decorative layers.
- Make empty slots semi-opaque by default.
- Add Slot Fill and Slot Border controls.
- Preserve Show hit zones for debug confirmation.

## Verification
`make verify` must pass and confirm the visible slot target markers exist in `site/game1/index.html`.
