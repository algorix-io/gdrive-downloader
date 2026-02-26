## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-26 - [Mobile Input Type UX]
**Learning:** Changing `input[type="text"]` to `input[type="url"]` is a high-value micro-UX change that triggers optimized mobile keyboards. However, it requires careful auditing of CSS selectors (e.g., `input[type=text]`) to ensure custom styling isn't lost.
**Action:** When updating semantic HTML types, always grep for the old type in CSS files to maintain visual consistency.
