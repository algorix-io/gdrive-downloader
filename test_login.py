from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/down.php")

        # intercept the form submit to see loading state
        page.evaluate("""() => {
            const form = document.querySelector('form');
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                console.log("Form submitted!");

                // Keep default form submission action if we want, but since we intercepted, it halts.
                // We're just checking the loading state right now.
            });
        }""")

        page.fill("input[name='access_password']", "matrixCore2025")

        # get initial state
        btn = page.locator("#loginBtn")
        print("Before text:", btn.evaluate("el => el.textContent"))
        print("Before disabled:", btn.evaluate("el => el.disabled"))

        # click button
        btn.click()

        # check state
        after_text = btn.evaluate("el => el.textContent")
        after_disabled = btn.evaluate("el => el.disabled")
        print("After text:", after_text)
        print("After disabled:", after_disabled)

        assert after_text == "[DECRYPTING...]", f"Expected [DECRYPTING...], got {after_text}"
        assert after_disabled is True, "Button should be disabled after click"
        print("Assertion passed successfully.")

        browser.close()

if __name__ == "__main__":
    run()
