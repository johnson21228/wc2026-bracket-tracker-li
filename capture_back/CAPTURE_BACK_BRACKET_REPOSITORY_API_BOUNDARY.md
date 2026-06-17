# Capture Back — Bracket repository API boundary

## Decision

The browser UI should not directly bind itself to JSON files or localStorage.

Instead, the UI should speak to a repository boundary. The first implementation reads static JSON and saves user brackets to localStorage. A future implementation can call REST endpoints backed by SQLite.

## Current mode

- Static JSON model source
- Browser localStorage bracket store

## Future mode

- REST adapter
- Server-side SQLite persistence

## Boundary

The pick model does not change when persistence changes.
