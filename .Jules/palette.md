## 2026-02-22 - [Terminal Validation Pattern]
**Learning:** Using existing UI components (like a terminal log) for validation feedback maintains immersion better than browser alerts.
**Action:** When working on themed UIs, adapt standard feedback mechanisms (alerts, toasts) to match the theme (terminal logs, matrix text) while ensuring accessibility via ARIA roles.

## 2026-02-25 - [Scrollable Log Accessibility]
**Learning:** Overflowing containers like terminal logs are inaccessible to keyboard users unless they receive focus.
**Action:** Add `tabindex="0"` to any scrollable container that isn't naturally focusable, ensuring keyboard users can scroll through history.
