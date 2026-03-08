## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-03-08 - [Synchronous Submission Feedback]
**Learning:** Even synchronous form submissions require immediate visual feedback (like disabling the submit button and showing a loading state) to prevent duplicate clicks and improve perceived performance, especially when server response times might vary.
**Action:** Always implement a loading state (text change and disabled button) via JavaScript `submit` event listeners on forms, even if they result in a full page reload, ensuring theme consistency (e.g., `button:disabled` background colors) is maintained.
