from playwright.sync_api import Page, expect, sync_playwright

def verify_feature(page: Page):
    page.goto("http://localhost:8000/down.php")
    page.wait_for_timeout(500)

    # Fill in the password
    password_input = page.locator("#access_password")
    password_input.fill("testpassword")
    page.wait_for_timeout(500)

    # Click the ENTER button
    enter_button = page.locator("#loginBtn")

    # In order to see the visual loading state without the page navigating away,
    # we can use page.evaluate to add a temporary preventDefault to the form
    page.evaluate("""() => {
        const form = document.getElementById('loginForm');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
        });
    }""")

    enter_button.click()

    # Wait a bit for the setTimeout to run and the UI to update
    page.wait_for_timeout(500)

    # Assert the button is disabled and has the correct text
    expect(enter_button).to_be_disabled()
    expect(enter_button).to_have_text("[DECRYPTING...]")

    # Capture screenshot
    page.screenshot(path="/home/jules/verification/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/home/jules/verification/video")
        page = context.new_page()
        try:
            verify_feature(page)
        finally:
            context.close()
            browser.close()
