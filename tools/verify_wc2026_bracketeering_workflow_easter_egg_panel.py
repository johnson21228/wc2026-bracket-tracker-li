#!/usr/bin/env python3
from pathlib import Path

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
    require(">WB</button>" in index, "Workflow easter egg button should be visible as WB.", errors)
    require("data-info-panel-open" in index and index.find("data-info-panel-open") < index.find("data-workflow-panel-open"), "Workflow button should be adjacent after the info button.", errors)
    require("data-workflow-panel" in index, "Workflow panel backdrop must exist.", errors)
    require("data-workflow-panel-body" in index, "Workflow panel must have a hydratable scroll body.", errors)
    require("setupBracketeeringWorkflowPanel(root);" in app, "App must wire workflow panel setup.", errors)
    require("WORKFLOW_PANEL_CORE_SENTENCE" in workflow and core in workflow, "Workflow panel must include the core sentence.", errors)
    require("bracketeering_workflow_infographic.jpeg" in workflow, "Workflow panel must render the JPEG infographic asset.", errors)
    require("overflow-y: auto" in css and ".workflow-panel-body" in css, "Workflow panel body must be scrollable.", errors)
    require("grid-template-columns: repeat(4, 34px)" in css, "Map icon controls should make room for the adjacent WB button.", errors)
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

    if errors:
        print("Bracketeering workflow easter egg panel verification failed: " + "; ".join(errors))
        return 1

    print("OK: Bracketeering workflow easter egg panel uses the approved JPEG asset and remains presentation-only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
