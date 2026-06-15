# Game 1 Modal Chooser Rule

## Purpose

The Game 1 playfield should stay simple.

The background image is the game board. Clicking a Round-of-32 cell opens a chooser window/frame.

## Rule

Do not build complex controls into the image.

Interaction should be:

```text
click slot
open chooser frame
choose team
flag appears in slot
```

## Runtime storage

Picks may be stored in browser localStorage during runtime.

The player can also export/import JSON.

## Delete rule

A selected slot must allow deletion/removal of its pick from the chooser window.
