#!/usr/bin/env python3
from pathlib import Path
import json

truth = json.loads(Path("site/data/current/official_truth.json").read_text())
picks = truth.get("picksBySlot", {})

expected = {
    "L-R32-01": ("GER", "Germany"),
    "L-R32-02": ("PAR", "Paraguay"),
    "L-R32-03": ("FRA", "France"),
    "L-R32-04": ("SWE", "Sweden"),
    "L-R32-05": ("RSA", "South Africa"),
    "L-R32-06": ("CAN", "Canada"),
    "L-R32-07": ("NED", "Netherlands"),
    "L-R32-08": ("MAR", "Morocco"),
    "L-R32-09": ("POR", "Portugal"),
    "L-R32-10": ("CRO", "Croatia"),
    "L-R32-11": ("ESP", "Spain"),
    "L-R32-12": ("AUT", "Austria"),
    "L-R32-13": ("USA", "USA"),
    "L-R32-14": ("BIH", "Bosnia and Herzegovina"),
    "L-R32-15": ("BEL", "Belgium"),
    "L-R32-16": ("SEN", "Senegal"),
    "R-R32-01": ("BRA", "Brazil"),
    "R-R32-02": ("JPN", "Japan"),
    "R-R32-03": ("CIV", "Côte d’Ivoire"),
    "R-R32-04": ("NOR", "Norway"),
    "R-R32-05": ("MEX", "Mexico"),
    "R-R32-06": ("ECU", "Ecuador"),
    "R-R32-07": ("ENG", "England"),
    "R-R32-08": ("COD", "DR Congo"),
    "R-R32-09": ("ARG", "Argentina"),
    "R-R32-10": ("CPV", "Cabo Verde"),
    "R-R32-11": ("AUS", "Australia"),
    "R-R32-12": ("EGY", "Egypt"),
    "R-R32-13": ("SUI", "Switzerland"),
    "R-R32-14": ("DZA", "Algeria"),
    "R-R32-15": ("COL", "Colombia"),
    "R-R32-16": ("GHA", "Ghana"),
}

errors = []

r32_slots = sorted(slot_id for slot_id in picks if "R32" in slot_id)
if sorted(expected) != r32_slots:
    missing = sorted(set(expected) - set(r32_slots))
    extra = sorted(set(r32_slots) - set(expected))
    if missing:
        errors.append(f"Missing R32 slots: {missing}")
    if extra:
        errors.append(f"Unexpected R32 slots: {extra}")

for slot_id, (team_id, team_name) in expected.items():
    record = picks.get(slot_id, {})
    pick = record.get("pick", {})

    observed_id = pick.get("teamId") or record.get("teamId")
    observed_code = pick.get("teamCode") or record.get("teamCode")
    observed_name = pick.get("teamName") or record.get("teamName")

    if observed_id != team_id:
        errors.append(f"{slot_id} teamId expected {team_id}, found {observed_id}")
    if observed_code != team_id:
        errors.append(f"{slot_id} teamCode expected {team_id}, found {observed_code}")
    if observed_name != team_name:
        errors.append(f"{slot_id} teamName expected {team_name}, found {observed_name}")

    if pick.get("source") != "site-owned-official-truth-r32-schedule":
        errors.append(f"{slot_id} pick.source missing schedule truth marker")

if errors:
    print("WC2026 official truth R32 schedule assignment verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: official_truth.json has all 32 R32 schedule assignments.")
