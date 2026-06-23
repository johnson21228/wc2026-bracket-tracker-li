# Group Stage later-round frame-only rendering

During Group Stage presentation, the board renders Round of 32 pick fills normally but renders later-round pick slots as frame-only.

Frame-only means:

- no filled team background
- no flag/code identity
- no pick slot label
- no `Choose Winner` placeholder

This is a presentation rule only:

- stored picks are preserved
- pick write/read state is unchanged
- later-round fills, labels, teams, and Champion Aura return when Knockout Stage presentation is active
- Game 2 resolved R32 display remains visible
