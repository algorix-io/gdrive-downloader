## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-25 - [Synchronous Form Loading UX]
**Learning:** Even on synchronous forms (like simple logins), users can experience a perceivable delay on slow connections, leading to duplicate clicks and frustration. Providing immediate visual feedback (e.g., disabling the submit button and changing its text) makes the interface feel more responsive.
**Action:** Always add an immediate loading state via JS on the `submit` event to synchronous form buttons to prevent double submissions and provide clear feedback that action is being taken.
