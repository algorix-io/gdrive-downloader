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

        # 2. Verify Login Button Loading State
        if page.locator("#loginForm").count() > 0:
            print("Checking login form loading state...")
            page.fill("input[name='access_password']", "matrixCore2025")

            # Use evaluate to add preventDefault so we can inspect the state after clicking
            page.evaluate('''() => {
                document.getElementById('loginForm').addEventListener('submit', (e) => {
                    e.preventDefault();
                }, { capture: true }); // capture to run before or after the existing one depending, but here we just want to stop navigation
            }''')

            # Note: capturing preventDefault might prevent the inline handler if it's relying on default action,
            # but our handler in down.php just listens to 'submit'. It doesn't depend on default action happening.
            page.click("#loginBtn")

            # Wait a tick for JS to run
            page.wait_for_timeout(100)

            login_btn = page.locator("#loginBtn")
            is_disabled = login_btn.is_disabled()
            text_content = login_btn.text_content()

            print(f"Login Button Disabled: {is_disabled}")
            print(f"Login Button Text: {text_content}")

            if not is_disabled or "[DECRYPTING...]" not in text_content:
                print("FAILED: Login button loading state not applied correctly.")
                exit(1)

            # Take a screenshot of the loading state
            page.screenshot(path="verification_login_loading.png")
            print("Login button loading state verified.")

            # Now let's reload and actually login
            page.reload()
            page.fill("input[name='access_password']", "matrixCore2025")
            page.click("#loginBtn")
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
