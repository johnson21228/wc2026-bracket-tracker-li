#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def text(path):
    return (ROOT / path).read_text()

def require(path, token):
    body = text(path)
    if token not in body:
        raise SystemExit(f"Missing {token!r} in {path}")

require("site/js/mvc/view.js", "function activeGameValue()")
require("site/js/mvc/view.js", "function slotEnabledForActiveGame(slot)")
require("site/js/mvc/view.js", 'if (activeGame === "game-1") return slot.round === "R32";')
require("site/js/mvc/view.js", 'if (activeGame === "game-2") return slot.round !== "R32";')
require("site/js/mvc/view.js", "button.dataset.pickDisabledByActiveGame")
require("site/js/mvc/view.js", "is-disabled-by-active-game")
require("site/js/mvc/view.js", "onActiveGameChange?.(activeGameValue())")
require("site/js/mvc/view.js", "activeGameValue };")

require("site/js/mvc/controller.js", "function slotAllowedForActiveGame(slot)")
require("site/js/mvc/controller.js", 'if (activeGame === "game-1") return slot.round === "R32";')
require("site/js/mvc/controller.js", 'if (activeGame === "game-2") return slot.round !== "R32";')
require("site/js/mvc/controller.js", "function onActiveGameChange(activeGame)")
require("site/js/mvc/controller.js", "onActiveGameChange });")

require("site/css/app.css", ".pick-slot-button.is-disabled-by-active-game")
require("site/index.html", "js/app.js?v=active-game-pick-gating")
require("site/index.html", "css/app.css?v=active-game-pick-gating")

view = text("site/js/mvc/view.js")
start = view.index("function slotEnabledForActiveGame")
end = view.index("function renderBoardShell")
gated_segment = view[start:end]

forbidden_hide_tokens = [
    "display: none",
    "visibility: hidden",
    "hidden = true",
    ".style.display =",
]
for token in forbidden_hide_tokens:
    if token in gated_segment:
        raise SystemExit(f"Active-game pick gating must disable, not hide; found {token!r}")

print("OK: active Game selector disables wrong-game pick surfaces without hiding bracket cells.")
