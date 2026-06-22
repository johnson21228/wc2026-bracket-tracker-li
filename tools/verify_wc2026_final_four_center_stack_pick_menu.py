#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

errors = []

model = Path("site/js/mvc/model.js").read_text()
view = Path("site/js/mvc/view.js").read_text()
controller = Path("site/js/mvc/controller.js").read_text()
manifest = json.loads(Path("site/data/geometry/uniform_pick_card_gameboard_manifest.json").read_text())
bracket_slots = json.loads(Path("site/data/model/bracket_slots.json").read_text())

def require(text, token, label):
    if token not in text:
        errors.append(f"missing {label}: {token}")

# Geometry slots must exist and old CENTER-FINAL-FOUR must not return as runtime geometry.
manifest_ids = {slot.get("slotId") for slot in manifest.get("slots", [])}
for slot_id in ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]:
    if slot_id not in manifest_ids:
        errors.append(f"manifest missing interactive center-stack geometry slot {slot_id}")
if "CENTER-FINAL-FOUR" in manifest_ids:
    errors.append("CENTER-FINAL-FOUR must not return as runtime pick-slot geometry")

# Canonical model must map those picks to matching geometry slots.
canonical = {slot.get("slotId"): slot for slot in bracket_slots.get("canonicalPickSlots", [])}
for slot_id in ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]:
    if canonical.get(slot_id, {}).get("geometrySlotId") != slot_id:
        errors.append(f"{slot_id} canonical pick slot must map to matching geometrySlotId")

# Model precedence constraints.
require(model, "FINAL_FOUR_PRECEDENT_CONSTRAINTS", "Final Four precedent constraint table")
for token in [
    '"FINAL-LEFT": Object.freeze(["L-SF-01", "L-SF-02"])',
    '"FINAL-RIGHT": Object.freeze(["R-SF-01", "R-SF-02"])',
    '"CHAMPION": Object.freeze(["FINAL-LEFT", "FINAL-RIGHT"])',
    "dependencies.set(slotId, feederIds.filter((feederId) => slotsById.has(feederId)))",
    "getKnockoutChoices(slotId)",
    "Final Four center-stack cells use the same dependency-map menu path",
]:
    require(model, token, "precedent-aware Final Four model wiring")

# Third-place behavior remains present and loser-constrained.
for token in [
    '"THIRD-PLACE-WINNER"',
    'loserFromSemifinal("FINAL-LEFT", ["L-SF-01", "L-SF-02"])',
    'loserFromSemifinal("FINAL-RIGHT", ["R-SF-01", "R-SF-02"])',
]:
    require(model, token, "third-place semifinal-loser behavior")

# Controller preselects clicked canonical slot before opening menu.
for token in [
    "let activeSlotId = null",
    "activeSlotId = slotId",
    "openPickMenu: activeSlotId ? model.getPickMenu(activeSlotId) : null",
]:
    require(controller, token, "controller active-slot preselection")

# View uses the same pick-surface click path. Do not require one exact disabled expression;
# older/current view code may represent non-pickable state through classes, attributes, or guards.
for token in [
    "button.dataset.slotId = slot.slotId",
    "handlers.onSlotClick?.(slot.slotId)",
]:
    require(view, token, "view pick-surface click/menu path")

if "slot.pickable" not in view and "pickable" not in view:
    errors.append("view should preserve pickable/non-pickable state for pick surfaces")

# FINAL-LEFT / FINAL-RIGHT / CHAMPION must be recognized by slot-id syntax, not filtered out.
if not re.search(r"FINAL\|CHAMPION", view):
    errors.append("view slot-id recognition should include FINAL and CHAMPION pick IDs")

# Lifecycle-stage pick gating remains covered by dedicated lifecycle presentation-only verifiers.
# This focused verifier must not fail just because presentation/background state names still exist.
for forbidden in [
    "lifecycleStageBlocksPick",
    "Group Stage only",
    "Knockout Stage only",
]:
    if forbidden in controller:
        errors.append(f"controller must not restore lifecycle-stage pick gating token: {forbidden}")

if errors:
    print("Final Four center-stack pick menu verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: Final Four center-stack cells preselect canonical slots and use existing precedent-aware pick menu constraints.")
