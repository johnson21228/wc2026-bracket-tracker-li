# Capture Back — Game 2 Shared Bracket Plane Geometry

## Change
Game 2 now uses a single shared `bracketPlane` coordinate system for the middle-layer PNG, slot guides, and bracket items.

## Why
The logical geometry was not agreeing with the image because the layers were using different coordinate frames.

## Preserved
- Game 1 untouched.
- Shared middle-layer PNG remains the current visible geometry source.
- Future truth-geometry transition remains open.

## Verification
Run `make verify` and open `site/game2/index.html`. Toggle slot guides to inspect captured slot alignment.
