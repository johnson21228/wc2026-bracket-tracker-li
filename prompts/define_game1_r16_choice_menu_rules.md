# Prompt — Define Game 1 R16 Choice Menu Rules

Use this prompt before implementing or repairing Game 1 R16 winner-pick behavior.

Confirm that each R16 slot derives its choice menu from the two R32 source slots that feed it. The menu must show exactly those two assigned teams once both are present. If one or both source slots are empty, the R16 menu should not offer a pick.

Preserve R32 assignment picks separately from R16 winner picks. Do not reuse R32 group eligibility rules for R16 winner choices.
