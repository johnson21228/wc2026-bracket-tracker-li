#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import json

repo_root = Path(__file__).resolve().parents[1]
props_path = repo_root / "site/data/current/site_properties.json"
service_path = repo_root / "site/js/services/PickLockdownPolicy.js"
model_path = repo_root / "site/js/mvc/model.js"
r32_controller_path = repo_root / "site/js/controllers/Game1R32PickController.js"

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require(props_path.exists(), "site/data/current/site_properties.json must exist")
require(service_path.exists(), "site/js/services/PickLockdownPolicy.js must exist")

props = {}
if props_path.exists():
    props = json.loads(props_path.read_text())

    require(props.get("LockDownTimeZone") == "America/New_York", "LockDownTimeZone must be America/New_York")
    require("LockDown" + "Time1" not in props, "first-lock time must be removed")
    require("LockDown" + "Time1Name" not in props, "first-lock name must be removed")
    require("LockDown" + "Time1SlotIds" not in props, "first-lock slot list must be removed")
    require("LockDown" in props, "site properties must include LockDown manual override")
    require(isinstance(props.get("LockDown"), bool), "LockDown must be a boolean")
    require("LockDownTime2" in props, "site properties must include LockDownTime2")
    require(
        props.get("PickLockdownPolicy", {}).get("lockdown2Scope") == "all-player-owned-picks",
        "PickLockdownPolicy.lockdown2Scope must state all-player-owned-picks",
    )
    require(
        "lockdown1Scope" not in props.get("PickLockdownPolicy", {}),
        "PickLockdownPolicy.lockdown1Scope must be removed",
    )

    try:
        t2 = datetime.fromisoformat(props["LockDownTime2"])
        require(t2.tzinfo is not None, "LockDownTime2 must include timezone offset")
    except Exception as exc:
        require(False, f"LockDownTime2 must be a valid ISO datetime with offset: {exc}")

service_text = service_path.read_text() if service_path.exists() else ""

for token in [
    "LockDown",
    "LockDownTime2",
    "isGlobalLocked",
    "tokensFromInput",
    "isPickChangeAllowed",
    "assertPickChangeAllowed",
    "bracketeering:pick-lockdown-blocked",
    "data/current/site_properties.json",
]:
    require(token in service_text, f"PickLockdownPolicy.js missing token {token}")

for removed_token in [
    "LockDown" + "Time1",
    "LockDown" + "Time1Name",
    "LockDown" + "Time1SlotIds",
    "isLockdown" + "1Active",
    "isLockdown" + "1SlotToken",
]:
    require(removed_token not in service_text, f"PickLockdownPolicy.js must not contain removed token {removed_token}")

require(
    "if (isGlobalLocked(now))" in service_text,
    "Pick lockdown must enforce global lock",
)

require(
    "Boolean(state.properties.LockDown)" in service_text,
    "Pick lockdown must honor manual LockDown boolean override",
)

require(
    "Lockdown is intentionally non-visual" in service_text
    and "Picks render exactly as they did before lockdown" in service_text,
    "Pick lockdown must be non-visual; locked picks must render exactly as before lockdown",
)

require(
    "event.preventDefault()" in service_text
    and "event.stopPropagation()" in service_text
    and "event.stopImmediatePropagation" in service_text,
    "Blocked interactions must stop edit events",
)

require(
    '"click"' in service_text
    and '"pointerdown"' in service_text
    and '"touchstart"' in service_text
    and '"change"' in service_text
    and '"submit"' in service_text
    and "addEventListener(eventName, blockLockedInteraction, true)" in service_text,
    "Pick lockdown must capture edit interactions before they reach pick editors",
)

if model_path.exists():
    model_text = model_path.read_text()
    require(
        "assertPlayerPickChangeAllowed" in model_text and "policy.assertPickChangeAllowed" in model_text,
        "main MVC model setPick must enforce PickLockdownPolicy at the write boundary",
    )

if r32_controller_path.exists():
    r32_controller_text = r32_controller_path.read_text()
    require(
        "assertProjectionPickChangeAllowed" in r32_controller_text and "policy.assertPickChangeAllowed" in r32_controller_text,
        "R32 projection controller must enforce PickLockdownPolicy before pick writes",
    )

if errors:
    print("WC2026 player pick lockdown verification failed:")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("OK: first-lock gate is removed; LockDownTime2 globally freezes player picks.")
