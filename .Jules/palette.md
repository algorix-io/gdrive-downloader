## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2024-05-18 - Visual Feedback on Synchronous Forms
**Learning:** Even synchronous forms benefit from immediate visual feedback during submission to prevent duplicate clicks and improve perceived performance, especially when server-side processing might take a moment.
**Action:** Always provide a visual loading state (like disabling the button and changing the text) upon form submission, even if it's a traditional synchronous post request.
