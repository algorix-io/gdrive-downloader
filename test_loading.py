from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://localhost:8000/down.php")

        if page.locator("input[name='access_password']").count() > 0:
            print("Logging in...")
            page.fill("input[name='access_password']", "matrixCore2025")

            # Since form submission navigates, intercept it just long enough to verify the UI state changed.
            # Use page.evaluate to dispatch a submit event instead to prevent immediate navigation blocking
            # our assertions in sync mode.

            page.evaluate("""() => {
                const form = document.getElementById('loginForm');
                form.addEventListener('submit', (e) => {
                    e.preventDefault(); // Stop actual navigation for test
                });
                form.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
            }""")

            # Verify button state
            btn = page.locator("button#loginBtn")
            is_disabled = btn.is_disabled()
            text = btn.inner_text()

            print(f"Disabled: {is_disabled}")
            print(f"Text: {text}")

            if not is_disabled:
                print("FAILED: Button is not disabled")
                exit(1)

            if "[DECRYPTING...]" not in text:
                print("FAILED: Button text did not change to DECRYPTING...")
                exit(1)

            print("SUCCESS: Loading state is working!")

        browser.close()

if __name__ == "__main__":
    run()
