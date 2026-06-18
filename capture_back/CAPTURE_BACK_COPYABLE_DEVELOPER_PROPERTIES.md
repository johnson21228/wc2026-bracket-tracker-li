# Capture Back — Copyable developer properties

## Problem

Developer tuning values were visible through sliders/selects but not easy to capture as durable defaults.

## Change

Added a copyable developer properties panel that reports:

- board dataset values
- board native size
- gameboard opacity
- gameboard line color
- gameboard line width
- gameboard glow
- SVG state
- truth resource paths

## Workflow

Tune visually, click `Copy properties`, paste JSON into the workbench chat, then promote the chosen values into source defaults.
