# vibeslop that actually connects to the podman, so i'll take that part and remove the others
# no node system

import uuid
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright




QUEUE = [
    "https://google.com",
    "https://github.com",
    "https://hackclub.com",
    "https://aops.com",
    "https://duck.ai",
    "https://wikipedia.org",
    "https://reddit.com",
    "https://phish.directory",
]
ENDPOINT = "ws://localhost:3301/"

SCREENSHOT_DIR = Path(__file__).resolve().parent / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

async def save_image(image_data: bytes, filepath: Path):
    filepath.write_bytes(image_data)

async def run_scan_task(browser, url: str):
    context = await browser.new_context()
    page = await context.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        screenshot_data = await page.screenshot()
        filepath = SCREENSHOT_DIR / f"{uuid.uuid4()}.png"
        await save_image(screenshot_data, filepath)
        print(f"saved screenshot: {filepath}")
    finally:
        await context.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect(ws_endpoint=ENDPOINT, timeout=10000)
        print("connected to podman browser server")

        for url in QUEUE:
            print(f"running task: {url}")
            await run_scan_task(browser, url)

        await browser.close()
        print("browser connection closed")

if __name__ == "__main__":
    asyncio.run(main())
