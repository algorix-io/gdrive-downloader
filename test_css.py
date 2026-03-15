from playwright.sync_api import sync_playwright

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
            });
        }""")

        page.fill("input[name='access_password']", "matrixCore2025")

        btn = page.locator("#loginBtn")
        btn.click()

        # check css
        bg = btn.evaluate("el => getComputedStyle(el).backgroundColor")
        print("After disabled bg color:", bg)

        # Hover over it
        btn.hover()
        bg_hover = btn.evaluate("el => getComputedStyle(el).backgroundColor")
        print("After disabled bg color on hover:", bg_hover)

        browser.close()

if __name__ == "__main__":
    run()
