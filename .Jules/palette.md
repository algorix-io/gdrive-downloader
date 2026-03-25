## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-25 - [Immediate Visual Feedback for Synchronous Forms]
**Learning:** Providing immediate visual feedback (disabling buttons, changing text to indicate a loading state) on synchronous form submissions prevents duplicate clicks and improves the perceived performance of the app, especially in customized interfaces where default browser indicators might be less apparent or clash with the theme.
**Action:** Apply a visual "loading" state to submit buttons even for synchronous forms to give users instant assurance their action is being processed. In custom-styled buttons, ensure disabled states override hover styles (e.g., `background: transparent`) to maintain correct visual semantics.
