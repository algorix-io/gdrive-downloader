from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/down.php")

        # Verify initial state of login button
        login_btn = page.locator("#loginBtn")
        print(f"Initial Button Text: {login_btn.inner_text()}")

        # We need to simulate form submission but prevent the actual POST
        # so we can see the synchronous feedback.
        page.evaluate("""
            document.getElementById('loginForm').addEventListener('submit', (e) => {
                e.preventDefault();
            });
        """)

        page.fill("input[name='access_password']", "matrixCore2025")

        # Click the login button
        login_btn.click()

        # Verify the button text and disabled state
        print(f"Button Text After Click: {login_btn.inner_text()}")
        is_disabled = login_btn.is_disabled()
        print(f"Is Button Disabled: {is_disabled}")

        # Take a screenshot to show the UI
        page.screenshot(path="verification_decrypting.png")

        browser.close()

if __name__ == "__main__":
    run()
