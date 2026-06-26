#!/usr/bin/env python3
"""Verify only Supabase Admin_/official R32 is materialized into player picks."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def require(condition, message):
    if not condition:
        errors.append(message)

model = read("site/js/mvc/model.js")
user_model = read("site/js/model/UserBracketModel.js")
makefile = read("Makefile")

require("function hydrateOnlySupabaseAdminR32IntoPlayerPicks" in model, "MVC model must have an explicit hydrate-only-Supabase-Admin-R32 helper.")
require("const playerOwnedPicks = stripR32OccupantsFromPlayerPicks(sourcePicks);" in model, "Hydration helper must strip stale player/local R32 before any copy.")
require("officialR32: officialBracketDocument" in model, "Hydration helper must use the loaded Admin_/official Supabase document.")
require("picks = hydrateOnlySupabaseAdminR32IntoPlayerPicks(picks);" in model, "Loaded player picks must be hydrated with only Supabase Admin R32.")
require("return getTeam(picks[slotId]);" in model, "Normal rendering/preselection must read from hydrated player picks.")
require("if (adminOfficialEditorActive) return officialTeam(slotId);" in model, "Admin full editor must still render official truth from officialPicks.")
require("if (adminOfficialR32EditorActive && isR32DisplaySlot(slotId)) return officialTeam(slotId);" in model, "Admin R32 editor must still render R32 official truth from officialPicks.")
require("R32 occupants are supplied by Admin_/official and cannot be edited by players" in model, "Normal player R32 edits must still be rejected.")
require("source === \"Supabase:Admin_/official\"" in user_model, "R32 hydration must be gated to Supabase Admin_/official source.")
require("return \"StaticJsonFallback:official_round_of_32\"" not in user_model, "R32 hydration must not fall back to static JSON as copy source.")
require("source === \"StaticJsonFallback:official_round_of_32\"" not in user_model, "Static JSON must not satisfy the R32 hydration gate.")
require("if (record?.round === \"R32_ENTRANT\" || record?.kind === \"entrant\") addRecord(slotId, record);" in user_model, "Only R32 entrant records may be extracted from Admin truth for player hydration.")
require("verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py" in makefile, "Makefile must run this hydration compatibility verifier.")

for rel in [
    "docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md",
    "captures/CAPTURE_BACK_HYDRATE_ONLY_SUPABASE_ADMIN_R32_INTO_PLAYER_PICKS.md",
    "cards/1019_hydrate_only_supabase_admin_r32_into_player_picks_card.md",
    "li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md",
]:
    text = read(rel)
    require("Copy ONLY R32" in text, f"{rel} must state the only-R32 copy rule.")
    require("Supabase Admin_/official" in text, f"{rel} must state the Supabase Admin source rule.")
    require("R16++" in text, f"{rel} must preserve player R16++ ownership.")

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
const teamsById = {
  GER: { id: "GER" }, BRA: { id: "BRA" }, USA: { id: "USA" }, JPN: { id: "JPN" }, MEX: { id: "MEX" }
};
const supabaseAdmin = {
  userId: "Admin_/official",
  bracketKind: "official",
  officialR32AuthoritySource: "Supabase:Admin_/official",
  picksBySlot: {
    "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("GER"), source: "Admin_/official" },
    "L-R32-02": { slotId: "L-R32-02", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("JPN"), source: "Admin_/official" },
    "L-R16-01": { slotId: "L-R16-01", kind: "winner", round: "R32_WINNER", pick: teamPickValue("BRA"), source: "Admin_/official" },
    "CHAMPION": { slotId: "CHAMPION", kind: "winner", round: "CHAMPION", pick: teamPickValue("BRA"), source: "Admin_/official" },
  },
};
let player = createEmptyBracketDocument({ userId: "player", bracketSlots, teamsById });
player = setBracketPick({ bracket: player, sitePickId: "L-R16-01", pickValue: teamPickValue("USA") });
player = {
  ...player,
  picksBySlot: {
    ...player.picksBySlot,
    "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("MEX"), source: "localStorage" },
  },
};
const hydrated = hydrateOfficialR32Occupants({ bracket: player, bracketSlots, teamsById, officialR32: supabaseAdmin });
if (hydrated.picksBySlot["L-R32-01"].pick.teamId !== "GER") throw new Error("Supabase Admin R32 did not overwrite stale player/local R32.");
if (hydrated.picksBySlot["L-R32-02"].pick.teamId !== "JPN") throw new Error("Supabase Admin R32 second feeder did not hydrate.");
if (hydrated.picksBySlot["L-R16-01"].pick.teamId !== "USA") throw new Error("Admin R16++ was copied over player R16++.");
if (hydrated.picksBySlot["CHAMPION"].pick !== null) throw new Error("Admin Champion was copied into player bracket.");
if (hydrated.picksBySlot["L-R32-01"].playerAuthored !== false) throw new Error("Hydrated R32 is not marked non-player-authored.");
if (hydrated.picksBySlot["L-R32-01"].hydratedFrom !== "Supabase:Admin_/official") throw new Error("Hydrated R32 does not identify Supabase Admin source.");

const staticOfficial = {
  officialR32AuthoritySource: "StaticJsonFallback:official_round_of_32",
  picksBySlot: {
    "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("BRA") },
  },
};
const emptyLocal = createEmptyBracketDocument({ userId: "local", bracketSlots, teamsById, officialR32: staticOfficial });
if (emptyLocal.picksBySlot["L-R32-01"].pick !== null) throw new Error("Static JSON R32 was copied into a player bracket.");

const missingSupabase = {
  userId: "Admin_/official",
  bracketKind: "official",
  officialR32AuthoritySource: "Supabase:Admin_/official",
  failClosed: true,
  picksBySlot: {},
};
const failClosed = hydrateOfficialR32Occupants({ bracket: hydrated, bracketSlots, teamsById, officialR32: missingSupabase });
if (failClosed.picksBySlot["L-R32-01"].pick !== null) throw new Error("Missing Supabase Admin R32 did not fail closed to unset.");
if (!failClosed.picksBySlot["L-R32-01"].officialUnset) throw new Error("Missing Supabase Admin R32 was not marked officialUnset.");
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
        errors.append("Runtime Supabase-only R32 hydration test failed:\n" + result.stderr + result.stdout)

if errors:
    print("WC2026 Supabase-only Admin R32 hydration verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player picks hydrate only Supabase Admin_/official R32 while preserving player R16++ picks.")
