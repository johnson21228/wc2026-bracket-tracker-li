# Capture Back: France Morocco Quarterfinal Result

## Intent

Record the official France vs Morocco quarterfinal result for Bracketeering Pub data.

## Result

- Match: France vs Morocco
- Round: Quarterfinal
- Score: France 2, Morocco 0
- Winner: France
- ESPN/FIFA game id: 53452525

## Patch boundary

This is an official knockout result data patch.

It should update the append-only knockout result data and downstream bracket advancement only. It should not change player picks, Supabase storage shape, UI styling, background presentation, chat behavior, or bracket geometry.

## Verification expectation

- `make verify` should pass.
- France should advance from the France/Morocco quarterfinal.
- Morocco should not advance past this quarterfinal.
- Official R32 truth should remain R32-only.
