# Open Site Make Targets

The WC2026 bracket tracker site should be tested through a local HTTP server, not by opening `site/index.html` directly with `file://`.

The site uses JavaScript modules and local checked-in JSON data. A local server gives the browser the same basic loading behavior expected by the runtime.

## Commands

```bash
make opensite
```

Starts a local site server on port `8000`, serves the `site/` directory, and opens:

```text
http://localhost:8000
```

```bash
make stopsite
```

Stops the local server started by `make opensite`, or any process listening on port `8000` if the PID file is unavailable.

## Runtime boundary

These targets are developer conveniences. They must not change the site runtime model, source data, pick menu behavior, or Living Infrastructure rules.
