#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

props_path = ROOT / "site/data/current/site_properties.json"
service_path = ROOT / "site/js/services/PickLockdownPolicy.js"
index_path = ROOT / "site/index.html"
css_path = ROOT / "site/css/app.css"
makefile_path = ROOT / "Makefile"

required_files = [
    props_path,
    service_path,
    ROOT / "li/world_cup/player_pick_lockdown_times_rule.md",
    ROOT / "docs/features/player_pick_lockdown_times.md",
    ROOT / "captures/CAPTURE_BACK_PLAYER_PICK_LOCKDOWN_TIMES.md",
    ROOT / "cards/300_player_pick_lockdown_times_card.md",
]

for path in required_files:
    require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

if props_path.exists():
    props = json.loads(props_path.read_text())
    require(props.get("LockDownTimeZone") == "America/New_York", "LockDownTimeZone must be America/New_York")
    require("LockDownTime1" in props, "site properties must include LockDownTime1")
    require("LockDownTime2" in props, "site properties must include LockDownTime2")
    require("R-R32-01" in props.get("LockDownTime1SlotIds", []), "LockDownTime1 must target R-R32-01")
    require(set(props.get("LockDownTime1TeamIds", [])) == {"CAN", "RSA"}, "LockDownTime1TeamIds must be CAN/RSA")

    try:
        t1 = datetime.fromisoformat(props["LockDownTime1"])
        t2 = datetime.fromisoformat(props["LockDownTime2"])
        require(t1 < t2, "LockDownTime1 must be before LockDownTime2")
    except Exception as exc:
        errors.append(f"LockDownTime values must be ISO datetimes with offsets: {exc}")

if service_path.exists():
    service = service_path.read_text()
    for token in [
        "BracketeeringPickLockdownPolicy",
        "LockDownTime1",
        "LockDownTime2",
        "isGlobalLocked",
        "isLockdown1SlotToken",
        "bracketeering:pick-lockdown-blocked",
        "data/current/site_properties.json",
    ]:
        require(token in service, f"PickLockdownPolicy.js missing token {token}")

if index_path.exists():
    index_text = index_path.read_text()
    require("js/services/PickLockdownPolicy.js" in index_text, "site/index.html must load PickLockdownPolicy.js")
    require("\\\\n</body>" not in index_text, "site/index.html must not contain a literal \\\\n before </body>")
    require(
        index_text.find("js/services/PickLockdownPolicy.js") < index_text.find("js/app.js"),
        "PickLockdownPolicy.js should load before js/app.js so lockdown is available before app wiring",
    )

if css_path.exists():
    css = css_path.read_text()
    require("is-pick-locked" in css, "CSS must define locked pick visual state")
    require("data-pick-locked" in css, "CSS must define data-pick-locked visual state")

if makefile_path.exists():
    require(
        "python3 tools/verify_wc2026_player_pick_lockdown_times.py" in makefile_path.read_text(),
        "Makefile verify target must run player pick lockdown verifier",
    )

if errors:
    print("WC2026 player pick lockdown verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: Player pick lockdown times are configured, captured, loaded, and verified.")
