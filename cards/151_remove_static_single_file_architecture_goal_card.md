# Card 151 — Remove Static Single-File Architecture Goal

## Intent

Align the WC2026 Bracket Tracker with the inventory review: modular MVC/TDD source is the desired design direction.

## Problem

Earlier LI described a page-concentrated implementation as a portability property. That helped early demos, but it now conflicts with the best-practice architecture needed for reliable Game 1 and Game 2 behavior.

## Decision

Remove the monolithic HTML property as an LI goal.

Keep static hosting as a possible deployment property, but do not treat one HTML file as the desired source architecture.

## Acceptance criteria

- No current LI tells the repo to strive for a page-concentrated implementation.
- A modular MVC/TDD source rule exists.
- The old static release rule is rewritten as static-hostable, not monolithic.
- The main verifier runs the modular source boundary verifier.
- Existing historical Capture Back records may remain historical evidence.

## Evidence

- `li/world_cup/modular_mvc_tdd_source_rule.md`
- `li/world_cup/static_html_release_rule.md`
- `docs/architecture/wc2026_modular_mvc_tdd_source_boundary.md`
- `tools/verify_wc2026_modular_source_boundary.py`
- `capture_back/CAPTURE_BACK_REMOVE_STATIC_SINGLE_FILE_ARCHITECTURE_GOAL.md`
