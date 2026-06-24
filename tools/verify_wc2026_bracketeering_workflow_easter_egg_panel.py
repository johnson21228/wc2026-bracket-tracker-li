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
    "Story",
    "Workbench",
    "Workbench is the memory",
    "Workbench is for any workflow where AI can help produce, revise, verify, and preserve artifacts",
    "The Workbench is the memory.",
    "Prompts are the interface.",
    "Continuity is the product.",
    "Capture Back is the protocol.",
    "Language Infrastructure is the compounding business win.",
    "The Bracketeering site is the product. The Workbench is the factory.",
]

FORBIDDEN_RUNTIME_TOKENS = [
    "bracketeering_workflow_infographic.jpeg",
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
    runtime = workflow + "\n" + index

    require("data-workflow-panel-open" in index, "Workflow panel open control must exist.", errors)
    require("data-workflow-panel" in index, "Workflow panel backdrop must exist.", errors)
    require("setupBracketeeringWorkflowPanel(root);" in app, "App must wire workflow panel setup.", errors)
    require("role=\"tablist\"" in workflow and "role=\"tab\"" in workflow and "role=\"tabpanel\"" in workflow, "Workflow panel must use accessible tab roles.", errors)
    require("ArrowLeft" in workflow and "ArrowRight" in workflow and "Home" in workflow and "End" in workflow, "Workflow tabs must support keyboard navigation.", errors)
    require("workflow-panel-tabs" in css, "Workflow tab styling must exist.", errors)
    require("workflow-panel-tabpanel[hidden]" in css, "Hidden tab panel styling must exist.", errors)

    for token in REQUIRED_TOKENS:
        require(token in runtime, f"Runtime missing protected copy: {token}", errors)
        require(token in (doc + capture + card), f"Docs/capture/card missing protected copy: {token}", errors)

    for token in FORBIDDEN_RUNTIME_TOKENS:
        require(token.lower() not in runtime.lower(), f"Workflow panel must not expose/render forbidden runtime material: {token}", errors)

    require(
        "python3 tools/verify_wc2026_bracketeering_workflow_easter_egg_panel.py" in makefile,
        "Makefile verify must run workflow Easter egg verifier.",
        errors,
    )

    if errors:
        print("Bracketeering workflow Easter egg panel verification failed: " + "; ".join(errors))
        return 1

    print("OK: Workbench Easter egg panel has Story/Workbench tabs, protects thesis copy, and remains text-only.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
