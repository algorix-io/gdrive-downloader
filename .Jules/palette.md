## 2025-05-22 - Accessibility of Console-like Interfaces
**Learning:** Terminal/Console emulators using `div` append often miss `aria-live` regions, leaving screen reader users in the dark about progress.
**Action:** Always wrap dynamic log containers in `aria-live="polite"` and consider `role="log"`.

## 2026-02-23 - Themed Validation over Native Alerts
**Learning:** Native `alert()` dialogs break immersion in heavily themed applications (like a Matrix terminal). Replacing them with in-page error injection maintains flow and context.
**Action:** Use `novalidate` on forms and inject errors into the existing output stream/log window, ensuring `aria-live` regions announce the error.
