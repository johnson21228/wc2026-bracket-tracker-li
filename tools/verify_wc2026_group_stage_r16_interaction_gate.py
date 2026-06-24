#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    capture = read("captures/CAPTURE_BACK_GROUP_STAGE_R16_INTERACTION_GATE.md")
    card = read("cards/1009_group_stage_r16_interaction_gate_card.md")
    doc = read("docs/features/group_stage_r16_interaction_gate.md")
    rule = read("li/world_cup/group_stage_r16_interaction_gate_rule.md")

    view = read("site/js/mvc/view.js")
    controller = read("site/js/mvc/controller.js")

    require("R16+ pick-menu interaction" in capture,
            "Capture must name the R16+ pick-menu interaction defect.", errors)
    require("Gate R16+ Pick Interaction During Group Stage" in card,
            "Card must capture the implementation target.", errors)
    require("pickable cursor, and pick-menu invocation" in doc,
            "Feature doc must state visual plus interaction suppression.", errors)
    require("controller backstop blocks R16+ slot menu invocation during Group Stage" in rule,
            "LI rule must require controller backstop.", errors)

    require("shouldSuppressPickFillForSlot" in view,
            "Existing Group Stage visual suppression gate must remain present.", errors)
    require("slotAllowedForActiveGame" in controller,
            "Controller active-game slot gate must remain present for the implementation backstop.", errors)

    if errors:
        print("Group Stage R16+ interaction gate capture verification failed: " + "; ".join(errors))
        return 1

    print("OK: Group Stage R16+ interaction gate defect is captured with visual, interaction, and controller-backstop requirements.")

if __name__ == "__main__":
    raise SystemExit(main())
