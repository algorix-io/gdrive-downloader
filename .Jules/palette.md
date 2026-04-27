## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-04-27 - [Visual Loading Feedback for Synchronous Forms]
**Learning:** Even for fast, synchronous form submissions like a password check, immediate visual feedback (disabling the button and changing text) is necessary to prevent duplicate clicks and communicate progress to the user.
**Action:** When updating form submission elements, convert `<input type="submit">` to a semantic `<button type="submit">` so its text can be dynamically altered via JavaScript, and ensure it respects the existing theme when in a disabled state.
