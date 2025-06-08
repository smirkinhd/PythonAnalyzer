import asyncio
from playwright.async_api import async_playwright
import sys
import os
from urllib.parse import urljoin
from aiohttp import web
import aiofiles


async def start_server(html_path, port=8000):
    async def handler(request):
        async with aiofiles.open(html_path, mode='r', encoding='utf-8') as f:
            content = await f.read()
        return web.Response(text=content, content_type='text/html')

    app = web.Application()
    app.router.add_get('/', handler)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', port)
    await site.start()
    return runner, site


async def analyze_page(html_path: str):
    # Запускаем HTTP-сервер
    runner, site = await start_server(html_path)

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto(f"http://localhost:8000")
            await page.wait_for_timeout(2000)

            console_messages = []
            page.on("console", lambda msg: console_messages.append(msg.text))

            # Получаем данные
            cookies = await context.cookies()
            local_storage = await page.evaluate("() => JSON.parse(JSON.stringify(window.localStorage))")
            session_storage = await page.evaluate("() => JSON.parse(JSON.stringify(window.sessionStorage))")

            print("🧪 Cookies:", cookies)
            print("🧪 LocalStorage:", local_storage)
            print("🧪 SessionStorage:", session_storage)
            print("🧪 Console Logs:", console_messages)

            await browser.close()
    finally:
        await site.stop()
        await runner.cleanup()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python analyze_dynamic.py suspicious.html")
        sys.exit(1)
    asyncio.run(analyze_page(sys.argv[1]))