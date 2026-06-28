#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "site/js/services/PickLockdownPolicy.js"
MODEL = ROOT / "site/js/mvc/model.js"
R32 = ROOT / "site/js/controllers/Game1R32PickController.js"
PROPS = ROOT / "site/data/current/site_properties.json"
VIEW = ROOT / "site/js/mvc/view.js"
BOARD_CSS = ROOT / "site/css/board.css"
INDEX = ROOT / "site/index.html"
errors = []

policy = POLICY.read_text()
model = MODEL.read_text()
r32 = R32.read_text()
props = json.loads(PROPS.read_text())

def require(condition, message):
    if not condition:
        errors.append(message)

def require_contains(text, token, label):
    require(token in text, f"{label} missing token {token}")

def require_absent(text, token, label):
    require(token not in text, f"{label} must not contain removed token {token}")

require("LockDown" in props, "site_properties.json must define top-level LockDown")
for key in [
    "LockDownTimeZone",
    "LockDownTime1",
    "LockDownTime1Name",
    "LockDownTime1SlotIds",
    "LockDownTime1TeamIds",
    "LockDownTime2",
    "LockDownTime2Name",
]:
    require(key not in props, f"site_properties.json must not contain {key}")

for token in [
    "LockDown: false",
    "function isManualLockDownEnabled",
    "function isGlobalLocked",
    "function tokensFromInput",
    "function getLockedPickReasonForTokens",
    "function getLockedPickReason",
    "function isPickChangeAllowed",
    "function assertPickChangeAllowed",
    "window.BracketeeringPickLockdownPolicy",
    "window.PickLockdownPolicy",
]:
    require_contains(policy, token, "PickLockdownPolicy.js")

for token in [
    "LockDownTimeZone",
    "LockDownTime1",
    "LockDownTime1Name",
    "LockDownTime1SlotIds",
    "LockDownTime1TeamIds",
    "LockDownTime2",
    "LockDownTime2Name",
    "parseTime",
    "nowMs",
    "Date.parse",
    "Date.now",
    "isLockdown1Active",
    "isLockdown1SlotToken",
]:
    require_absent(policy, token, "PickLockdownPolicy.js")

for token in [
    "markElement",
    "is-pick-locked",
    "data-pick-locked",
    "disabled = true",
    "pointerdown",
    "stopImmediatePropagation",
]:
    require_absent(policy, token, "PickLockdownPolicy.js")

require("function applyLockedState(root = document)" in policy, "PickLockdownPolicy.js must keep non-visual applyLockedState compatibility seam")
require("return root;" in policy, "PickLockdownPolicy.js applyLockedState must be non-visual no-op")
require('value === true || String(value).toLowerCase() === "true"' in policy, "LockDown flag must accept boolean true or string true")

require("function setPick(slotId, teamId)" in model, "model.js must expose setPick")
require("window.BracketeeringPickLockdownPolicy?.assertPickChangeAllowed?.({ slotId, teamId });" in model, "model.js setPick must enforce LockDown before write")
require("setPick({ fifaSlotId, teamId })" in r32, "Game1R32PickController.js must expose setPick")
require("window.BracketeeringPickLockdownPolicy?.assertPickChangeAllowed?.({ slotId: fifaSlotId, teamId });" in r32, "R32 controller setPick must enforce LockDown before write")
require("clearPick({ fifaSlotId })" in r32, "Game1R32PickController.js must expose clearPick")
require("window.BracketeeringPickLockdownPolicy?.assertPickChangeAllowed?.({ slotId: fifaSlotId });" in r32, "R32 controller clearPick must enforce LockDown before write")

view = VIEW.read_text()
board_css = BOARD_CSS.read_text()
index = INDEX.read_text()
for token in [
    "data-pick-interaction-suppressed",
]:
    require_absent(view, token, "site/js/mvc/view.js")
for token in [
    "data-pick-interaction-suppressed",
    "cursor: grab !important",
    "cursor: grabbing !important",
]:
    require_absent(board_css, token, "site/css/board.css")
require("lockdown-manual" not in index and "locked-slot-hit-test" not in index, "site/index.html must not contain lockdown cache-bust experiments")

if errors:
    print("WC2026 flag-only LockDown verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("OK: flag-only LockDown is a non-visual gameplay write policy with no time-lock or render/CSS behavior.")
