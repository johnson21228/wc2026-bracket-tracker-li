# Card 136: Repair Pages Review Pick Acceptance

## Claim

The public GitHub Pages review build must accept visible pick selections and persist them locally for review.

## Problem

The site can be served successfully from GitHub Pages while a reviewer cannot complete bracket picks. A review link is not useful unless tap/click selection writes the chosen team to the bracket store and re-renders the picked cell.

## Decision

Add a runtime review acceptance guard that mirrors accepted choices into the unified bracket pick store and legacy stores, then re-renders the board. Finality validation may adorn invalid picks, but must not prevent the review act of making a pick.

## Acceptance Criteria

- The GitHub Pages site loads.
- Tapping a team in a choice menu stores the pick.
- The picked cell visibly updates without requiring reload.
- Reload preserves the pick through localStorage.
- R32 aliases are mirrored so logical and manifest slot ids resolve.
