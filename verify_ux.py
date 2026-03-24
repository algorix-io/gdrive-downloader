from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/down.php")

        print("Checking for login form...")

        # Verify the loginBtn exists and is initially active
        login_btn = page.locator("#loginBtn")
        if login_btn.count() == 0:
            print("FAILED: #loginBtn not found on page.")
            exit(1)

        print("Initial button text:", login_btn.text_content())
        print("Is button disabled?", login_btn.is_disabled())

        # Fill the form
        page.fill("input[name='access_password']", "matrixCore2025")

        print("Submitting the form and blocking navigation...")
        # Inject script to prevent default form submission to observe loading state
        page.evaluate("""
            const form = document.getElementById('loginForm');
            form.addEventListener('submit', (e) => {
                e.preventDefault();
            });
        """)

        # Click the login button
        login_btn.click()

        # Wait a small moment to ensure JS executes
        page.wait_for_timeout(500)

        # Verify button text has changed to [DECRYPTING...]
        new_text = login_btn.text_content()
        is_disabled = login_btn.is_disabled()

        print("New button text:", new_text)
        print("Is button disabled?", is_disabled)

        if "[DECRYPTING...]" not in new_text:
            print("FAILED: Button text did not change to [DECRYPTING...]")
            exit(1)

        if not is_disabled:
            print("FAILED: Button was not disabled")
            exit(1)

        # Check the background color is transparent
        bg_color = login_btn.evaluate("el => window.getComputedStyle(el).backgroundColor")
        print("Disabled button background color:", bg_color)
        if bg_color != "rgba(0, 0, 0, 0)":
            print("WARNING: Button background color may not be transparent. Found:", bg_color)

        page.screenshot(path="verification_loading_state.png")
        print("Screenshot saved to verification_loading_state.png")

        browser.close()

if __name__ == "__main__":
    run()
