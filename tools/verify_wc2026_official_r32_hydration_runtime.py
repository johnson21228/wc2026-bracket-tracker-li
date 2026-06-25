#!/usr/bin/env python3
"""Verify official R32 hydration runtime/model boundary."""
from pathlib import Path
import subprocess
import textwrap

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "site/js/model/UserBracketModel.js": [
        "function hydrateOfficialR32Occupants",
        "function officialR32OccupantsBySlot",
        "source: \"Admin_/official\"",
        "authority: \"Admin_/official\"",
        "playerAuthored: false",
        "blockedPlayerR32Authoring: true",
        "isR32EntrantSlot(existingRecord)",
    ],
    "site/js/services/StaticJsonModelSource.js": [
        "officialRoundOf32Path = \"data/official_round_of_32.json\"",
        "async loadOfficialRoundOf32()",
        "officialRoundOf32",
    ],
    "site/js/services/BracketRepository.js": [
        "hydrateOfficialR32Occupants",
        "async loadOfficialR32Source",
        "officialR32,",
        "async saveUserBracket(bracket)",
    ],
    "site/js/mvc/model.js": [
        "hydrateOfficialR32Occupants",
        "officialR32: officialBracketDocument",
        "record?.kind === \"entrant\" || record?.round === \"R32_ENTRANT\"",
    ],
    "docs/features/official_r32_hydration.md": [
        "Runtime implementation",
        "creation, load, import, and save boundaries",
        "Runtime does not change player-facing copy",
        "Runtime does not remove Game 1/Game 2 labels",
    ],
    "cards/1012_official_r32_hydration_runtime_card.md": [
        "Admin_/official is the authority for R32 occupants",
        "Hydration happens at creation, load, import, and save boundaries",
        "Existing player knockout winner picks are preserved",
        "Runtime does not change player-facing copy",
    ],
    "captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RUNTIME.md": [
        "Runtime/model only",
        "BracketDocument remains the persistence container",
        "Supabase row-per-user-per-game remains valid",
        "No UI copy cleanup",
    ],
}

errors = []
for rel, needles in REQUIRED.items():
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            errors.append(f"{rel}: missing phrase {needle!r}")

makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
if "python3 tools/verify_wc2026_official_r32_hydration_runtime.py" not in makefile:
    errors.append("Makefile verify target does not include official R32 hydration runtime verifier")

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
    { slotId: "L-R16-01", sitePickId: "L-R16-01", kind: "winner", round: "R32_WINNER" },
  ],
};
const teamsById = { USA: { id: "USA" }, BRA: { id: "BRA" }, FRA: { id: "FRA" } };
const officialR32 = { slots: [{ slotId: "L-R32-01", teamId: "USA" }] };

let bracket = createEmptyBracketDocument({
  userId: "player-1",
  bracketSlots,
  teamsById,
  officialR32,
});

if (bracket.picksBySlot["L-R32-01"].pick.teamId !== "USA") throw new Error("creation did not hydrate official R32 occupant");
if (bracket.picksBySlot["L-R32-01"].source !== "Admin_/official") throw new Error("hydrated R32 source is not official");
if (bracket.picksBySlot["L-R32-01"].playerAuthored !== false) throw new Error("hydrated R32 occupant is not marked non-player-authored");

bracket = setBracketPick({ bracket, sitePickId: "L-R32-01", pickValue: teamPickValue("BRA") });
if (bracket.picksBySlot["L-R32-01"].pick.teamId !== "USA") throw new Error("player authored over official R32 occupant");
if (!bracket.officialR32Hydration?.blockedPlayerR32Authoring) throw new Error("R32 authoring block was not recorded");

bracket = setBracketPick({ bracket, sitePickId: "L-R16-01", pickValue: teamPickValue("USA") });
if (bracket.picksBySlot["L-R16-01"].pick.teamId !== "USA") throw new Error("R32 match winner pick was not preserved as player-authored");
if (bracket.picksBySlot["L-R16-01"].source !== "user") throw new Error("winner pick is not player-owned");

const loaded = hydrateOfficialR32Occupants({
  bracket: {
    ...bracket,
    picksBySlot: {
      ...bracket.picksBySlot,
      "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("BRA"), source: "user" },
    },
  },
  bracketSlots,
  teamsById,
  officialR32,
});
if (loaded.picksBySlot["L-R32-01"].pick.teamId !== "USA") throw new Error("load/import/save hydration did not restore official R32 occupant");
if (loaded.picksBySlot["L-R16-01"].pick.teamId !== "USA") throw new Error("load/import/save hydration did not preserve knockout winner pick");
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
        errors.append("runtime hydration behavior test failed:\n" + result.stderr + result.stdout)

if errors:
    print("WC2026 official R32 hydration runtime verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 official R32 hydration runtime keeps R32 occupants official, preserves player knockout winner picks, and wires creation/load/import/save boundaries without UI cleanup.")
