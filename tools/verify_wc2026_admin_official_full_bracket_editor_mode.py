#!/usr/bin/env python3
"""Verify Admin_/official can edit full official bracket truth while players stay separated."""
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
makefile = read("Makefile")

require('urlParams.get("adminOfficialEditor") === "1"' in app, "App must expose explicit adminOfficialEditor query-gated mode.")
require("adminOfficialEditor," in app and "adminOfficialR32Editor," in app, "App must pass full and R32 Admin editor flags into createBracketModel.")
require("adminOfficialEditor = adminOfficialR32Editor" in model, "Model must derive full Admin editor mode from the existing admin official gate by default.")
require("adminOfficialEditorActive" in model and "saveAdminOfficialBracketTruth" in model, "Full Admin editor mode must require a Supabase official truth save boundary.")
require("function pickRecordForAdminOfficialSlot" in model and "officialTruth: true" in model, "Admin full editor saves must mark later picks as official truth.")
require("function buildAdminOfficialBracketDocument" in model and "admin-official-full-bracket-editor-mode" in model, "Admin full edits must build an official BracketDocument.")
require("function persistAdminOfficialTruth" in model and "officialBracketStore.saveAdminOfficialBracketTruth" in model, "Admin full edits must save through the official Supabase truth method.")
require("if (adminOfficialEditorActive) return officialTeam(slotId);" in model, "Admin full editor display must read later picks from officialPicks, not player picks.")
require("if (adminOfficialEditorActive)" in model and "adminOfficialTruthEdited: true" in model, "setPick must route Admin full edits to official truth.")
require("R32 occupants are supplied by Admin_/official and cannot be edited by players" in model, "Normal player setPick must still reject R32 edits.")
require("picks = stripR32OccupantsFromPlayerPicks(picks);" in model, "Normal player loaded picks must still strip R32 occupants.")
require("remoteSavePromise" in model and "bracketStore.saveUserBracket" in model, "Normal player save path must remain the player bracket store.")
require("async saveAdminOfficialBracketTruth" in store, "SupabaseBracketStore must expose a full official truth save method.")
require("saveOfficialR32BracketAuthority" in store and "saveAdminOfficialBracketTruth" in store, "Full editor must preserve the existing R32 official save method.")
require("user_id: ADMIN_OFFICIAL_USER_ID" in store and "bracket_kind: \"official\"" in store, "Official truth save must upsert the Admin_/official official row.")
require("SupabaseBracketStore can only save the signed-in user's bracket" in store, "Normal player save must remain isolated from Admin_/official writes.")
require("officialEdit ? \"Admin_/official\"" in user_model and "record.officialTruth = true" in user_model, "Document helper must mark official bracket edits as Admin_/official truth.")
require("if (isR32EntrantSlot(existingRecord) && bracket?.bracketKind !== \"official\")" in user_model, "Document helper must keep blocking non-official R32 authoring.")
require("verify_wc2026_admin_official_full_bracket_editor_mode.py" in makefile, "Makefile must run the Admin official full bracket editor verifier.")

for rel in [
    "docs/features/admin_official_full_bracket_editor_mode.md",
    "captures/CAPTURE_BACK_ADMIN_OFFICIAL_FULL_BRACKET_EDITOR_MODE.md",
    "cards/1018_admin_official_full_bracket_editor_mode_card.md",
    "li/world_cup/admin_official_full_bracket_editor_mode_rule.md",
]:
    text = read(rel)
    require("Admin_/official" in text and "official bracket truth" in text, f"{rel} must state Admin official truth ownership.")
    require("Normal players" in text and "R16++" in text, f"{rel} must preserve normal player R16++ ownership.")

runtime_test = r'''
import {
  createEmptyBracketDocument,
  hydrateOfficialR32Occupants,
  setBracketPick,
} from "./site/js/model/UserBracketModel.js";
import { teamPickValue } from "./site/js/model/PickValue.js";

const bracketSlots = {
  canonicalPickSlots: [
    { slotId: "L-R32-01", sitePickId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT" },
    { slotId: "L-R32-02", sitePickId: "L-R32-02", kind: "entrant", round: "R32_ENTRANT" },
    { slotId: "L-R16-01", sitePickId: "L-R16-01", kind: "winner", round: "R32_WINNER" },
    { slotId: "L-QF-01", sitePickId: "L-QF-01", kind: "winner", round: "R16_WINNER" },
    { slotId: "CHAMPION", sitePickId: "CHAMPION", kind: "winner", round: "CHAMPION" },
  ],
};
const teamsById = { GER: { id: "GER" }, BRA: { id: "BRA" }, USA: { id: "USA" } };
const adminOfficial = {
  userId: "Admin_/official",
  bracketKind: "official",
  officialR32AuthoritySource: "Supabase:Admin_/official",
  picksBySlot: {
    "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("GER"), source: "Admin_/official" },
  },
};

let player = createEmptyBracketDocument({ userId: "player", bracketSlots, teamsById, officialR32: adminOfficial });
const blockedR32 = setBracketPick({ bracket: player, sitePickId: "L-R32-01", pickValue: teamPickValue("BRA") });
if (blockedR32.picksBySlot["L-R32-01"].pick.teamId !== "GER") throw new Error("Normal player changed R32 occupant.");
const playerLater = setBracketPick({ bracket: player, sitePickId: "L-R16-01", pickValue: teamPickValue("GER") });
if (playerLater.picksBySlot["L-R16-01"].pick.teamId !== "GER") throw new Error("Normal player R16++ pick was blocked.");
if (playerLater.picksBySlot["L-R16-01"].source !== "user") throw new Error("Normal player later pick did not stay player-owned.");

let official = createEmptyBracketDocument({ userId: "Admin_/official", bracketSlots, teamsById });
official = { ...official, userId: "Admin_/official", bracketKind: "official" };
official = setBracketPick({ bracket: official, sitePickId: "L-R32-01", pickValue: teamPickValue("BRA") });
official = setBracketPick({ bracket: official, sitePickId: "L-R16-01", pickValue: teamPickValue("BRA") });
official = setBracketPick({ bracket: official, sitePickId: "L-QF-01", pickValue: teamPickValue("BRA") });
official = setBracketPick({ bracket: official, sitePickId: "CHAMPION", pickValue: teamPickValue("BRA") });
for (const slotId of ["L-R32-01", "L-R16-01", "L-QF-01", "CHAMPION"]) {
  const record = official.picksBySlot[slotId];
  if (record.pick.teamId !== "BRA") throw new Error(`Official did not edit ${slotId}.`);
  if (record.source !== "Admin_/official") throw new Error(`Official edit for ${slotId} was not marked Admin_/official.`);
  if (!record.officialTruth) throw new Error(`Official edit for ${slotId} was not marked official truth.`);
}

const rehydrated = hydrateOfficialR32Occupants({ bracket: playerLater, bracketSlots, teamsById, officialR32: official });
if (rehydrated.picksBySlot["L-R32-01"].pick.teamId !== "BRA") throw new Error("Player did not mirror edited Admin R32 value.");
if (rehydrated.picksBySlot["L-R16-01"].pick.teamId !== "GER") throw new Error("Player later pick was overwritten by Admin later truth.");
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
        errors.append("Runtime Admin full editor test failed:\n" + result.stderr + result.stdout)

if errors:
    print("WC2026 Admin_/official full bracket editor mode verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Admin_/official can edit full official bracket truth while normal players keep player-only ownership.")
