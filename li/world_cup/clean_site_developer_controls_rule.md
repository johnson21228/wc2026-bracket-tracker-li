# Clean site developer controls rule

The clean WC2026 site may include developer controls below the board surface to support rebuilding the app layer by layer.

Developer controls must be separated from board rendering modules.

They may:

- inspect module status
- show board truth resource paths
- toggle layer visibility
- report pending layers
- expose debugging state

They must not:

- become product UI
- own pick state
- own menu behavior
- read legacy localStorage
- patch legacy runtime behavior

The developer controls panel is a diagnostic surface for rebuild confidence.
