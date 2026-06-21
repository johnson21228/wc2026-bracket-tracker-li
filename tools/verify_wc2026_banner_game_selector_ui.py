#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        raise AssertionError(f"Missing required file: {path}")
    return target.read_text()

def main() -> int:
    errors = []
    index = read("site/index.html")
    css = read("site/css/app.css")
    makefile = read("Makefile")

    if "data-dev-game-selector" not in index:
        errors.append("site/index.html must include data-dev-game-selector")
    if "Developer game selector" not in index:
        errors.append("selector should be explicitly developer-facing for accessibility")

    game1_pattern = re.compile(r'<input[^>]+type="radio"[^>]+name="dev-game-view"[^>]+value="game-1"[^>]+checked', re.S)
    if not game1_pattern.search(index):
        errors.append("Game 1 radio option must exist and be checked by default")

    game2_pattern = re.compile(r'<input[^>]+type="radio"[^>]+name="dev-game-view"[^>]+value="game-2"', re.S)
    if not game2_pattern.search(index):
        errors.append("Game 2 radio option must exist")
    game2_input = game2_pattern.search(index)
    if game2_input and "checked" in game2_input.group(0):
        errors.append("Game 2 must not be checked by default")

    for label in ["Game 1", "Game 2", "Dev game view"]:
        if label not in index:
            errors.append(f"selector label missing: {label}")

    for token in [".dev-game-selector", ".dev-game-selector-option", "input:checked + span"]:
        if token not in css:
            errors.append(f"site/css/app.css missing selector styling token: {token}")

    js_paths = [ROOT / "site/js/app.js", ROOT / "site/js/mvc/controller.js", ROOT / "site/js/mvc/model.js", ROOT / "site/js/mvc/view.js"]
    for js_path in js_paths:
        if not js_path.exists():
            continue
        js = js_path.read_text()
        for token in ["dev-game-view", "data-dev-game-selector", "game-2"]:
            if token in js:
                errors.append(f"{js_path.relative_to(ROOT)} must not wire banner game selector into runtime JS via {token!r}")

    if "tools/verify_wc2026_banner_game_selector_ui.py" not in makefile:
        errors.append("Makefile verify target must run verify_wc2026_banner_game_selector_ui.py")

    if errors:
        print("Banner Game selector UI verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("OK: WC2026 banner Game selector UI is present, defaults to Game 1, and remains unwired from gameplay runtime.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
