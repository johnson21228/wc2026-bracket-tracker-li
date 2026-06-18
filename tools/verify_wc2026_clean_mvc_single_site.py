#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys

ROOT = Path.cwd()


def fail(title: str, items: list[str]) -> None:
    print(title)
    for item in items:
        print(f"- {item}")
    raise SystemExit(1)


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        fail("Missing required clean MVC file:", [rel])
    return path.read_text(encoding="utf-8", errors="replace")


def require_tokens(label: str, rel: str, tokens: list[str]) -> None:
    text = read(rel)
    missing = [token for token in tokens if token not in text]
    if missing:
        fail(f"{label} tokens missing:", [f"{rel}: {token}" for token in missing])


def node_check(rel: str) -> None:
    result = subprocess.run(["node", "--check", str(ROOT / rel)], text=True, capture_output=True)
    if result.returncode != 0:
        fail("JS syntax check failed:", [f"{rel}: {result.stderr or result.stdout}"])


def main() -> int:
    required = [
        "site/index.html",
        "site/js/app.js",
        "site/js/mvc/model.js",
        "site/js/mvc/view.js",
        "site/js/mvc/controller.js",
        "site/css/app.css",
        "site/css/board.css",
        "site/css/dev.css",
        "cards/182_make_single_site_clean_mvc_runtime_card.md",
        "capture_back/CAPTURE_BACK_CLEAN_MVC_SINGLE_SITE.md",
        "docs/architecture/clean_mvc_single_site_runtime.md",
        "li/world_cup/clean_mvc_single_site_runtime_rule.md",
    ]
    missing = [rel for rel in required if not (ROOT / rel).exists()]
    if missing:
        fail("Missing clean MVC files:", missing)

    html = read("site/index.html")
    if '<main id="wc2026-app"' not in html or 'src="js/app.js"' not in html:
        fail("Single site shell is not wired to app.js:", ["site/index.html"])
    if "mvc-test.html" in html:
        fail("Single site must not link to a separate MVC test page:", ["site/index.html"])

    app = read("site/js/app.js")
    forbidden_imports = ["./board/", "./dev/", "R32PickMenuLayer", "BoardShell", "DeveloperFrame"]
    bad_imports = [token for token in forbidden_imports if token in app]
    if bad_imports:
        fail("app.js imports old board/dev runtime:", [f"site/js/app.js: {token}" for token in bad_imports])
    require_tokens("app.js", "site/js/app.js", ["./mvc/model.js", "./mvc/view.js", "./mvc/controller.js", "createBracketModel", "createBracketView", "createBracketController"])

    require_tokens("Model", "site/js/mvc/model.js", ["BOARD_NATIVE_SIZE", "1536", "1024", "buildDependencyMap", "cascadeClearInvalidDescendants", "getR32Choices", "getKnockoutChoices", "validatePick", "CENTER-FINAL-FOUR"])
    require_tokens("View", "site/js/mvc/view.js", ["renderBoardShell", "renderSlots", "renderMenu", "pick-slot-button", "pick-menu-popover"])
    require_tokens("Controller", "site/js/mvc/controller.js", ["onSlotClick", "onTeamPick", "onClearPick", "onClearAll", "redraw"])
    require_tokens("CSS pointer contract", "site/css/board.css", ["pointer-events: none", "pointer-events: auto", "--board-w-px", "--board-h-px"])
    require_tokens("LI rule", "li/world_cup/clean_mvc_single_site_runtime_rule.md", ["one site entry point", "Model owns", "View owns", "Controller owns", "downstream pick"])

    geometry = json.loads(read("site/data/geometry/gameboard_manifest.json"))
    native = geometry.get("nativeSizePx", {})
    if native.get("width") != 1536 or native.get("height") != 1024:
        fail("Geometry native size must remain 1536x1024:", ["site/data/geometry/gameboard_manifest.json"])
    rounds = {slot.get("round") for slot in geometry.get("slots", [])}
    for required_round in ["R32", "R16", "QF", "SF", "FINAL_FOUR"]:
        if required_round not in rounds:
            fail("Geometry missing required round:", [required_round])

    for rel in ["site/js/app.js", "site/js/mvc/model.js", "site/js/mvc/view.js", "site/js/mvc/controller.js"]:
        node_check(rel)

    print("WC2026 clean MVC single-site verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
