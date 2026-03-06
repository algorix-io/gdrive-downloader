## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-24 - [Synchronous Form Loading States]
**Learning:** Even synchronous form submissions (like login) need immediate visual feedback. Users may double-click or feel the app is unresponsive during the brief server roundtrip.
**Action:** Always provide a loading state (e.g., disabling the button, changing text to "DECRYPTING...") on synchronous forms using JavaScript to improve perceived performance and prevent duplicate submissions.
