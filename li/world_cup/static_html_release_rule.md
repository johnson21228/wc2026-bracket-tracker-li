# Static HTML Release Rule

## Purpose

The tracker should remain usable as a single static HTML file.

The same static file can be:

- downloaded and opened locally
- emailed or texted
- hosted on GitHub Pages
- hosted on a simple server
- passed back into an II reasoner

## Release rule

Each meaningful update should create a new immutable release under `releases/`.

Example:

```text
releases/world_cup_bracket_tracker_v001.html
releases/world_cup_bracket_tracker_v002.html
```

For GitHub Pages, copy the current public release to:

```text
index.html
```
