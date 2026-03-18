from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/down.php")

        # Check if we are at login
        if page.locator("input[name='access_password']").count() > 0:
            print("Login page found.")

            # Add a listener to prevent default form submission so we can inspect the button state
            page.evaluate('''() => {
                const loginForm = document.getElementById('loginForm');
                if (loginForm) {
                    loginForm.addEventListener('submit', (e) => {
                        e.preventDefault();
                        console.log("Form submission intercepted.");
                    });
                }
            }''')

            # Fill the password and trigger submit
            page.fill("input[name='access_password']", "matrixCore2025")
            page.click("button#loginBtn")

            # Let the UI update
            time.sleep(0.5)

            # Assert button is disabled
            login_btn = page.locator("button#loginBtn")
            is_disabled = login_btn.get_attribute("disabled")
            if is_disabled is None:
                print("FAILED: Login button is not disabled after submission.")
                exit(1)
            else:
                print("PASSED: Login button is disabled.")

            # Assert button text is changed
            btn_text = login_btn.text_content()
            if btn_text != "[DECRYPTING...]":
                print(f"FAILED: Expected button text '[DECRYPTING...]', got '{btn_text}'")
                exit(1)
            else:
                print("PASSED: Login button text changed to [DECRYPTING...].")

            page.screenshot(path="verification_loading_state.png")
            print("Screenshot saved to verification_loading_state.png")
        else:
            print("FAILED: Did not find the login form.")
            exit(1)

        browser.close()

if __name__ == "__main__":
    run()