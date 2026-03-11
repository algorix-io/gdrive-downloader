## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-03-05 - [Synchronous Loading States]
**Learning:** Even synchronous operations (like form submissions) benefit from immediate visual feedback (e.g., disabling the submit button and changing its text). This prevents duplicate submissions and improves perceived performance while the page reloads.
**Action:** When adding `:disabled` states to buttons, always explicitly reset the `background` (e.g., `background: transparent`) if the button has `:hover` styles, to prevent the hover effect from overriding the disabled appearance.
