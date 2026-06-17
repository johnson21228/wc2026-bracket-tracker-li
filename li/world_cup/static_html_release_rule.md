# Static-Hostable Site Release Rule

## Purpose

This rule replaces the older monolithic HTML release posture.

The WC2026 Bracket Tracker should remain easy to review and deploy as a static-hostable site, but the Workbench should not strive for a page-concentrated implementation or monolithic page implementation.

## Current direction

The source should be modular and governed by the MVC/TDD boundary:

- data files remain data files
- model logic remains testable outside the DOM
- view logic renders from model/controller outputs
- controller logic coordinates user intent and state transitions
- HTML files remain entry points, not the system of record

## Release rule

Each meaningful update may create an immutable release snapshot under `releases/`, but release snapshots are evidence of a working version, not the preferred authoring surface.

The canonical implementation should live under `site/` and related source/data/test folders.

## Deployment rule

GitHub Pages compatibility is still acceptable when it does not conflict with modular structure.

A deployable static site can include multiple HTML, JavaScript, CSS, JSON, image, and data assets.
