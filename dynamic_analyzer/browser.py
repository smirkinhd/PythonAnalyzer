from playwright.sync_api import sync_playwright

def scan_url(url):
    results = {"console": [], "requests": [], "errors": []}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Перехват консольных логов
        page.on("console", lambda msg: results["console"].append(msg.text))
        page.on("request", lambda req: results["requests"].append(req.url))
        page.on("pageerror", lambda err: results["errors"].append(str(err)))

        page.goto(url)
        page.wait_for_timeout(5000)

        browser.close()

    return results
