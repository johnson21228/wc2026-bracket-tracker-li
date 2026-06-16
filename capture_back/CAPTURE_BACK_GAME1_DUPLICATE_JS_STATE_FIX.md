# Capture Back — Game 1 Duplicate JS State Fix

Removed stale duplicate Game 1 state declarations that prevented the script from parsing. The hit target layer was present in markup, but the runtime could not execute because duplicate `const STORAGE_KEY` declarations caused a syntax error.
