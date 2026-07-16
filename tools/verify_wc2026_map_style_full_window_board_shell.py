#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"WC2026 map-style full-window board shell verification failed: {message}")


def require_contains(text: str, token: str, label: str) -> None:
    if token not in text:
        fail(f"missing {label}: {token}")


def main() -> int:
    index = (ROOT / "site/index.html").read_text()
    app_css = (ROOT / "site/css/app.css").read_text()
    view_js = (ROOT / "site/js/mvc/view.js").read_text()

    for hook in [
        "data-rules-panel-open",
        'data-action="clear-all"',
        "data-board-zoom",
        "data-dev-game-selector",
        "data-supabase-identity-surface",
        "data-status-panel",
        "data-board-scroll",
        "data-board-scale-frame",
        "data-board-plane",
    ]:
        require_contains(index, hook, "required runtime hook")

    require_contains(index, "css/app.css?v=map-style-full-window-board", "map-style CSS cache tag")
    require_contains(view_js, 'src="assets/playfield/uniform_pick_card_gameboard.svg"', "single SVG truth linework source")

    require_contains(app_css, "Card 260: map-style full-window board shell", "Card 260 CSS marker")
    require_contains(app_css, ".board-scroll {", "board scroll CSS rule")
    require_contains(app_css, "position: fixed;", "fixed overlay/full-window positioning")
    require_contains(app_css, "inset: 0;", "full-window board inset")
    require_contains(app_css, ".app-header {", "header overlay CSS rule")
    require_contains(app_css, "pointer-events: none;", "overlay shell pass-through")
    require_contains(app_css, ".app-actions {", "action overlay CSS rule")
    require_contains(app_css, "pointer-events: auto;", "control interactivity preservation")
    require_contains(app_css, ".status-panel {", "status overlay CSS rule")

    hidden_hero_pattern = re.compile(
        r"\.app-header\s+\.eyebrow,\s*\.app-header\s+h1,\s*\.app-header\s+\.app-summary\s*\{[^}]*display:\s*none;",
        re.MULTILINE | re.DOTALL,
    )
    if not hidden_hero_pattern.search(app_css):
        fail("hero/banner text is not hidden by the map-style shell CSS")

    marker_index = app_css.index("Card 260: map-style full-window board shell")
    override = app_css[marker_index:]
    require_contains(override, "padding: 0;", "Card 260 app padding override")

    print("OK: WC2026 page chrome is converted to a map-style full-window board shell with required overlay hooks preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
