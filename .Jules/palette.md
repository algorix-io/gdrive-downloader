## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-04-15 - [Synchronous Form Loading States]
**Learning:** Even synchronous forms benefit significantly from visual loading states (like disabling a submit button and changing text) to prevent duplicate submissions and provide immediate feedback, improving the perceived performance. Native disabled styles may clash with dark themes.
**Action:** Always add loading states to forms to prevent duplicate clicks, and ensure disabled elements in themed interfaces have explicit transparent backgrounds to avoid unwanted hover styles.
