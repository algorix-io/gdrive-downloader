## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-02-24 - [Disabled Hover Specificity in Themed UIs]
**Learning:** In high-contrast themed interfaces where buttons have prominent `:hover` styles (e.g., background color changes), the `button:disabled` state needs specific overrides (`background: transparent !important;`) to prevent the `:hover` style from improperly activating when users hover over disabled, loading elements.
**Action:** When adding visual loading states or disabling buttons during async/sync submissions, explicitly cancel `:hover` background and text color changes on `:disabled` pseudoclasses to maintain proper visual affordance.
