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

        # 2. Verify Loading State and Disabled Styles on Login Button
        if page.locator("input[name='access_password']").count() > 0:
            print("Verifying login loading state...")
            page.fill("input[name='access_password']", "matrixCore2025")

            # Use evaluate to add a preventDefault listener so we can check the loading state
            # without the page navigating away immediately.
            page.evaluate("""() => {
                const form = document.getElementById('loginForm');
                if(form) {
                    form.addEventListener('submit', (e) => {
                        e.preventDefault();
                    });
                }
            }""")

            login_btn = page.locator("#loginBtn")
            login_btn.click()

            # Wait a tiny bit for the setTimeout to trigger
            page.wait_for_timeout(100)

            # Assert text changed
            btn_text = login_btn.inner_text()
            print(f"Login button text after submit: {btn_text}")
            if btn_text != "[DECRYPTING...]":
                print("FAILED: Login button text did not change to [DECRYPTING...]")
                exit(1)

            # Assert button is disabled
            is_disabled = login_btn.is_disabled()
            print(f"Login button is disabled: {is_disabled}")
            if not is_disabled:
                print("FAILED: Login button is not disabled")
                exit(1)

            # Assert disabled style - hover should not apply background color
            # First force a hover
            login_btn.hover(force=True)
            bg_color = login_btn.evaluate("element => getComputedStyle(element).backgroundColor")
            print(f"Disabled login button background color on hover: {bg_color}")
            if bg_color != "rgba(0, 0, 0, 0)": # transparent
                print("FAILED: Disabled button hover style is not transparent")
                exit(1)

            # Take a screenshot of the disabled state
            page.screenshot(path="verification_login_disabled.png")

            # Now actually submit by removing our listener and triggering submit, or just reloading and doing it normally
            page.goto("http://localhost:8000/down.php")
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
