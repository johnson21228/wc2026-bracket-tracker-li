# Card 170 — Promote gameboard visual defaults

## Intent

Promote the copied developer-tuned gameboard presentation values into durable site defaults.

## Copied developer properties

```json
{
  "gameboardOpacity": "0.52",
  "gameboardLineColor": "rgba(255, 255, 255, 0.98)",
  "gameboardLineWidth": "1.5",
  "gameboardLineGlow": "0.05"
}
```

## Acceptance

- `BoardShell.js` initializes the gameboard outline with these defaults.
- `DeveloperFrame.js` fallback values match these defaults.
- Source SVG and geometry manifest remain unchanged.
- `make verify` and `make pack` pass.
