// Public Supabase browser configuration for Bracketeering Pub.
//
// The anon key is intended to be public in browser apps when RLS policies protect data.
// Keep service_role keys and any private secrets out of this repo.
//
// To enable Auth on GitHub Pages:
// 1. Set enabled to true.
// 2. Set supabaseUrl to your project API URL, for example:
//    https://YOUR_PROJECT_REF.supabase.co
// 3. Set supabaseAnonKey to the project's public anon key.
// 4. Configure Supabase Auth redirect URLs to include the Pages URL and local dev URL.

export const WC2026_SUPABASE_PUBLIC_CONFIG = Object.freeze({
  enabled: false,
  supabaseUrl: "",
  supabaseAnonKey: "",
  authFlow: "magic_link",
});
