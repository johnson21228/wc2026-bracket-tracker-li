# SQLite storage adapter rule

SQLite is a valid future persistence layer only behind a server/API boundary.

The static browser site must not assume it can write directly to a shared SQLite database.

The site should code against a storage adapter interface so localStorage, JSON import/export, and future SQLite-backed APIs can share the same bracket model.
