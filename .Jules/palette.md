## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-25 - [Synchronous Form Feedback]
**Learning:** Even synchronous form submissions (like standard login) benefit from immediate visual feedback. If a user clicks 'submit' and the network is slow, they might click again or think it's broken.
**Action:** Always provide visual feedback (disable button, change text) using JS `onsubmit`, even when the form action is handled synchronously by the browser.

## 2026-02-25 - [Themed Disabled Buttons]
**Learning:** When using custom styling and `:hover` background colors for buttons, disabled buttons (`button:disabled`) may incorrectly inherit the hover color if not explicitly reset.
**Action:** Ensure `button:disabled` explicitly sets `background: transparent` (or another appropriate color) to prevent `:hover` from applying background colors incorrectly.
