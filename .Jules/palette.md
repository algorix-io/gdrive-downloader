## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-24 - [Themed Focus Visibility]
**Learning:** Standard browser focus rings often clash with or are invisible in dark/themed interfaces (like Matrix style). Using `box-shadow` to create a "glow" effect provides a high-contrast, theme-appropriate focus indicator that is superior to `outline: none` alone.
**Action:** Replace default outlines with theme-consistent `box-shadow` or `border` styles for focus states to ensure keyboard accessibility doesn't break immersion.

## 2026-04-06 - [Synchronous Loading Feedback]
**Learning:** Even synchronous form submissions (like standard POSTs) benefit from immediate visual feedback. Disabling the submit button and changing its text to a loading state prevents duplicate clicks and improves perceived performance, which is a key UX pattern.
**Action:** Add visual loading states (e.g., button disable + text change) to standard forms via JavaScript to provide immediate feedback before page navigation occurs.
## 2026-05-09 - Semantic Input Types & Preserving Custom Styles
**Learning:** Using semantic input types (like `type="url"`) significantly improves mobile UX by triggering the correct virtual keyboard layout. However, doing so without care can break existing CSS styling if rules are explicitly targeting `input[type=text]`.
**Action:** Whenever converting an `input[type="text"]` to a more semantic type (e.g., `email`, `url`, `tel`), I must always  the CSS to ensure the new input type is added to all corresponding selectors, ensuring visual consistency.
## 2026-05-09 - Semantic Input Types and Preserving Custom Styles
**Learning:** Using semantic input types like type=url significantly improves mobile UX by triggering the correct virtual keyboard layout. However, doing so without care can break existing CSS styling if rules are explicitly targeting input[type=text].
**Action:** Whenever converting an input[type=text] to a more semantic type like email, url, or tel, I must always grep the CSS to ensure the new input type is added to all corresponding selectors, ensuring visual consistency.
