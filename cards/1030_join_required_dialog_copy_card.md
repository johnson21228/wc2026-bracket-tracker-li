# Card 1030: Join Required Dialog Copy

## Change

Update the Join/Profile dialog copy so signed-out players are told that playing Bracketeering requires joining the Pool.

## Runtime expectations

- Signed-out title: `Join the Pool`
- Signed-out intro: `Playing Bracketeering requires you to join the Pool.`
- Signed-out guidance explains Google sign-in avoids email verification.
- Signed-out guidance tells email-link users to check spam if needed.
- Signed-out state: `Not joined yet.`
- Signed-in title: `Profile`
- Signed-in copy only supports editing the player name and logging out.

## Verification

`python3 tools/verify_wc2026_join_required_dialog_copy.py`
