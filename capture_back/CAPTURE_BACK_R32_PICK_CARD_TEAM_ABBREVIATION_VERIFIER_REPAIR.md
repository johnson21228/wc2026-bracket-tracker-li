# Capture Back — R32 Pick Card Team Abbreviation Verifier Repair

## Captured issue

The team-abbreviation authority overlay applied, but the verifier failed because it attempted to parse the full HTML file with Node:

```text
node --check site/game1/index.html
ERR_UNKNOWN_FILE_EXTENSION: Unknown file extension ".html"
```

## Repair

The verifier now extracts inline JavaScript from `site/game1/index.html` and checks the extracted script as a temporary `.js` file.

## Preservation

This repair does not alter the Game 1 runtime. It only repairs verification.
