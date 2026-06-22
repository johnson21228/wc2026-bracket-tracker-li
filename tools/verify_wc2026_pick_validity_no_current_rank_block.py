from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def text(path):
    return (ROOT / path).read_text()


def require(path, token):
    data = text(path)
    if token not in data:
        raise SystemExit(f"Missing token in {path}: {token}")


def forbid(path, token):
    data = text(path)
    if token in data:
        raise SystemExit(f"Forbidden current-rank conflict token remains in {path}: {token}")


model = "site/js/mvc/model.js"

# The current standings rank should no longer be used as an invalid-pick warning.
forbid(model, "function expectedRankForR32Logic")
forbid(model, "this slot expects the Group")
forbid(model, "Number(entry.rank) !== expectation.rank")
forbid(model, "expectedRankForR32Logic(logic)")

# Source scope and structural duplicate conflict are still part of validity.
require(model, "not one of the current feeder teams for this winner slot")
require(model, "already assigned to another Round of 32 slot")
require(model, "pickValidityForSlot")

require("li/world_cup/pick_validity_no_current_rank_block_rule.md", "Current group rank")
require("li/world_cup/pick_validity_no_current_rank_block_rule.md", "must not be used as an invalid-pick warning by itself")
require("docs/features/pick_validity_no_current_rank_block.md", "source-scope boundary remains intact")
require("cards/208_remove_current_rank_pick_conflict_card.md", "Card 208")
require("capture_back/CAPTURE_BACK_PICK_VALIDITY_NO_CURRENT_RANK_BLOCK.md", "current group standings rank is context")
require("Makefile", "tools/verify_wc2026_pick_validity_no_current_rank_block.py")

print("OK: pick validity no longer warns solely from current group rank.")
