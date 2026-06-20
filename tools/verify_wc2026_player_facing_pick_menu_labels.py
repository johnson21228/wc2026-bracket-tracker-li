#!/usr/bin/env python3
from pathlib import Path
import re
import sys

errors = []

js_path = Path("site/js/board/R32PickMenuLayer.js")
js = js_path.read_text()

required = [
    "playerFacingSlotLabel",
    "playerFacingMenuSubtitle",
    "scrubPlayerFacingText",
    "scrubPlayerFacingTree(popover)",
    "Group ${firstGroup} winner",
    "Group ${firstGroup} runner-up",
    "Possible third-place teams",
    "Pick a possible winner",
]

for token in required:
    if token not in js:
        errors.append(f"missing player-facing menu token: {token}")

scrub_coverage = [
    ("THIRD-PLACE-CANDIDATE-SET", "third-place internal source kind"),
    ("KNOCKOUT-FEEDER", "knockout internal source kind"),
    ("Feeder choices", "feeder choices heading"),
    ("candidate-set", "candidate-set wording"),
    ("knockout-feeder", "knockout-feeder wording"),
    ("Winner from", "winner-from raw heading"),
    ("L-R32-", "raw R32 feeder ids"),
    ("previous matches", "player-facing previous-match replacement"),
]

for token, description in scrub_coverage:
    if token not in js:
        errors.append(f"missing scrub coverage for {description}: {token}")

if re.search(r"headingTitle\.textContent\s*=\s*logicSlot\.fifaLabel", js):
    errors.append("menu heading still directly renders logicSlot.fifaLabel")

if re.search(r"subtitle\.textContent\s*=\s*title", js):
    errors.append("menu subtitle still directly renders raw title")

if re.search(r"label\.textContent\s*=\s*logicSlot\.fifaLabel", js):
    errors.append("slot button label still directly renders logicSlot.fifaLabel")


compact_required = [
    "Group $1 winner",
    "Group $1 runner-up",
    "\\b1([A-L])\\b",
    "\\b2([A-L])\\b",
    "\\b3\\s+[A-L]{2,}\\b",
]

for token in compact_required:
    if token not in js:
        errors.append(f"missing compact slot-code player-facing scrub coverage: {token}")

if errors:
    print("WC2026 player-facing pick menu label verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: WC2026 pick menus render player-facing labels and scrub internal source terms.")
