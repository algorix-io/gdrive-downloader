## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-03-05 - [Synchronous Form Loading States & CSS Specificity]
**Learning:** Even synchronous form submissions (like standard POST requests) benefit immensely from immediate visual feedback. However, custom disabled states often conflict with `:hover` pseudo-classes due to CSS specificity, causing buttons to appear active when disabled if hovered over.
**Action:** Always provide loading states (disabling buttons, updating text) upon form submission using `setTimeout(..., 0)` to prevent duplicate clicks. Additionally, explicitly reset `background` properties in `:disabled` selectors to prevent `:hover` styles from incorrectly applying.
