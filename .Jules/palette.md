## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-03-14 - [Synchronous Form Loading States]
**Learning:** Users often click submit buttons multiple times if a synchronous form submission takes time, causing confusion or duplicate processing. In themed apps, standard browser loading spinners are missing, making the UI feel frozen. Hover states applying on disabled buttons also look broken.
**Action:** Always provide immediate visual feedback via JS (disabling the button and changing its text) even for synchronous submissions. For themed CSS, explicitly clear hover styles (`background: transparent`) on the `:disabled` pseudo-class.
