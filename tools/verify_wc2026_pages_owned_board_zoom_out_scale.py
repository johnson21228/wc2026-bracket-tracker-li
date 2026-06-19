#!/usr/bin/env python3
from pathlib import Path

required = {
    "captures/CAPTURE_BACK_PAGES_OWNED_BOARD_ZOOM_OUT_SCALE.md": [
        "All board actors speak native gameboard coordinates",
        "Supabase/Postgres must not know about board zoom",
        "Backout posture",
    ],
    "cards/223_add_pages_owned_board_zoom_out_scale_card.md": [
        "Card 223: Add Pages-Owned Board Zoom-Out Scale",
        "All View and Controller work stays inside the Pages site",
        "Supabase is durable Model persistence only",
        "Do not change Supabase SQL",
        "The feature can be backed out with a single revert commit",
    ],
    "docs/features/pages_owned_board_zoom_out_scale.md": [
        "native board coordinate -> View render scale -> browser pixels",
        "Zoom-out requires an explicit render scale below `1.0`",
        "no `picks_json` changes",
    ],
    "li/world_cup/pages_owned_board_zoom_out_scale_rule.md": [
        "Board zoom is Pages site View/Controller behavior",
        "Only the Pages View shell converts native coordinates to rendered screen coordinates",
        "Supabase stores durable model data only",
    ],
    "prompts/implement_pages_owned_board_zoom_out_scale.md": [
        "Support board render scales below 100%",
        "Do not rewrite geometry manifests into scaled coordinates",
        "Keep the change isolated and easy to revert",
    ],
}

missing = []
for path_text, tokens in required.items():
    path = Path(path_text)
    if not path.exists():
        missing.append(f"missing file: {path_text}")
        continue
    text = path.read_text()
    for token in tokens:
        if token not in text:
            missing.append(f"{path_text}: missing token {token!r}")

makefile = Path("Makefile").read_text()
if "python3 tools/verify_wc2026_pages_owned_board_zoom_out_scale.py" not in makefile:
    missing.append("Makefile: verifier is not wired into make verify")

map_text = Path("MAP.md").read_text()
for token in [
    "Pages-Owned Board Zoom-Out Scale",
    "cards/223_add_pages_owned_board_zoom_out_scale_card.md",
    "tools/verify_wc2026_pages_owned_board_zoom_out_scale.py",
]:
    if token not in map_text:
        missing.append(f"MAP.md: missing token {token!r}")

if missing:
    raise SystemExit("\n".join(missing))

print("OK: WC2026 Pages-owned board zoom-out scale LI is captured and verified.")
