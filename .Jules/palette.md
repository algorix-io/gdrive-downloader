## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-03-03 - [Synchronous Form Loading UX]
**Learning:** Even for synchronous form submissions (like standard POST logins), users benefit from immediate visual feedback. If a page takes a moment to reload, users might click the submit button multiple times, causing duplicate submissions or confusion.
**Action:** Use JavaScript to intercept synchronous form submissions, instantly disable the submit button, and update its text (e.g., "[DECRYPTING...]") before allowing the default form submission or programmatic submission to proceed. This prevents duplicate clicks and provides immediate, perceived performance improvements.
