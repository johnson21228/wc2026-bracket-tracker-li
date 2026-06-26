#!/usr/bin/env python3
"""Verify player-visible R32 is forced to mirror Supabase Admin_/official."""
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
app = read("site/js/app.js")
repo = read("site/js/services/BracketRepository.js")
user_model = read("site/js/model/UserBracketModel.js")

require("createSupabaseBracketStore" in app, "App must import/create a Supabase bracket store for official truth.")
require("officialBracketStore" in app and "createBracketModel({\n    officialBracketStore" in app, "Main player board model must receive the officialBracketStore.")
require("function selectedTeam(slotId)" in model and "if (isR32DisplaySlot(slotId)) return officialTeam(slotId);" in model, "R32 display must be projected from Admin_/official, not player picks.")
require("stripR32OccupantsFromPlayerPicks" in model and "picks = stripR32OccupantsFromPlayerPicks(picks);" in model, "Loaded player/local R32 occupant values must be stripped before render/save.")
require("R32 occupants are supplied by Admin_/official and cannot be edited by players" in model, "setPick must reject player edits to R32 occupant slots.")
require("if (officialBracketStore && !adminOfficialR32EditorActive) return [];" in model and "Normal players never get R32 choices" in model, "Public player runtime must not generate R32 fallback choices from group data outside Admin_/official editor mode.")
require("failClosedAdminOfficialR32TruthDocument" in model and "Admin_/official R32 truth missing; failing closed" in model, "Main board must fail closed when Admin_/official is missing or unreadable.")
require("playerVisibleR32MatchesAdminOfficial" in model and "adminOfficialR32FailClosed" in model, "Model summary must expose Admin R32 mirror/fail-closed status.")
require("officialR32UnsetSlotRecord" in user_model and "mirrorsAdminOfficialExactly: true" in user_model and "officialUnset: true" in user_model, "R32 hydration must overwrite stale player slots and preserve partial Admin truth exactly.")
require("return failClosedOfficialR32Source(\"load-error\")" in repo and "return failClosedOfficialR32Source(\"missing-admin-official-row\")" in repo, "Repository must fail closed for Supabase Admin_/official failures instead of static fallback.")
require("return staticOfficialR32Fallback(modelBundle);" in repo, "Static fallback may remain only for non-Supabase/local repository paths.")

for rel in [
    "docs/features/force_player_r32_matches_admin_official.md",
    "captures/CAPTURE_BACK_FORCE_PLAYER_R32_MATCHES_ADMIN_OFFICIAL.md",
    "cards/1016_force_player_r32_matches_admin_official_card.md",
]:
    text = read(rel)
    require("playerVisibleR32 = Admin_/official R32 truth" in text, f"{rel} must capture the exact invariant.")
    require("R32 picks/occupants are not player picks" in text, f"{rel} must block player-R32 vocabulary slop.")

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
if (player.picksBySlot["L-R32-01"].pick.teamId !== "GER") throw new Error("Admin one-pick R32 did not hydrate exactly.");
if (player.picksBySlot["L-R32-02"].pick !== null) throw new Error("Missing Admin R32 slot was filled instead of staying unset.");

player = {
  ...player,
  picksBySlot: {
    ...player.picksBySlot,
    "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("BRA"), source: "user" },
    "L-R32-02": { slotId: "L-R32-02", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("USA"), source: "localStorage" },
  },
};
const rehydrated = hydrateOfficialR32Occupants({ bracket: player, bracketSlots, teamsById, officialR32: adminOfficial });
if (rehydrated.picksBySlot["L-R32-01"].pick.teamId !== "GER") throw new Error("Stale player R32 overrode Admin truth.");
if (rehydrated.picksBySlot["L-R32-02"].pick !== null) throw new Error("Stale local/static R32 survived where Admin has no value.");
if (!rehydrated.officialR32Hydration.mirrorsAdminOfficialExactly) throw new Error("Hydration is not tagged as exact Admin mirror.");

const blocked = setBracketPick({ bracket: rehydrated, sitePickId: "L-R32-01", pickValue: teamPickValue("BRA") });
if (blocked.picksBySlot["L-R32-01"].pick.teamId !== "GER") throw new Error("Player setPick changed an Admin-owned R32 slot.");
const later = setBracketPick({ bracket: rehydrated, sitePickId: "L-R16-01", pickValue: teamPickValue("GER") });
if (later.picksBySlot["L-R16-01"].pick.teamId !== "GER") throw new Error("Later player winner pick was blocked unexpectedly.");
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
        errors.append("Runtime Admin mirror test failed:\n" + result.stderr + result.stdout)

if errors:
    print("WC2026 player R32 Admin mirror verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player-visible R32 is forced to mirror Supabase Admin_/official; stale player/local/static R32 cannot masquerade as truth.")
