#!/usr/bin/env python3
"""Verify Admin_/official can author R32 while normal players only mirror it."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def require(condition, message):
    if not condition:
        errors.append(message)

app = read("site/js/app.js")
model = read("site/js/mvc/model.js")
store = read("site/js/services/SupabaseBracketStore.js")
user_model = read("site/js/model/UserBracketModel.js")

require('urlParams.get("adminOfficialR32Editor") === "1"' in app, "App must expose explicit adminOfficialR32Editor query-gated mode.")
require("adminOfficialR32Editor," in app and "officialBracketStore," in app, "App must pass Admin editor mode and the official store into createBracketModel.")
require("adminOfficialR32Editor = false" in model, "Model must default Admin_/official R32 editor mode off.")
require("adminOfficialR32EditorActive" in model and "saveOfficialR32BracketAuthority" in model, "Admin editor mode must require an official Supabase save boundary.")
require("function pickRecordForOfficialR32Slot" in model and "round: \"R32_ENTRANT\"" in model, "Admin R32 saves must write R32 entrant records.")
require("function buildAdminOfficialR32BracketDocument" in model and "bracketKind: \"official\"" in model, "Admin R32 edits must build an official BracketDocument.")
require("function persistAdminOfficialR32" in model and "officialBracketStore.saveOfficialR32BracketAuthority" in model, "Admin R32 edits must save to the official Supabase row.")
require("if (officialBracketStore && !adminOfficialR32EditorActive) return [];" in model, "Normal players must receive no R32 choices in public Supabase runtime.")
require("if (!adminOfficialR32EditorActive)" in model and "cannot be edited by players" in model, "Normal player setPick must still reject R32 edits.")
require("adminOfficialR32Edited: true" in model, "Admin R32 setPick must return an edit marker.")
require("r32EditableByAdminOfficial" in model and "r32ReadOnlyForPlayer" in model, "Slot view models must distinguish Admin editable R32 from player read-only R32.")
require("async saveOfficialR32BracketAuthority" in store, "SupabaseBracketStore must expose an official R32 save method.")
require("user_id: ADMIN_OFFICIAL_USER_ID" in store and "bracket_kind: \"official\"" in store, "Official R32 save must upsert the Admin_/official official row.")
require("await this.requireSignedInUser()" in store, "Official R32 save must require a signed-in Supabase session before attempting RLS-protected write.")
require("if (isR32EntrantSlot(existingRecord) && bracket?.bracketKind !== \"official\")" in user_model, "Document helper must keep blocking non-official R32 authoring.")

for rel in [
    "docs/features/admin_official_r32_editor_mode.md",
    "captures/CAPTURE_BACK_ADMIN_OFFICIAL_R32_EDITOR_MODE.md",
    "cards/1017_admin_official_r32_editor_mode_card.md",
    "li/world_cup/admin_official_r32_editor_mode_rule.md",
]:
    text = read(rel)
    require("Only Admin_/official may edit R32 occupant slots" in text, f"{rel} must state the edit authority invariant.")
    require("All players mirror Admin_/official R32 occupant truth" in text, f"{rel} must preserve the mirror invariant.")

runtime_test = r'''
import {
  createEmptyBracketDocument,
  setBracketPick,
} from "./site/js/model/UserBracketModel.js";
import { teamPickValue } from "./site/js/model/PickValue.js";

const bracketSlots = {
  canonicalPickSlots: [
    { slotId: "L-R32-01", sitePickId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT" },
    { slotId: "L-R16-01", sitePickId: "L-R16-01", kind: "winner", round: "R32_WINNER" },
  ],
};
const teamsById = { GER: { id: "GER" }, BRA: { id: "BRA" } };
let player = createEmptyBracketDocument({ userId: "player", bracketSlots, teamsById, officialR32: {
  userId: "Admin_/official",
  bracketKind: "official",
  officialR32AuthoritySource: "Supabase:Admin_/official",
  picksBySlot: {
    "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("GER"), source: "Admin_/official" },
  },
}});
const blocked = setBracketPick({ bracket: player, sitePickId: "L-R32-01", pickValue: teamPickValue("BRA") });
if (blocked.picksBySlot["L-R32-01"].pick.teamId !== "GER") throw new Error("Non-admin player changed R32 occupant.");
let official = { ...player, bracketKind: "official" };
official = setBracketPick({ bracket: official, sitePickId: "L-R32-01", pickValue: teamPickValue("BRA") });
if (official.picksBySlot["L-R32-01"].pick.teamId !== "BRA") throw new Error("Official bracket helper could not edit R32 occupant.");
'''

if not errors:
    result = subprocess.run(
        ["node", "--input-type=module", "-e", runtime_test],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        errors.append("Runtime Admin editor test failed:\n" + result.stderr + result.stdout)

if errors:
    print("WC2026 Admin_/official R32 editor mode verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Admin_/official can edit R32 truth while normal players mirror R32 read-only.")
