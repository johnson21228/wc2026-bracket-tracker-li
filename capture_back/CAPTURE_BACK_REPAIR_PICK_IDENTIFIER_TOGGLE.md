# Capture Back — Repair pick identifier developer toggle

## Problem

The board can render pick identifiers, but the developer panel lacks a show/hide toggle.

## Repair

Added `Show pick identifiers` to `DeveloperFrame.js`.

## Boundary

This changes only developer controls. It does not change geometry, pick state, or the pick identifier layer.
