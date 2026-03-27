import os
from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Navigate to the login page
    page.goto("http://localhost:8000/down.php")
    page.wait_for_timeout(500)

    # In order to see the [DECRYPTING...] loading state, we need to intercept the form submission
    # and prevent it from actually reloading the page or we'd miss the UI change.

    # 1. Fill the password
    page.fill("input[name='access_password']", "matrixCore2025")
    page.wait_for_timeout(500)

    # 2. Intercept the form submission to prevent actual navigation
    page.evaluate("""() => {
        document.getElementById('loginForm').addEventListener('submit', (e) => {
            e.preventDefault();
        });
    }""")

    # 3. Submit the form
    page.click("button[id='loginBtn']")
    page.wait_for_timeout(500)

    # 4. Take screenshot of the loading state
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Setup video recording directory
        video_dir = "/home/jules/verification/videos"
        os.makedirs(video_dir, exist_ok=True)

        context = browser.new_context(record_video_dir=video_dir)
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
