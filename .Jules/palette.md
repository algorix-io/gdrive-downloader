## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-04-28 - [Synchronous Form Loading States]
**Learning:** Even synchronous form submissions (like standard POST requests) need immediate visual loading feedback. Without it, users might double-click or think the app is unresponsive, especially on slower connections or themed UIs where native loading indicators might be subtle.
**Action:** Always intercept synchronous form submissions with JS to provide immediate visual feedback (e.g., disabling the submit button and changing its text) before the page unloads, preventing double-clicks and improving perceived performance.

## 2026-04-28 - [Themed Disabled Elements]
**Learning:** When using custom themes with `:hover` states on buttons or inputs, those `:hover` styles often incorrectly apply to the `:disabled` state, causing confusing visual feedback (e.g., a disabled button changing color on hover).
**Action:** Always explicitly define or override styles for disabled elements (e.g., `background: transparent !important;` for `button:disabled`) to ensure they remain visually inactive regardless of user interaction.
