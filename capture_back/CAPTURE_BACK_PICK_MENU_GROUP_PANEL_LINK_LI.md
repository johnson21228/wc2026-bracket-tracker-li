# Capture Back — Pick Menu Group Panel Link LI

## Captured decision

Pick menus that use World Cup group-derived choices must preserve group context.

All group-derived choices should be collected under visible group labels, and each group label should be clickable/tappable to open the shared group standings panel for that group.

## Reason

The group standings panel should be reachable from anywhere in the site that shows a group button or group label, including pick menus. This keeps the bracket-picking flow connected to the underlying group standings model data.

## Runtime boundary

The group label opens the local group panel. It does not navigate to ESPN, FIFA, or any live external standings page.

The WB may use the ESPN standings URL during Capture Back to update normalized model data, but the browser runtime consumes local checked-in JSON.
