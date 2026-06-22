#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
view = (ROOT / "site/js/mvc/view.js").read_text()
css = (ROOT / "site/css/board.css").read_text()
makefile = (ROOT / "Makefile").read_text()

errors = []

helper = re.search(
    r'function playerFacingEmptyPickText\(slot\) \{(?P<body>[\s\S]*?)\n  \}',
    view,
)
helper_body = helper.group("body") if helper else ""
if not helper:
    errors.append("missing playerFacingEmptyPickText helper")
if 'return "Choose Team";' not in helper_body:
    errors.append('playerFacingEmptyPickText must return exactly "Choose Team"')

for forbidden in [
    "slot.slotId",
    "slot.label",
    "slot.fifaLabel",
    "CHAMPION",
    "THIRD-PLACE-WINNER",
    "R16",
    "QF",
    "SF",
    "FINAL",
]:
    if forbidden in helper_body:
        errors.append(f"empty-cell helper still uses internal fallback token: {forbidden}")

if 'function unpickedSlotDisplayText(slot) {' not in view:
    errors.append("missing unpickedSlotDisplayText helper")
if 'return playerFacingEmptyPickText(slot);' not in view:
    errors.append("unpickedSlotDisplayText must delegate to playerFacingEmptyPickText(slot)")
if 'unpickedLabel.className = "unpicked-cell-label";' not in view:
    errors.append("unpicked render path must use unpicked-cell-label")
if 'unpickedLabel.textContent = unpickedSlotDisplayText(slot);' not in view:
    errors.append("unpicked render path must use unpickedSlotDisplayText(slot)")

for token in [
    "picked-cell-identity",
    "picked-cell-flag",
    "picked-cell-code",
    "displayTeam.flag",
    "flag.style.fontSize",
    "displayTeam.abbr || displayTeam.id",
    "identity.append(flag, code)",
    "value.append(identity)",
]:
    if token not in view:
        errors.append(f"picked-cell rendering token missing: {token}")

css_compact = re.sub(r"\s+", " ", css)
for token in [
    ".pick-slot-button.is-unpicked .unpicked-cell-label",
    "display: flex",
    "align-items: center",
    "justify-content: center",
    "text-align: center",
]:
    if token not in css_compact:
        errors.append(f"centered unpicked-cell CSS missing: {token}")

if "python3 tools/verify_wc2026_picked_bracket_cell_identity_rendering.py" not in makefile:
    errors.append("picked-cell identity verifier is no longer wired into make verify")

if errors:
    print("WC2026 unpicked bracket-cell Choose Team verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print('OK: unpicked bracket cells render centered "Choose Team" without internal IDs.')
