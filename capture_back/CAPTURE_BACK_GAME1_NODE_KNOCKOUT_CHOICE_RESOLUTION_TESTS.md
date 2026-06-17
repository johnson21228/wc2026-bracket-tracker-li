# Capture Back — Game 1 Node knockout choice resolution tests

This capture adds a command-line Node runner for the Game 1 knockout choice-resolution harness.

It supports diagnosis of the empty-set menu issue by separating contestant resolution from browser click/menu rendering.

If the Node runner passes but the UI still shows an empty choice set, the remaining issue is runtime tap/menu wiring. If the Node runner fails, the resolver or its data-store lookup is the issue.
