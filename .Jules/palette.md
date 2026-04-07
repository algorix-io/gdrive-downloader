## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-28 - [Synchronous Form Loading States]
**Learning:** Even for synchronous form submissions, providing immediate visual feedback (like disabling the submit button and changing its text) prevents duplicate clicks and improves perceived performance. Also, custom `:hover` styles on disabled buttons need explicit overrides (like `background: transparent !important;`) to prevent the hover effect from applying.
**Action:** Always implement a loading state on form submissions, even synchronous ones. Ensure disabled button styles explicitly override hover effects.