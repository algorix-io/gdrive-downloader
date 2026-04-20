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

        # 2. Verify Button Focus Style
        # First, we need to login because the main button is behind auth
        # Check if we are at login
        if page.locator("input[name='access_password']").count() > 0:
            print("Logging in...")
            page.fill("input[name='access_password']", "matrixCore2025")

            # Verify the UX Loading state on login form
            page.evaluate("""
                window.__testLoginListener = function(e) { e.preventDefault(); };
                document.getElementById('loginForm').addEventListener('submit', window.__testLoginListener);
            """)

            # Click button and check state
            page.click("#loginBtn")

            login_btn = page.locator("#loginBtn")
            btn_text = login_btn.inner_text()
            is_disabled = login_btn.is_disabled()

            print(f"Login button text during submit: {btn_text}")
            print(f"Login button disabled state: {is_disabled}")

            if btn_text != "[DECRYPTING...]" or not is_disabled:
                print("FAILED: Login button loading state not applied correctly.")
                exit(1)

            # Remove listener and actually submit
            page.evaluate("""
                document.getElementById('loginForm').removeEventListener('submit', window.__testLoginListener);
                document.getElementById('loginForm').submit();
            """)
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
