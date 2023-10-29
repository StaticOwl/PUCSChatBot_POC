'''This script is going to be used to scrape the data from the webpages that are
mentioned in the urls.txt file. The data is going to be stored in the runtime folder.
I am going to use playwright async for loading the webpages and then I am going to
use the selectors to get the data from the webpages.'''

import os
# from utils.fileloader import print_env
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright:Playwright, url:str):
    browser = await playwright.webkit.launch(headless=True)
    page = await browser.new_page()
    await page.goto(url)
    await browser.close()

async def scrape():
    async with async_playwright() as playwright, \
    open(os.getenv("URL_LIST_PATH"), "r") as urls:
        for url in urls:
            await run(playwright, url)

def main():
    asyncio.run(scrape())