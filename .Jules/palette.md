## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-25 - [Synchronous Form Loading States & Disabled Hover Overrides]
**Learning:** Immediate visual feedback (disabling submit button and changing text) is important even for synchronous form submissions to prevent duplicate clicks and improve perceived performance. Additionally, in custom-themed UIs, `:hover` states can inadvertently apply to `:disabled` elements if not explicitly overridden (e.g., using `background: transparent !important;`).
**Action:** Always add loading states to forms, even if they submit synchronously, by using a `submit` event listener with a 0ms `setTimeout`. When styling `:disabled` states in custom themes, explicitly negate `:hover` effects to maintain visual consistency.