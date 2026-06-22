#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def require_contains(path: Path, needle: str, errors: list[str], label: str | None = None) -> None:
    text = path.read_text()
    if needle not in text:
        errors.append(label or f"{path} missing {needle!r}")


def require_not_contains(path: Path, needle: str, errors: list[str], label: str | None = None) -> None:
    text = path.read_text()
    if needle in text:
        errors.append(label or f"{path} unexpectedly contains {needle!r}")


def main() -> int:
    view = ROOT / "site/js/mvc/view.js"
    app_css = ROOT / "site/css/app.css"
    makefile = ROOT / "Makefile"
    docs = ROOT / "docs/features/mouse_drag_board_pan.md"
    li = ROOT / "li/world_cup/mouse_drag_board_pan_rule.md"
    card = ROOT / "cards/251_mouse_drag_board_pan_card.md"
    capture = ROOT / "captures/CAPTURE_BACK_MOUSE_DRAG_BOARD_PAN.md"

    errors: list[str] = []
    for path in [view, app_css, makefile, docs, li, card, capture]:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    if errors:
        print("WC2026 mouse drag board pan verification failed: " + "; ".join(errors))
        return 1

    view_text = view.read_text()
    css_text = app_css.read_text()

    required_view_tokens = [
        ("function installMouseBoardDragPan()", "missing View-owned board drag-pan installer"),
        ("function isBoardPanInteractiveTarget(target)", "missing interactive target exclusion helper"),
        ("event.pointerType === \"touch\"", "missing explicit touch guard"),
        ("event.pointerType && event.pointerType !== \"mouse\"", "missing mouse-only pointer guard"),
        ("event.button !== 0", "missing left-button-only guard"),
        ("!event.isPrimary", "missing primary pointer guard"),
        ("BOARD_DRAG_PAN_THRESHOLD_PX", "missing small drag threshold"),
        ("setPointerCapture", "missing mouse pointer capture for drag-pan"),
        ("pointerdown", "missing pointerdown handler"),
        ("pointermove", "missing pointermove handler"),
        ("pointerup", "missing pointerup handler"),
        ("pointercancel", "missing pointercancel handler"),
        ("lostpointercapture", "missing lostpointercapture cleanup"),
        ("boardScroll.scrollLeft = dragState.startScrollLeft - deltaX", "drag-pan must mutate scrollLeft only for horizontal pan"),
        ("boardScroll.scrollTop = dragState.startScrollTop - deltaY", "drag-pan must mutate scrollTop only for vertical pan"),
        ("installMouseBoardDragPan();", "drag-pan installer must be wired into setHandlers"),
        (".pick-menu-popover", "interactive exclusions must include pick menu popovers"),
        (".group-panel-popover", "interactive exclusions must include group panel popovers"),
        ("[data-menu-layer]", "interactive exclusions must include menu layer"),
        ("[data-group-panel-layer]", "interactive exclusions must include group panel layer"),
        ("[data-board-zoom]", "interactive exclusions must include zoom controls"),
    ]
    for token, message in required_view_tokens:
        if token not in view_text:
            errors.append(message)

    forbidden_view_tokens = [
        "touchstart",
        "touchmove",
        "gesturestart",
        "gesturechange",
        "touch-action: none",
    ]
    for token in forbidden_view_tokens:
        if token in view_text:
            errors.append(f"custom touch/pinch gesture token should not appear in view.js: {token}")

    required_css_tokens = [
        ("Card 251: mouse-only map-style board drag-pan affordance", "missing CSS marker for drag-pan affordance"),
        (".board-scroll", "missing board scroll CSS target"),
        ("cursor: grab", "missing grab cursor"),
        (".board-scroll.is-drag-panning", "missing dragging class CSS"),
        ("cursor: grabbing", "missing grabbing cursor"),
        ("user-select: none", "missing text-selection suppression while dragging"),
        ("-webkit-overflow-scrolling: touch", "native iOS scrolling polish should remain explicit"),
    ]
    for token, message in required_css_tokens:
        if token not in css_text:
            errors.append(message)

    if "touch-action: none" in css_text:
        errors.append("CSS must not globally disable touch navigation with touch-action: none")

    require_contains(makefile, "python3 tools/verify_wc2026_mouse_drag_board_pan.py", errors, "Makefile does not run mouse drag board pan verifier")
    
    if "mouse-only" not in docs.read_text().lower():
        errors.append("feature doc should name mouse-only scope")
    require_contains(li, "touch", errors, "LI rule should preserve touch navigation boundary")
    require_contains(capture, "Do not disturb iPad/iPhone browser touch navigation", errors, "capture back should preserve touch navigation constraint")


    card_251_css_match = re.search(
        r"/\* Card 251: mouse-only map-style board drag-pan affordance\. \*/\s*\.board-scroll\s*\{(?P<body>[^}]*)\}",
        css_text,
        re.S,
    )
    if not card_251_css_match:
        errors.append("missing Card 251 board-scroll CSS block")
    elif "overscroll-behavior" in card_251_css_match.group("body"):
        errors.append("Card 251 board-scroll CSS must not contain overscroll-behavior because MacBook trackpad scroll chaining should remain native")


    if errors:
        print("WC2026 mouse drag board pan verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 board has mouse-only map-style drag-pan while preserving native touch navigation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
