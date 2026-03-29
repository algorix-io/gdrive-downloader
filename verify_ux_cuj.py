from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:8000/down.php")
    page.wait_for_timeout(500)

    # Fill in the access code
    page.fill("input[name='access_password']", "matrixCore2025")
    page.wait_for_timeout(500)

    # Submit the form using the new button id and wait for the state change
    page.click("#loginBtn")

    # Wait to see the DECRYPTING... text and disabled state before navigation happens
    # (Since this is a synchronous form, the page will navigate, but we can capture the brief state change
    # if we are fast, or we can just capture the final logged-in state. Let's capture the final logged-in state first)
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(500)

    # Take screenshot of the logged-in state
    page.screenshot(path="verification_cuj.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
