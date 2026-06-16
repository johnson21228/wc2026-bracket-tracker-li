# Capture Back — Game 1 R32 Choice Menu Team Tile Spacing

The previous spacing attempts targeted generic `.choice*` selectors, but grep confirmed the live menu renderer uses `.teamTile`, `.teamMeta`, `.teamName`, and `.teamDetail`.

This repair adds LI and patches the active renderer CSS so country name and metadata are separated.
