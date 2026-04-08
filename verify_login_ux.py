from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/down.php")

        # Verify login form
        if page.locator("input[name='access_password']").count() > 0:
            print("Login form found.")
            page.fill("input[name='access_password']", "matrixCore2025")

            # Click and immediately take a screenshot to capture the "DECRYPTING..." state
            # Note: since the page reloads, we need to take a screenshot very fast
            # To prevent reload from hiding it, we can evaluate a script to stop default submission
            page.evaluate("document.getElementById('loginForm').addEventListener('submit', (e) => e.preventDefault())")

            page.click("#loginBtn")

            page.screenshot(path="verification_login_disabled.png")
            print("Screenshot taken.")
        else:
            print("Login form not found. Maybe already logged in.")

        browser.close()

if __name__ == "__main__":
    run()
