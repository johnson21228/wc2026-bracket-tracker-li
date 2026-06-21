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

    required_index_tokens = [
        "data-rules-panel-open",
        "data-rules-panel",
        "data-rules-panel-close",
        "rules-panel-body",
        "How Bracketeering Pub-Hub works",
        "one continuous two-game World Cup pool",
        "Game 1 Rules:",
        "Before the final round of group-stage matches begins",
        "Group Stage Finale",
        "Development preview",
        "Dev Game View selector is present while the games are still being developed",
        "simulated Game 2",
        "Game 2 Preview",
        "Rule status",
    ]
    for token in required_index_tokens:
        if token not in index:
            errors.append(f"site/index.html missing single Rules panel token: {token}")

    forbidden_index_tokens = [
        "data-rules-panel-section=\"game-1\"",
        "data-rules-panel-section=\"game-2\"",
        "rules-panel-active-label",
        "Showing Game 1 rules",
        "Showing Game 2 rules",
        "Developer note",
        "Game selector is currently UI-only",
    ]
    for token in forbidden_index_tokens:
        if token in index:
            errors.append(f"site/index.html still contains obsolete selector-driven Rules token: {token}")

    for token in [
        ".rules-panel-backdrop",
        ".rules-panel",
        ".rules-panel-body",
        "overflow-y: auto",
    ]:
        if token not in css:
            errors.append(f"site/css/app.css missing rules panel styling token: {token}")

    required_runtime_tokens = [
        "function setupRulesPanel",
        "data-rules-panel-open",
        "data-rules-panel-close",
        "Escape",
    ]
    for token in required_runtime_tokens:
        if token not in app_js:
            errors.append(f"site/js/app.js missing rules panel runtime token: {token}")

    forbidden_runtime_tokens = [
        "data-rules-panel-section",
        "rulesPanelSection",
        "selectedGameValue",
        "syncRulesPanel",
        "Showing Game 1 rules",
        "Showing Game 2 rules",
    ]
    for token in forbidden_runtime_tokens:
        if token in app_js:
            errors.append(f"site/js/app.js still contains selector-driven Rules runtime token: {token}")

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

    print("OK: WC2026 Rules panel is a single player-facing Pub-Hub rules display.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
