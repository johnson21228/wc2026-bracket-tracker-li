# Capture Back Governance

The current repo hygiene convention is:

```text
captures/        current Capture Back reports
capture_back/    legacy/historical Capture Back material
cards/           implementation cards
li/              durable Language Infrastructure rules
docs/            explanatory architecture/workflow docs
```

## Current convention

New CB reports should be created under `captures/`.

Examples:

```text
captures/CAPTURE_BACK_PUBLIC_MULTI_USER_PLAY_LI.md
captures/CAPTURE_BACK_EMPTY_PICK_STATE_STORAGE_MODEL.md
captures/CAPTURE_BACK_CB_GOVERNANCE.md
```

## Apply-script convention

Apply scripts should print each CB report path as it is written:

```text
wrote captures/CAPTURE_BACK_EXAMPLE.md
```

This gives the user a visible terminal clue about where the CB report was placed.

## What not to do

Do not create new root-level CB reports:

```text
CAPTURE_BACK_EXAMPLE.md
```

Do not write new reports to `capture_back/` unless the card explicitly says it is preserving or migrating legacy material.
