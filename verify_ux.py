from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/down.php")

        # 1. Verify Log Window is focusable (tabindex="0")
        log_window = page.locator("#logWindow")
        # Log window is present on the login page too? Let's check.
        # Yes, it is.

        tabindex = log_window.get_attribute("tabindex")
        print(f"Log Window tabindex: {tabindex}")

        if tabindex != "0":
            print("FAILED: Log window does not have tabindex='0'")
            exit(1)

        # Focus the log window and take screenshot
        log_window.focus()
        page.screenshot(path="verification_log_focus.png")

        # 1.5 Verify Synchronous Login Form Loading State
        # We need to test the visual loading state before it navigates.
        if page.locator("input[name='access_password']").count() > 0:
            print("Testing login loading state...")
            page.fill("input[name='access_password']", "matrixCore2025")

            # Add a listener to prevent default so we can inspect the state
            page.evaluate("""
                document.getElementById('loginForm').addEventListener('submit', (e) => {
                    e.preventDefault();
                }, { once: true });
            """)

            # Submit the form using Javascript to trigger the event listener
            page.evaluate("document.getElementById('loginBtn').click()")

            # Check if button is disabled and text changed
            login_btn = page.locator("#loginBtn")
            is_disabled = login_btn.is_disabled()
            text = login_btn.text_content()

            print(f"Login button disabled: {is_disabled}, Text: {text}")

            if not is_disabled or text != "[DECRYPTING...]":
                print("FAILED: Login button loading state not applied correctly")
                exit(1)

            print("Login loading state verified. Proceeding with actual login...")
            # Now we actually login
            page.evaluate("document.getElementById('loginForm').submit()")
            page.wait_for_load_state("networkidle")

        # Wait for the main page form
        page.wait_for_selector("#submitBtn")

        # Focus the submit button
        submit_btn = page.locator("#submitBtn")
        submit_btn.focus()

        # Take a screenshot of the focused button
        page.screenshot(path="verification_button_focus.png")

        # Check CSS properties
        # We want to verify that outline is none and box-shadow is applied
        # Note: box-shadow might be complex to parse, but we can check if it's not 'none'
        box_shadow = submit_btn.evaluate("element => getComputedStyle(element).boxShadow")
        outline_style = submit_btn.evaluate("element => getComputedStyle(element).outlineStyle")

        print(f"Button outline style: {outline_style}")
        print(f"Button box shadow: {box_shadow}")

        # In some browsers, :focus-visible only applies on keyboard interaction.
        # .focus() might trigger :focus, but our CSS targets :focus-visible.
        # However, Playwright's .focus() usually behaves like a script focus.
        # Let's try to simulate Tab navigation to be sure.
        page.locator("#drive_link").focus()
        page.keyboard.press("Tab")
        page.screenshot(path="verification_tab_focus.png")

        browser.close()

if __name__ == "__main__":
    run()
