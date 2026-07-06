#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_RUNTIME_TOKENS = [
    "Built with Workbench",
    "This site was built in a new way.",
    "Workbench + AI",
    "The AI helped make things. The Workbench kept the work coherent.",
    "Story",
    "Workbench",
    "C64 Loop",
    "Personal Bearocrat",
    "Workbench is the memory",
    "Workbench keeps the middle from disappearing.",
    "Prompts are the interface.",
    "Continuity is the product.",
    "Capture Back is the protocol.",
    "Language Infrastructure is the compounding win.",
    "The site is the product. The Workbench is the factory.",
    "The C64 is not the point. It is just a tiny world where the rules are visible.",
    "Your Personal Bearocrat",
    "Every Inference Interface needs one.",
    "A WB is your personal bearocrat",
    "Inference Interface asks.",
    "WB Loop curates.",
    "Capture Back remembers.",
]

REQUIRED_SUPPORTING_ARTIFACTS = [
    "docs/features/workbench_story_easter_egg_copy.md",
    "captures/CAPTURE_BACK_WORKBENCH_STORY_EASTER_EGG_COPY.md",
    "cards/284_workbench_story_easter_egg_copy_card.md",
    "captures/CAPTURE_BACK_EASTER_EGG_HUMAN_EDITOR_COPY_REFRESH.md",
    "captures/CAPTURE_BACK_EASTER_EGG_BEAROCRAT_TAB_THESIS.md",
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
    makefile = read("Makefile")
    runtime = workflow + "\n" + index

    require("data-workflow-panel-open" in index, "Workflow panel open control must exist.", errors)
    require("data-workflow-panel" in index, "Workflow panel backdrop must exist.", errors)
    require("setupBracketeeringWorkflowPanel(root);" in app, "App must wire workflow panel setup.", errors)
    require("role=\"tablist\"" in workflow and "role=\"tab\"" in workflow and "role=\"tabpanel\"" in workflow, "Workflow panel must use accessible tab roles.", errors)
    require("ArrowLeft" in workflow and "ArrowRight" in workflow and "Home" in workflow and "End" in workflow, "Workflow tabs must support keyboard navigation.", errors)
    require("workflow-panel-tabs" in css, "Workflow tab styling must exist.", errors)
    require("workflow-panel-tabpanel[hidden]" in css, "Hidden tab panel styling must exist.", errors)

    for token in REQUIRED_RUNTIME_TOKENS:
        require(token in runtime, f"Runtime missing protected copy: {token}", errors)

    for rel in REQUIRED_SUPPORTING_ARTIFACTS:
        require((ROOT / rel).exists(), f"Missing supporting Easter egg artifact: {rel}", errors)

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

    print("OK: Workbench Easter egg panel has Story/Workbench/C64/Personal Bearocrat tabs and protected human-editor copy.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
