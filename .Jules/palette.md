## 2024-05-23 - [Terminal Interface Accessibility]
**Learning:** Terminal-like interfaces (log windows) are inaccessible to screen readers by default because new content is appended silently. Adding `aria-live="polite"` makes them usable instantly. Also, adding `tabindex="0"` allows keyboard users to scroll history.
**Action:** Always add `aria-live` and `tabindex="0"` to any container that acts as a live log or console output.
