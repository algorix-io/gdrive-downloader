## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-04-08 - [Synchronous Form Loading States]
**Learning:** Even synchronous form submissions (like standard POST logins) benefit from immediate visual feedback (e.g., changing button text to "DECRYPTING..." and disabling it). Playwright tests may fail if they expect a specific `input[type="submit"]` element that is changed to a more semantic `<button>` tag to enable this behavior.
**Action:** When updating form submission elements to improve UX and accessibility (e.g., input to button), ensure all corresponding test selectors in e2e tests (like Playwright) are updated. Use `background: transparent !important` for disabled buttons in custom themes to prevent `hover` pseudo-classes from overriding the disabled state styles.
