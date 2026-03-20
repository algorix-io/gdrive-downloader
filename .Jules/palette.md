## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-03-20 - [Synchronous Form Loading States]
**Learning:** Even synchronous form submissions (like standard POST logins) benefit from immediate visual feedback (disabling button, changing text). It prevents duplicate clicks during network latency and improves perceived performance.
**Action:** Always add an instant disabled/loading state via JavaScript `submit` event listeners for forms, even if they aren't fully asynchronous/AJAX based.
