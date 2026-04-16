## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-24 - [Synchronous Form Loading States]
**Learning:** Even synchronous forms that immediately trigger a page reload benefit from a visual loading state on submission. Users with slower connections might double-click or feel uncertain if the button provides no feedback during the network round-trip.
**Action:** Always intercept form submissions via JavaScript to disable the submit button and change its text/icon to a loading state, even if the form submission isn't an asynchronous AJAX request.
