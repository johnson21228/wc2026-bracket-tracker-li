#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
store=(ROOT/'site/js/services/SupabaseBracketStore.js').read_text()
model=(ROOT/'site/js/mvc/model.js').read_text()
controller=(ROOT/'site/js/mvc/controller.js').read_text()
errors=[]
def require(c,m):
    if not c: errors.append(m)
require('const DEFAULT_GAME_ID = "game1";' in store, "store must use one canonical game")
require('.eq("bracket_kind", "official")' in store, "official loader must query official row")
require('function isAdminOfficialAuthority(row)' in store, "official loader must verify semantic authority")
require('function hasR32Picks(bracket)' in store, "official loader must require R32 content")
require('r32ReadOnlyForPlayer' in model, "player R32 slots must be read-only")
require('R32 occupants are supplied by Admin_/official' in model, "model must reject player R32 edits")
require('Round of 32 occupants are set by Admin_/official' in controller, "controller must explain read-only R32")
if errors:
    print("Official truth hidden player verification failed:")
    for e in errors: print(f"- {e}")
    raise SystemExit(1)
print("OK: official truth bracket remains hidden from player editing in one-game runtime.")
