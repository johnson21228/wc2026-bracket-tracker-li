#!/usr/bin/env python3
from pathlib import Path

def require(text, token, label, errors):
    if token not in text:
        errors.append(f"missing {label}: {token}")

def forbid(text, token, label, errors):
    if token in text:
        errors.append(f"unexpected {label}: {token}")

def main():
    errors = []

    service = Path("site/js/services/FloatingSurfaceDismissal.js").read_text()
    view = Path("site/js/mvc/view.js").read_text()
    r32 = Path("site/js/board/R32PickMenuLayer.js").read_text()
    controller = Path("site/js/mvc/controller.js").read_text()
    makefile = Path("Makefile").read_text()

    require(service, "export function registerFloatingSurfaceDismissal", "shared dismissal service export", errors)
    require(service, 'root.addEventListener("pointerdown", handlePointerDown, true)', "capture-phase pointer dismissal", errors)
    require(service, 'root.addEventListener("keydown", handleKeyDown, true)', "Escape dismissal", errors)
    require(service, "isInsideSelector(element, surfaces)", "inside-surface guard", errors)
    require(service, "return function teardownFloatingSurfaceDismissal()", "listener teardown return", errors)

    require(view, 'import { registerFloatingSurfaceDismissal } from "../services/FloatingSurfaceDismissal.js";', "MVC View imports dismissal service", errors)
    require(view, "function dismissFloatingSurfaces()", "MVC View-owned dismiss function", errors)
    require(view, 'surfaceSelectors: [".pick-menu-popover", ".group-panel-popover"]', "MVC menu and group panel selectors", errors)
    require(view, "handlers.onCloseMenu?.();", "MVC preserves controller menu close seam", errors)
    require(view, "renderGroupPanel(null);", "MVC closes group panel without controller change", errors)
    require(view, "dismissFloatingSurfaces();", "MVC Escape uses shared dismiss path", errors)

    require(r32, 'import { registerFloatingSurfaceDismissal } from "../services/FloatingSurfaceDismissal.js";', "R32 layer imports dismissal service", errors)
    require(r32, 'surfaceSelectors: [".r32-pick-menu-popover"]', "R32 popover dismissal selector", errors)
    require(r32, "onDismiss: () => closeExistingMenu(layer)", "R32 closes existing menu from View/layer code", errors)

    require(makefile, "python3 tools/verify_wc2026_floating_surface_dismissal_view_owned.py", "Makefile verifier wiring", errors)

    forbid(controller, "FloatingSurfaceDismissal", "controller dismissal dependency", errors)
    forbid(controller, "dismissFloatingSurfaces", "controller dismiss function", errors)

    if errors:
        print("Floating surface dismissal verification failed: " + "; ".join(errors))
        return 1

    print("OK: floating surface dismissal is View-owned and closes open pick menus/group panels without controller changes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
