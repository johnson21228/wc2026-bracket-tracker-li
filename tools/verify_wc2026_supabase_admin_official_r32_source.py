#!/usr/bin/env python3
"""Verify Supabase Admin_/official is primary source for official R32 hydration."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "site/js/services/SupabaseBracketStore.js": [
        "const ADMIN_OFFICIAL_USER_ID = \"Admin_/official\"",
        "const ADMIN_OFFICIAL_AUTHORITY_SOURCE = \"Supabase:Admin_/official\"",
        "async loadOfficialR32BracketAuthority",
        ".eq(\"user_id\", ADMIN_OFFICIAL_USER_ID)",
        ".eq(\"tournament_id\", tournamentId)",
        ".eq(\"game_id\", gameId)",
        "officialR32AuthoritySource: ADMIN_OFFICIAL_AUTHORITY_SOURCE",
        "authority: \"Admin_/official\"",
    ],
    "site/js/services/BracketRepository.js": [
        "async loadOfficialR32Source",
        "this.bracketStore.loadOfficialR32BracketAuthority",
        "officialR32AuthoritySource: \"Supabase:Admin_/official\"",
        "StaticJsonFallback:official_round_of_32",
        "failing closed",
        "officialR32,",
    ],
    "site/js/services/StaticJsonModelSource.js": [
        "async loadOfficialRoundOf32Fallback()",
        "StaticJsonFallback:official_round_of_32",
        "fallbackOnly: true",
    ],
    "site/js/model/UserBracketModel.js": [
        "function officialR32AuthoritySource",
        "Supabase:Admin_/official",
        "source === \"Supabase:Admin_/official\"",
        "hydratedFrom: occupant.hydratedFrom || \"Supabase:Admin_/official\"",
        "blockedPlayerR32Authoring: true",
    ],
    "site/js/mvc/model.js": [
        "loadOfficialR32BracketAuthority",
        "officialR32AuthoritySource: \"Supabase:Admin_/official\"",
        "source: \"Supabase:Admin_/official\"",
        "record?.kind === \"entrant\" || record?.round === \"R32_ENTRANT\"",
    ],
    "docs/features/official_r32_hydration.md": [
        "Supabase Admin_/official source",
        "Supabase `Admin_/official` bracket row as the primary authority",
        "Static `site/data/official_round_of_32.json` is no longer the production authority",
        "StaticJsonFallback:official_round_of_32",
    ],
    "cards/1013_supabase_admin_official_r32_source_card.md": [
        "Supabase `Admin_/official` bracket row",
        "loadOfficialR32BracketAuthority",
        "StaticJsonFallback:official_round_of_32",
        "Existing player knockout winner picks remain player-owned and are preserved",
    ],
    "captures/CAPTURE_BACK_SUPABASE_ADMIN_OFFICIAL_R32_SOURCE.md": [
        "Supabase `Admin_/official` bracket row as the primary production authority",
        "BracketDocument remains the persistence container",
        "Supabase remains row-per-user-per-game",
        "No player-facing copy cleanup",
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

repo_text = (ROOT / "site/js/services/BracketRepository.js").read_text(encoding="utf-8")
method_index = repo_text.find("async loadOfficialR32Source")
supabase_index = repo_text.find("this.bracketStore.loadOfficialR32BracketAuthority", method_index)
static_index = repo_text.find("return staticOfficialR32Fallback(modelBundle)", method_index)
if method_index < 0 or supabase_index < 0 or static_index < 0 or supabase_index > static_index:
    errors.append("BracketRepository must try Supabase Admin_/official before static official_round_of_32 fallback")

makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
if "python3 tools/verify_wc2026_supabase_admin_official_r32_source.py" not in makefile:
    errors.append("Makefile verify target does not include Supabase Admin_/official R32 source verifier")

runtime_test = r'''
import {
  createEmptyBracketDocument,
  hydrateOfficialR32Occupants,
  officialR32AuthoritySource,
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
const supabaseOfficial = {
  userId: "Admin_/official",
  bracketKind: "official",
  officialR32AuthoritySource: "Supabase:Admin_/official",
  picksBySlot: {
    "L-R32-01": { slotId: "L-R32-01", kind: "entrant", round: "R32_ENTRANT", pick: teamPickValue("USA"), source: "Admin_/official" },
  },
};
if (officialR32AuthoritySource(supabaseOfficial) !== "Supabase:Admin_/official") throw new Error("Supabase source was not recognized");
const staticOfficial = { officialR32AuthoritySource: "StaticJsonFallback:official_round_of_32" };
if (officialR32AuthoritySource(staticOfficial) === "Supabase:Admin_/official") throw new Error("Static fallback masqueraded as Supabase Admin source");
let bracket = createEmptyBracketDocument({ userId: "player-1", bracketSlots, teamsById, officialR32: supabaseOfficial });
if (bracket.picksBySlot["L-R32-01"].pick.teamId !== "USA") throw new Error("Supabase official R32 did not hydrate entrant");
if (bracket.picksBySlot["L-R32-01"].hydratedFrom !== "Supabase:Admin_/official") throw new Error("hydrated entrant is not tagged Supabase Admin_/official");
bracket = setBracketPick({ bracket, sitePickId: "L-R32-01", pickValue: teamPickValue("BRA") });
if (bracket.picksBySlot["L-R32-01"].pick.teamId !== "USA") throw new Error("player overwrote official R32 entrant");
bracket = setBracketPick({ bracket, sitePickId: "L-R16-01", pickValue: teamPickValue("USA") });
const rehydrated = hydrateOfficialR32Occupants({ bracket, bracketSlots, teamsById, officialR32: supabaseOfficial });
if (rehydrated.picksBySlot["L-R16-01"].pick.teamId !== "USA") throw new Error("player knockout winner pick was not preserved");

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
        errors.append("Supabase Admin_/official R32 source runtime test failed:\n" + result.stderr + result.stdout)

if errors:
    print("WC2026 Supabase Admin_/official R32 source verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 official R32 hydration uses Supabase Admin_/official as primary authority and fails closed for public Supabase official-source misses.")
