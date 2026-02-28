## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.
\n## 2026-02-28 - [Synchronous Submission Feedback]\n**Learning:** In themed UIs where traditional spinners break immersion, using dynamic button text (e.g., `[DECRYPTING...]`) provides crucial immediate visual feedback for synchronous POST submissions.\n**Action:** When working on immersive or heavily themed interfaces, consider changing the button text dynamically on form submit to indicate processing, rather than relying on standard browser loading indicators or un-themed spinners.
