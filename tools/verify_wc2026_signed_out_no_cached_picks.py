from pathlib import Path

model = Path("site/js/mvc/model.js").read_text()
account = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
controller = Path("site/js/mvc/controller.js").read_text()
r32 = Path("site/js/controllers/Game1R32PickController.js").read_text()

errors = []

if "picks = pickFromStorage();" in model:
    errors.append("model.js must not hydrate player picks from localStorage on signed-out startup")
if "saveToStorage(picks);" in model:
    errors.append("model.js must not save player picks to localStorage fallback in join-required runtime")
if "clearAccountPicksForSignedOut" not in model:
    errors.append("model.js must expose clearAccountPicksForSignedOut for auth sign-out cleanup")
if "model.clearAccountPicksForSignedOut();" not in account:
    errors.append("AccountSaveActionSurface must clear rendered player picks when not joined")
if "if (!authSettled) return;" not in account:
    errors.append("AccountSaveActionSurface must not show not-joined guidance before auth settles")
if "signed-out-picks-cleared" not in account or "signed-out-picks-cleared" not in controller:
    errors.append("signed-out pick clearing must dispatch and render accurate user feedback")
if "window.localStorage.getItem(storageKey)" in r32 or "window.localStorage.setItem(storageKey" in r32:
    errors.append("Game1R32PickController must not use cached local projection picks in join-required runtime")
if "Picks are not loaded because you are not signed in." not in controller:
    errors.append("controller must report signed-out picks-not-loaded feedback")

if errors:
    print("WC2026 signed-out no cached picks verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: signed-out players do not see cached local picks and get accurate not-loaded feedback.")
