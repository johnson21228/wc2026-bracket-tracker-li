# Guarded Supabase remote smoke path rule

The Supabase remote smoke path is a developer-only terminal harness.

It must not be imported by the public Pages runtime.

It must require explicit environment opt-in.

It may verify the inactive `SupabaseBracketStore` against the applied Supabase dashboard schema, but it must not change the active store mode of the site.

Normal `make verify` may verify the existence and isolation of the smoke path, but must not run the live Supabase smoke harness.
