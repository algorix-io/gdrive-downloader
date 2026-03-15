## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-03-15 - [Synchronous Form Feedback]
**Learning:** Even for synchronous form submissions, relying purely on the browser's implicit loading state (network indicator) can leave users confused and prone to duplicate submissions, especially on fast connections or themed UIs where native indicators are less noticeable.
**Action:** Always provide immediate visual feedback (e.g., changing button text to a loading state and disabling the button) via a JavaScript event listener on the form's `submit` event, ensuring the user immediately knows the request is processing.
