from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:8000/down.php")
    page.wait_for_timeout(500)

    # Fill in the access code
    page.fill("input[name='access_password']", "matrixCore2025")
    page.wait_for_timeout(500)

    # Add an event listener to prevent default form submission to capture the visual loading state
    page.evaluate("""() => {
        document.getElementById('loginForm').addEventListener('submit', (e) => {
            e.preventDefault();
        });
    }""")

    # Click the button
    page.click("#loginBtn")
    page.wait_for_timeout(500)

    # Take screenshot of the visual loading state (button should be DECRYPTING...)
    page.screenshot(path="verification_decrypting.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="videos_decrypt"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
