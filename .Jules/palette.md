## 2025-05-22 - Accessibility of Console-like Interfaces
**Learning:** Terminal/Console emulators using `div` append often miss `aria-live` regions, leaving screen reader users in the dark about progress.
**Action:** Always wrap dynamic log containers in `aria-live="polite"` and consider `role="log"`.
