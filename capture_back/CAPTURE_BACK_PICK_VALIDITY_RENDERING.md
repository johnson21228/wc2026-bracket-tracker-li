# Capture Back: Pick Validity Rendering

## Change
Defined and implemented invalid pick rendering as a non-destructive warning layer.

Invalid picked cells keep the existing flag/code identity and add:

- thin red outline
- red `!` marker
- accessible/title reason when available

## Why
A bracket pick is user intent. Current standings and slot rules may prove that intent invalid, but the UI should show that fact rather than silently clearing the pick.

## Verification
Added `tools/verify_wc2026_pick_validity_rendering.py` and wired it into `make verify`.
