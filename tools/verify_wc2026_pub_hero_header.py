#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path.cwd()

def fail(title, items):
    print(title)
    for item in items:
        print(f"- {item}")
    sys.exit(1)

def read(path):
    return (ROOT / path).read_text(encoding="utf-8", errors="replace")

def main():
    required_files = [
        "site/index.html",
        "site/js/mvc/view.js",
        "site/js/mvc/controller.js",
        "site/js/mvc/model.js",
        "li/world_cup/pub_hero_header_rule.md",
        "docs/features/pub_hero_header.md",
        "cards/197_define_pub_hero_header_card.md",
        "capture_back/CAPTURE_BACK_PUB_HERO_HEADER.md",
    ]
    missing = [p for p in required_files if not (ROOT / p).exists()]
    if missing:
        fail("Missing pub hero header files:", missing)

    html = read("site/index.html")
    html_tokens = [
        'class="eyebrow">World Cup 2026</p>',
        '<h1 id="app-title">Bracketeering Hub</h1>',
        'Scroll and zoom the game board below and make your picks.',
        'data-action="clear-all"',
                                            ]
    missing_html = [t for t in html_tokens if t not in html]
    if missing_html:
        fail("Pub hero header required HTML tokens missing:", missing_html)

    stale = [
        "World Cup 2026 Bracket Tracker",
        "Clean MVC runtime: one site",
    ]
    present = [t for t in stale if t in html]
    if present:
        fail("Implementation-facing hero copy still present:", present)

    view = read("site/js/mvc/view.js")
    view_tokens = [
                                                    ]
    missing_view = [t for t in view_tokens if t not in view]
    if missing_view:
        fail("Pub hero header required view wiring tokens missing:", missing_view)

    controller = read("site/js/mvc/controller.js")
    controller_tokens = [
        "function onExportPicks()",
        "function onImportPicks",
        "exportPicksSnapshot",
        "importPicksSnapshot",
        "braketeering-pub-picks",
    ]
    missing_controller = [t for t in controller_tokens if t not in controller]
    if missing_controller:
        fail("Pub hero header controller wiring tokens missing:", missing_controller)

    model = read("site/js/mvc/model.js")
    model_tokens = [
        "function exportPicksSnapshot()",
        "function importPicksSnapshot",
        "wc2026.braketeeringPub.picks",
        "picks: { ...picks }",
    ]
    missing_model = [t for t in model_tokens if t not in model]
    if missing_model:
        fail("Pub hero header model snapshot tokens missing:", missing_model)

    makefile = read("Makefile")
    if "python3 tools/verify_wc2026_pub_hero_header.py" not in makefile:
        fail("Makefile does not run pub hero header verifier:", ["Makefile"])


    forbidden_player_storage_tokens = [
        'data-action="export-picks"',
        'data-action="import-picks"',
        'data-import-picks-file',
        'Export picks',
        'Import picks',
        'Capture Picks',
        'Capture picks',
    ]

    forbidden_present = [token for token in forbidden_player_storage_tokens if token in html]
    if forbidden_present:
        print("Player-facing storage UI tokens must not be present:")
        for token in forbidden_present:
            print(f"- {token}")
        return 1


    forbidden_player_storage_view_tokens = [
        "onExportPicks",
        "onImportPicks",
        "readAsText",
    ]

    view_text_for_storage_check = Path("site/js/mvc/view.js").read_text()
    forbidden_view_present = [
        token
        for token in forbidden_player_storage_view_tokens
        if token in view_text_for_storage_check
    ]
    if forbidden_view_present:
        print("Player-facing storage view wiring must not be present:")
        for token in forbidden_view_present:
            print(f"- {token}")
        return 1

    print("OK: WC2026 pub hero header LI and runtime are captured and verified.")

if __name__ == "__main__":
    main()
