## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-24 - [Synchronous Loading States]
**Learning:** Even synchronous form submissions (like standard POST logins) benefit greatly from immediate visual loading states (e.g., changing button text to "DECRYPTING..." and disabling it). This prevents duplicate clicks and provides immediate reassurance to the user that their action was registered, especially if the server takes a moment to respond.
**Action:** Always implement a programmatic loading state on form submission, regardless of whether the request is synchronous or asynchronous.
