#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []
    required = [
        "cards/228_add_bracketdocument_save_seam_before_supabase_card.md",
        "docs/architecture/bracketeering_bracketdocument_save_seam.md",
        "li/world_cup/bracketdocument_save_seam_before_supabase_rule.md",
        "tools/verify_wc2026_bracketdocument_save_seam_before_supabase.py",
        "site/js/controllers/Game1R32PickController.js",
        "site/js/services/BracketRepository.js",
        "site/js/services/LocalStorageBracketStore.js",
        "site/js/model/UserBracketModel.js",
        "Makefile",
    ]
    for rel in required:
        require((ROOT / rel).exists(), f"missing required file: {rel}", errors)
    if errors:
        for error in errors: print(error)
        raise SystemExit(1)
    controller = read("site/js/controllers/Game1R32PickController.js")
    repository = read("site/js/services/BracketRepository.js")
    local_store = read("site/js/services/LocalStorageBracketStore.js")
    model = read("site/js/model/UserBracketModel.js")
    docs = "\n".join([
        read("docs/architecture/bracketeering_bracketdocument_save_seam.md"),
        read("docs/architecture/bracketeering_canonical_bracket_document_runtime.md"),
        read("docs/architecture/bracketeering_model_persistence_contract.md"),
        read("li/world_cup/bracketdocument_save_seam_before_supabase_rule.md"),
        read("li/world_cup/canonical_bracket_document_runtime_rule.md"),
    ])
    makefile = read("Makefile")
    require("verify_wc2026_bracketdocument_save_seam_before_supabase.py" in makefile, "Makefile does not wire the BracketDocument save seam verifier", errors)
    require("saveUserBracket(bracket)" in repository and "this.bracketStore.saveUserBracket(bracket)" in repository, "BracketRepository must expose saveUserBracket and delegate to the configured store", errors)
    require("normalizeBracketDocument" in local_store, "LocalStorageBracketStore must normalize before saving canonical BracketDocument", errors)
    for token in ["schemaVersion", "gameId", "status", "expectedPickCount", "updatedAt", "picksBySlot"]:
        require(token in local_store or token in model, f"canonical BracketDocument token missing from local save/model path: {token}", errors)
    require("createStaticBracketRepository" in controller, "Game1R32PickController must use/create BracketRepository for save seam", errors)
    require("setBracketPick" in controller, "Game1R32PickController must update canonical BracketDocument with setBracketPick", errors)
    require("saveBracketDocumentFromProjectionPicks" in controller, "Game1R32PickController must expose saveBracketDocumentFromProjectionPicks", errors)
    require("this.bracketRepository" in controller and ".saveUserBracket(nextBracket)" in controller, "Game1R32PickController must save canonical BracketDocument through BracketRepository", errors)
    require("this.writePicks(picks)" in controller, "legacy projection pick write should remain during transition to preserve rendering behavior", errors)
    require("createEmptyBracketDocument" in model and "normalizeBracketDocument" in model and "picksBySlot" in model, "UserBracketModel must create/normalize canonical BracketDocument with picksBySlot", errors)
    require("legacyPicksFromPicksBySlot" in model, "UserBracketModel must keep transitional legacy rendering compatibility from picksBySlot", errors)
    site_js = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in (ROOT / "site/js").rglob("*.js"))
    require("supabase" not in site_js.lower(), "site/js must not introduce Supabase client calls in this pre-Supabase save seam card", errors)
    for phrase in ["Same BracketDocument. Different store.", "LocalStorageBracketStore", "SupabaseBracketStore", "user_brackets.picks_json"]:
        require(phrase in docs, f"docs/LI missing save-seam phrase: {phrase}", errors)
    if errors:
        for error in errors: print(error)
        raise SystemExit(1)
    print("OK: WC2026 BracketDocument save seam is in place before Supabase implementation.")

if __name__ == "__main__":
    main()
