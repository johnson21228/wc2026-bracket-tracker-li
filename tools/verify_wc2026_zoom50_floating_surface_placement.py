#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path.cwd()


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        print(f"missing required file: {rel}", file=sys.stderr)
        raise SystemExit(1)
    return path.read_text(encoding="utf-8", errors="replace")


def require(text: str, token: str, label: str, errors: list[str]) -> None:
    if token not in text:
        errors.append(f"missing {label}: {token}")


def main() -> int:
    errors: list[str] = []
    helper = read("site/js/services/FloatingSurfacePlacement.js")
    view = read("site/js/mvc/view.js")
    r32 = read("site/js/board/R32PickMenuLayer.js")
    css = read("site/css/board.css")
    makefile = read("Makefile")
    card = read("cards/233_make_zoom50_floating_surfaces_visible_card.md")
    rule = read("li/world_cup/zoom50_floating_surface_placement_rule.md")
    docs = read("docs/features/zoom50_floating_surface_placement.md")

    for token, label in [
        ("function positionFloatingSurfaceNearAnchor", "shared placement helper"),
        ("getBoundingClientRect()", "rendered screen coordinate measurement"),
        ("DEFAULT_BOTTOM_CONTROL_SELECTORS", "bottom control selector list"),
        ("floatingSurfaceSafeBottomExcludesControls", "bottom control exclusion marker"),
        ("zoom-50-safe", "50 percent zoom safe marker"),
    ]:
        require(helper, token, label, errors)

    for token, label in [
        ("../services/FloatingSurfacePlacement.js", "MVC imports shared placement helper"),
        ("positionFloatingSurfaceNearAnchor({", "MVC uses shared placement helper"),
        ("preferredPlacement: \"right-then-left\"", "pick menu side placement preference"),
        ("preferredPlacement: \"above-then-below\"", "group panel above placement preference"),
        ("pendingGroupPanelAnchorElement", "group panel tracks rendered anchor element"),
        ("data-group-rail-layer", "bottom rail exclusion is visible to placement"),
    ]:
        require(view, token, label, errors)

    for token, label in [
        ("../services/FloatingSurfacePlacement.js", "R32 menu imports shared placement helper"),
        ("positionFloatingSurfaceNearAnchor({", "R32 menu uses shared placement helper"),
        ("preferredPlacement: \"right-then-left\"", "R32 menu placement preference"),
        ("data-group-rail-layer", "R32 bottom rail exclusion"),
    ]:
        require(r32, token, label, errors)

    for token, label in [
        ("Card 233: 50 percent zoom floating-surface placement", "CSS card marker"),
        ("--wc-z-pick-menu: 11000", "pick menu z index above buttons"),
        ("--wc-z-group-panel: 12000", "group panel z index above pick menu and buttons"),
        (".board-menu-layer", "MVC menu layer included"),
        (".board-r32-pick-menu-layer", "R32 menu layer included"),
        ("overflow: visible", "overlay layers remain unclipped"),
    ]:
        require(css, token, label, errors)

    for text, label in [(card, "card"), (rule, "LI rule"), (docs, "docs")]:
        for token in ["50% zoom", "bottom controls", "getBoundingClientRect", "fully visible"]:
            require(text, token, f"{label} token", errors)

    require(makefile, "python3 tools/verify_wc2026_zoom50_floating_surface_placement.py", "Makefile verifier registration", errors)

    if errors:
        print("WC2026 zoom-50 floating surface placement verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 50% zoom floating surfaces are shared-placement, safe-area clamped, and above bottom controls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
