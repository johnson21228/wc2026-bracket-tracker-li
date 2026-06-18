# WC2026 user bracket storage model

The storage model separates stable game data from presentation and persistence.

## Core records

- Team
- User
- BracketSlot
- UserBracket
- PickValue
- FifaR32SlotMap

## Storage adapter

The browser implementation uses localStorage first.

A later SQLite implementation should live behind an API server while preserving the same model shape.
