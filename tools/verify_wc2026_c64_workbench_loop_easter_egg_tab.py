#!/usr/bin/env python3
from pathlib import Path

def read(path):
    return Path(path).read_text()

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    js = read("site/js/workflow/BracketeeringWorkflowPanel.js")
    css = read("site/css/app.css")
    image = Path("site/assets/workflow/c64_workbench_stage0_learning_loop.jpeg")

    require('label: "Story"' in js, "Story tab must remain.", errors)
    require('label: "Workbench"' in js, "Workbench tab must remain.", errors)
    require('label: "C64 Loop"' in js, "C64 Loop tab must be present.", errors)
    require('label: "Personal Bearocrat"' in js, "Personal Bearocrat tab must be present.", errors)
    require('data-workflow-tabpanel="c64-loop"' in js, "C64 Loop tabpanel must be present.", errors)

    require("C64_WORKBENCH_LOOP_IMAGE_SRC" in js, "C64 Loop image source constant must exist.", errors)
    require("c64_workbench_stage0_learning_loop.jpeg" in js, "C64 Loop image path must be referenced.", errors)
    require("The C64 Workbench Loop" in js, "C64 Loop title copy must be present.", errors)
    require("The C64 is not the point. It is just a tiny world where the rules are visible." in js, "C64 compact metaphor copy must be present.", errors)

    for token in [
        "Conversation",
        "repo change",
        "verification",
        "C64 build",
        "emulator evidence",
        "Capture Back",
        "next lab",
    ]:
        require(token in js, f"C64 loop copy must include: {token}", errors)

    require(image.exists(), "C64 Workbench loop image asset must exist.", errors)
    require(image.stat().st_size > 10000, "C64 Workbench loop image asset must not be empty.", errors)
    require(".workflow-panel-figure img" in css, "C64 Loop image CSS must be present.", errors)

    for path in [
        "cards/289_c64_workbench_loop_easter_egg_tab_card.md",
        "captures/CAPTURE_BACK_C64_WORKBENCH_LOOP_EASTER_EGG_TAB.md",
        "docs/features/c64_workbench_loop_easter_egg_tab.md",
        "li/world_cup/c64_workbench_loop_easter_egg_tab_rule.md",
    ]:
        require(Path(path).exists(), f"Missing capture/card/doc/rule artifact: {path}", errors)

    if errors:
        print("WC2026 C64 Workbench Loop Easter egg tab verification failed: " + "; ".join(errors))
        return 1

    print("OK: Workbench Easter egg panel includes C64 Loop image tab and explanatory copy.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
