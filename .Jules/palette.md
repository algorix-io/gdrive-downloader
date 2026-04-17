## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.
## 2026-04-17 - Immediate Feedback for Synchronous Forms
**Learning:** Even for synchronous form submissions (like standard POSTs) where the page immediately unloads, providing a visual loading state (disabling the button, updating text) drastically improves perceived performance and prevents duplicate submissions while the user waits for the network request to finish.
**Action:** Always add a synchronous `submit` event listener on forms to update the submit button UI state immediately, even if the form isn't handled via AJAX.
