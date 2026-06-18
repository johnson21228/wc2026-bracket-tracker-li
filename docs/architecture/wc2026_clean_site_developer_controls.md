# WC2026 clean site developer controls

The clean site includes a developer controls panel below the board surface.

## Purpose

The controls panel provides visibility while rebuilding from first principles. It answers whether the current modules have rendered and which truth resources are wired.

## Initial controls

| Control | Status |
| --- | --- |
| Show background | Active |
| Show SVG gameboard | Pending/disabled |
| Show pick IDs | Pending/disabled |

## Module

`site/new/js/dev/DeveloperControlsPanel.js`

This module does not render the board. It observes and controls layer visibility through explicit data attributes.

## Boundary

Developer controls are not product UI. They are diagnostic tooling for the clean rebuild.
