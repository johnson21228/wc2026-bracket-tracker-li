#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"Missing required file: {rel}")
    return path.read_text(encoding="utf-8", errors="ignore")


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    index = read("site/index.html")
    app = read("site/js/app.js")
    css = read("site/css/app.css")
    workflow = read("site/js/workflow/BracketeeringWorkflowPanel.js")
    card = read("cards/1004_add_bracketeering_workflow_easter_egg_panel_card.md")
    makefile = read("Makefile")

    jpeg = ROOT / "site/assets/visuals/bracketeering_workflow/bracketeering_workflow_infographic.jpeg"
    core = "The game evolves because the Workbench keeps code, intent, and verification aligned."

    require(jpeg.exists(), "JPEG infographic must exist at the durable Pages asset path.", errors)
    require(jpeg.exists() and jpeg.stat().st_size > 100_000, "JPEG infographic should be a real image asset, not an empty placeholder.", errors)
    require("data-workflow-panel-open" in index, "Visible workflow panel open control must exist in index.", errors)
    require(">wb</button>" in index, "Workflow easter egg button should be visible as small lowercase wb.", errors)
    require("workflow-floating-button" in index, "Workflow easter egg control must be the lower-right floating button.", errors)
    rail_match = re.search(r'<div class="map-board-icon-controls"[^>]*>.*?</div>', index, re.DOTALL)
    require(rail_match is not None, "Map icon controls rail must exist.", errors)
    if rail_match is not None:
        rail = rail_match.group(0)
        require("data-board-zoom-in" in rail, "Upper-left map controls must keep + zoom.", errors)
        require("data-info-panel-open" in rail, "Upper-left map controls must keep i info.", errors)
        require("data-board-zoom-out" in rail, "Upper-left map controls must keep − zoom.", errors)
        require("data-workflow-panel-open" not in rail, "Upper-left map controls must not contain the workflow easter egg.", errors)
        require("workflow-map-button" not in rail, "Upper-left map controls must not contain the old workflow map button.", errors)
    require("data-workflow-panel" in index, "Workflow panel backdrop must exist.", errors)
    require("data-workflow-panel-body" in index, "Workflow panel must have a hydratable scroll body.", errors)
    require("setupBracketeeringWorkflowPanel(root);" in app, "App must wire workflow panel setup.", errors)
    require("WORKFLOW_PANEL_CORE_SENTENCE" in workflow and core in workflow, "Workflow panel must include the core sentence.", errors)
    require("bracketeering_workflow_infographic.jpeg" in workflow, "Workflow panel must render the JPEG infographic asset.", errors)
    require("overflow-y: auto" in css and ".workflow-panel-body" in css, "Workflow panel body must be scrollable.", errors)
    require(".workflow-floating-button" in css and "position: fixed" in css and "bottom:" in css and "right:" in css, "Workflow easter egg button must be fixed in the lower-right corner.", errors)
    require("opacity: 0" in css and "pointer-events: auto" in css, "Workflow easter egg button must be invisible by default but still tappable.", errors)
    require(".workflow-floating-button:hover" in css and ".workflow-floating-button:focus-visible" in css and "opacity: 1" in css, "Workflow easter egg button must become visible on mouse hover or keyboard focus.", errors)
    require("Download / Apply Pattern" in card and core in card, "Card must capture Download/Apply and the core sentence.", errors)
    require("python3 tools/verify_wc2026_bracketeering_workflow_easter_egg_panel.py" in makefile, "Makefile verify must run workflow easter egg verifier.", errors)

    forbidden_runtime_tokens = [
        '.from("user_brackets")',
        ".from('user_brackets')",
        ".from(`user_brackets`)",
        "bracket_json",
        "picks_json",
    ]
    combined_runtime = "\n".join([index, app, workflow])
    for token in forbidden_runtime_tokens:
        require(token.lower() not in combined_runtime.lower(), f"Workflow panel must not introduce remote bracket persistence: {token}", errors)

    require("width: 76px" in css and "height: 76px" in css, "Workflow easter egg button must use a larger invisible pointer hit target.", errors)
    require(".workflow-floating-button::before" in css and "width: 34px" in css and "height: 34px" in css, "Workflow easter egg button must render the small visible wb affordance inside the larger hit target.", errors)

    require(
        ".workflow-floating-button::after" in css
        and 'content: "wb"' in css
        and "display: inline-flex" in css
        and "align-items: center" in css
        and "justify-content: center" in css,
        "Workflow easter egg wb glyph must be centered by the 34px visual affordance pseudo-element.",
        errors,
    )
    require(
        ".workflow-floating-button-label" not in css,
        "Workflow easter egg centering must not depend on an unused runtime label wrapper.",
        errors,
    )
    if errors:
        print("Bracketeering workflow easter egg panel verification failed: " + "; ".join(errors))
        return 1

    print("OK: Bracketeering workflow easter egg panel uses the approved JPEG asset and remains presentation-only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
