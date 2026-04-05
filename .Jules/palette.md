## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-24 - Immediate Feedback on Synchronous Forms
**Learning:** Even on synchronous forms (like the Matrix Core login page), users can click multiple times or wonder if their request was received before the page unloads/reloads.
**Action:** Always provide immediate visual feedback (e.g., changing button text to "DECRYPTING..." and setting `disabled=true`) upon the `submit` event to prevent duplicate clicks and reassure the user, while ensuring CSS handles the disabled state correctly (e.g., removing hover backgrounds).
