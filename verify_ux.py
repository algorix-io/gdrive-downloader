from playwright.sync_api import sync_playwright

import os

def run():
    # clear session files
    os.system("rm -f /tmp/sess_*")
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

        # 1.5 Verify Loading state on synchronous login form
        # We intercept the submit to check if the button goes disabled
        if page.locator("#loginForm").count() > 0:
            print("Intercepting login form to check visual loading state...")
            # We add a listener in page that calls preventDefault so it doesn't navigate
            page.evaluate("""
                const form = document.getElementById('loginForm');
                if(form) {
                    form.addEventListener('submit', (e) => {
                        e.preventDefault();
                    });
                }
            """)
            page.fill("input[name='access_password']", "matrixCore2025")

            # Click the login btn
            page.click("#loginBtn")

            # Check if button is disabled and text is DECRYPTING...
            login_btn = page.locator("#loginBtn")
            is_disabled = login_btn.is_disabled()
            btn_text = login_btn.inner_text()

            print(f"Login button disabled state: {is_disabled}")
            print(f"Login button text: {btn_text}")

            if not is_disabled or "DECRYPTING" not in btn_text:
                print("FAILED: Login button does not show proper loading state!")
                exit(1)

            # Now we actually log in
            page.evaluate("""
                const form = document.getElementById('loginForm');
                if(form) {
                    // Remove our preventDefault listener by cloning and replacing
                    const newForm = form.cloneNode(true);
                    form.parentNode.replaceChild(newForm, form);
                }
            """)
            # the form is new so we need to fill it again and submit
            page.fill("input[name='access_password']", "matrixCore2025")
            # we need to re-click the button. But wait, after the clone, event listeners added by DOMContentLoaded might be lost.
            # actually our js adds event listener to the form! If we clone, it's lost.
            # let's just navigate to login again and submit properly
            page.goto("http://localhost:8000/down.php")
            page.fill("input[name='access_password']", "matrixCore2025")
            page.click("#loginBtn")
            page.wait_for_load_state("networkidle")

        # 2. Verify Button Focus Style
        # First, we need to login because the main button is behind auth
        # Check if we are at login
        if page.locator("input[name='access_password']").count() > 0:
            print("Logging in...")
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
