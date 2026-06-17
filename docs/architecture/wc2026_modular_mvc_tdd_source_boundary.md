# WC2026 Modular MVC/TDD Source Boundary

## Decision

The inventory review found that the Workbench process is strong but the application implementation has accumulated too much behavior inside large HTML surfaces.

The desired direction is now modular MVC/TDD source. The older old portability property is removed as an architectural goal.

## Why

The repeated bugs around menus, slot identity, storage, rendering, transparency, hit testing, and knockout candidate resolution all point to the same cause: too many responsibilities were patched into one page.

A page-concentrated artifact makes early demos easy, but it makes durable behavior harder to reason about once the app includes:

- two games
- slot-specific eligibility
- third-place rules
- advancement paths
- persisted picks
- geometry authority
- public review surfaces
- future scoring

## Boundary

Use this separation:

```text
site/
  index.html                  entry point / review shell
  assets/
  data/
  js/
    models/
    controllers/
    views/
    tests/
```

The exact folder names may evolve, but the boundary should not: rules and state do not belong directly in the HTML entry point.

## Model examples

- team registry
- group registry
- R32 slot rules
- third-place pools
- bracket geometry
- pick store
- Game 1 state
- Game 2 state
- scoring inputs

## Controller examples

- open candidate menu
- close active menu
- apply pick
- clear invalid downstream picks
- resolve feeder contestants
- rerender affected board cells

## View examples

- board layer rendering
- menu rendering
- flag and abbreviation display
- pick-card display
- empty slot display
- tooltip and review affordances

## TDD expectation

Every behavioral repair should preserve the mistake as a durable regression test when practical.

The first durable test suite should cover:

```text
R32 eligibility
third-place eligibility
knockout feeder resolution
pick persistence
state separation
geometry coverage
menu lifecycle
```

## What not to do

Do not add new LI or prompts that say the app should remain a page-concentrated implementation.

Do not solve new behavior by appending another isolated patch into the page unless it is explicitly temporary and followed by a Capture Back card to extract it.
