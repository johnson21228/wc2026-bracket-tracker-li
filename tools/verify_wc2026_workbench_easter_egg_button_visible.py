#!/usr/bin/env python3
from pathlib import Path
import re

def read(path):
    return Path(path).read_text()

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    index = read("site/index.html")
    app = read("site/js/app.js")
    panel = read("site/js/workflow/BracketeeringWorkflowPanel.js")

    button_tags = re.findall(r"<button[^>]*>", index)
    workflow_buttons = [
        tag for tag in button_tags
        if "workflow-floating-button" in tag and "data-workflow-panel-open" in tag
    ]

    require(workflow_buttons, "Expected visible Workbench/Easter egg open button markup.", errors)

    if workflow_buttons:
        tag = workflow_buttons[0]
        require("hidden" not in tag, "Workbench/Easter egg open button must not be hidden.", errors)
        require('aria-hidden="true"' not in tag, "Visible Workbench/Easter egg button must not be aria-hidden.", errors)
        require('tabindex="-1"' not in tag, "Visible Workbench/Easter egg button must remain keyboard reachable.", errors)

    require("setupBracketeeringWorkflowPanel" in app, "Workbench panel setup must remain wired.", errors)
    require("data-workflow-panel-body" in index, "Workbench panel markup must remain present.", errors)
    require("Workbench" in panel, "Workbench panel copy must remain available.", errors)

    for path in [
        "cards/288_unhide_workbench_easter_egg_button_card.md",
        "captures/CAPTURE_BACK_UNHIDE_WORKBENCH_EASTER_EGG_BUTTON.md",
        "docs/features/unhide_workbench_easter_egg_button.md",
        "li/world_cup/unhide_workbench_easter_egg_button_rule.md",
    ]:
        require(Path(path).exists(), f"Missing capture/card/doc/rule artifact: {path}", errors)

    if errors:
        print("WC2026 Workbench Easter egg visible-button verification failed: " + "; ".join(errors))
        return 1

    print("OK: Workbench/Easter egg floating button is visible and panel remains wired.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
