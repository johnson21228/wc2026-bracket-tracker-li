#!/usr/bin/env python3
from pathlib import Path

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
    app_js = read("site/js/app.js")
    makefile = read("Makefile")

    for token in [
        "data-rules-panel-open",
        "data-rules-panel",
        "data-rules-panel-close",
        "data-rules-panel-section=\"game-1\"",
        "data-rules-panel-section=\"game-2\"",
        "rules-panel-body",
    ]:
        if token not in index:
            errors.append(f"site/index.html missing rules panel token: {token}")

    for text in [
        "Rules",
        "Game 1 — Pick the Round of 32 field",
        "before kickoff of the earliest third-round group-stage match",
        "Some Round-of-32 places may already be known by then",
        "Game 2 — Pick the knockout bracket",
        "Game 2 tiebreakers",
        "Higher Game 1 score",
        "Third-place pick",
        "Earliest valid Game 1 save timestamp",
    ]:
        if text not in index:
            errors.append(f"rules panel text missing: {text}")

    for token in [
        ".rules-panel-backdrop",
        ".rules-panel",
        ".rules-panel-body",
        "overflow-y: auto",
        ".rules-panel-section[hidden]",
    ]:
        if token not in css:
            errors.append(f"site/css/app.css missing rules panel styling token: {token}")

    for token in [
        "function setupRulesPanel",
        "data-rules-panel-open",
        "data-rules-panel-close",
        "data-rules-panel-section",
        "Escape",
        "rulesPanelSection",
    ]:
        if token not in app_js:
            errors.append(f"site/js/app.js missing rules panel runtime token: {token}")

    # Guard the boundary: inspect only the rules-panel runtime body so existing unrelated
    # imports/services do not fail this UI verifier. The panel may observe the UI selector,
    # but must not call into model/controller/storage APIs to switch gameplay modes.
    rules_runtime = ""
    start = app_js.find("function setupRulesPanel")
    end = app_js.find("async function main", start)
    if start != -1 and end != -1:
        rules_runtime = app_js[start:end]
    forbidden_runtime_phrases = [
        "setActiveGame",
        "switchGame",
        "activeGame =",
        "loadGame2",
        "renderGame2",
        "saveGameMode",
        "localStorage.setItem",
        "createBracketController",
        "createBracketModel",
        "Supabase",
    ]
    for phrase in forbidden_runtime_phrases:
        if phrase in rules_runtime:
            errors.append(f"rules panel runtime must not wire gameplay switching via {phrase!r}")

    if "tools/verify_wc2026_banner_rules_panel_ui.py" not in makefile:
        errors.append("Makefile verify target must run verify_wc2026_banner_rules_panel_ui.py")

    if errors:
        print("Banner rules panel UI verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 banner Rules panel shows active game rules and remains unwired from gameplay switching.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
