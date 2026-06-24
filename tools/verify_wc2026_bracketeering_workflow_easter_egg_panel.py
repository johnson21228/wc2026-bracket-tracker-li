#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TOKENS = [
    "Built with Workbench",
    "This site was built in a new way.",
    "The old way",
    "Raw AI assistance",
    "Workbench + AI",
    "Workbench thesis",
    "The card changes the artifact.",
    "The artifact is verified.",
    "Workbench is not just for coding.",
    "The point is that it was built in a new way.",
    "The Bracketeering site is the product. The Workbench is the factory.",
]

FORBIDDEN_WORKFLOW_TOKENS = [
    "service_role",
    "auth.uid",
    "bracket_json",
    "picks_json",
]


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

    workflow = read("site/js/workflow/BracketeeringWorkflowPanel.js")
    index = read("site/index.html")
    app = read("site/js/app.js")
    css = read("site/css/app.css")
    doc = read("docs/features/workbench_story_easter_egg_copy.md")
    capture = read("captures/CAPTURE_BACK_WORKBENCH_STORY_EASTER_EGG_COPY.md")
    card = read("cards/284_workbench_story_easter_egg_copy_card.md")
    makefile = read("Makefile")

    require("data-workflow-panel-open" in index, "Workflow panel open control must exist.", errors)
    require("data-workflow-panel" in index, "Workflow panel backdrop must exist.", errors)
    require("setupBracketeeringWorkflowPanel(root);" in app, "App must wire workflow panel setup.", errors)
    require("workflow-panel-subheading" in css, "Visible section heading styling must exist.", errors)
    require("workflow-panel-copy-list" in css, "Workflow loop list styling must exist.", errors)
    require("workflow-panel-closing" in css, "Closing line styling must exist.", errors)

    require(
        "bracketeering_workflow_infographic.jpeg" not in workflow and "bracketeering_workflow_infographic.jpeg" not in index,
        "Workbench Easter egg panel must not render the old workflow infographic.",
        errors,
    )

    for token in REQUIRED_TOKENS:
        require(token in workflow, f"Workflow panel missing protected copy: {token}", errors)
        require(token in (doc + capture + card), f"Docs/capture/card missing protected copy: {token}", errors)

    for token in FORBIDDEN_WORKFLOW_TOKENS:
        require(token.lower() not in workflow.lower(), f"Workflow panel must not expose private persistence material: {token}", errors)

    require(
        "python3 tools/verify_wc2026_bracketeering_workflow_easter_egg_panel.py" in makefile,
        "Makefile verify must run workflow Easter egg verifier.",
        errors,
    )

    if errors:
        print("Bracketeering workflow Easter egg panel verification failed: " + "; ".join(errors))
        return 1

    print("OK: Workbench Easter egg panel frames Bracketeering as a new build path and protects the thesis copy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
