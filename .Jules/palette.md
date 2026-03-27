## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-24 - [Immediate Visual Feedback for Synchronous Forms]
**Learning:** Providing immediate visual feedback (like disabling a button and changing text) on synchronous form submissions prevents duplicate clicks and improves perceived performance, especially important when there is backend processing occurring before a page reload or subsequent interactions.
**Action:** When implementing synchronous forms, use JavaScript to intercept the submission, apply a loading/disabled state to the submit button (with appropriate visual styling that doesn't break themes like disabled button backgrounds), and prevent duplicate submissions.
