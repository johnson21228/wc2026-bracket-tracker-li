#!/usr/bin/env python3
from pathlib import Path
import re
import sys

html_path = Path("site/index.html")
html = html_path.read_text()
errors = []

required = [
    "WC2026_GAME1_PICK_STATE",
    "WC2026_GAME1_CANONICAL_PICK_STATE_MODEL_START",
    "WC2026_CARD155_RENDER_FROM_CANONICAL_PICK_STATE",
    "WC2026_CARD155_PATCH_ADORNMENTS_FROM_CANONICAL_PICK_STATE",
    "function storedPickForSlot(slotId)",
    "function canonicalPickIsRenderableForRule(rule, pick)",
    "model.getPick(slotId)",
    "model.isPickValid(slotId)",
]
for token in required:
    if token not in html:
        errors.append(f"missing required token: {token}")

stored_block = re.search(r"function storedPickForSlot\(slotId\)\{(?P<body>.*?)\n  \}", html, re.S)
if not stored_block:
    errors.append("missing storedPickForSlot function")
else:
    body = stored_block.group("body")
    if "WC2026_GAME1_PICK_STATE" not in body and "wc2026CanonicalPickStateModel" not in body:
        errors.append("storedPickForSlot does not route through canonical model")
    if "return bracket[slotId] || r16[slotId] || qfSf[slotId] || null;" in body and "model.getPick" not in body:
        errors.append("storedPickForSlot still uses only direct legacy storage")

if "if (!storedKnockoutPickIsRenderable(rule, pick))" in html:
    errors.append("stored render still gates directly through storedKnockoutPickIsRenderable instead of canonical wrapper")

patch_block = re.search(r"function patchStoredKnockoutCards\(\)\{(?P<body>.*?)\n  \}\n\n  const previousRenderPicks", html, re.S)
if not patch_block:
    errors.append("missing patchStoredKnockoutCards block")
else:
    body = patch_block.group("body")
    if "localStorage" in body or "JSON.parse" in body or "readJson" in body:
        errors.append("patchStoredKnockoutCards still reads storage directly")
    if "WC2026_GAME1_PICK_STATE" not in body or "model.getPick" not in body:
        errors.append("patchStoredKnockoutCards does not read canonical model")
    if "model.isPickValid" not in body:
        errors.append("patchStoredKnockoutCards does not validate canonical pick before patching")

card = Path("cards/155_route_game1_rendering_through_canonical_pick_state_model_card.md")
if not card.exists():
    errors.append("missing Card 155")

if errors:
    print("WC2026 Game 1 canonical rendering verifier FAILED:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("WC2026 Game 1 canonical rendering verifier passed.")
