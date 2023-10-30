"""This script is going to be used to scrape the data from the webpages that are
mentioned in the urls.txt file. The data is going to be stored in the runtime folder.
I am going to use playwright async for loading the webpages, and then I am going to
use the selectors to get the data from the webpages."""
import json
import os
import asyncio
from playwright.async_api import async_playwright, Playwright

dataset = []


async def scrape(playwright: Playwright, url: str):
    locator_config = json.load(open(os.getenv("LOCATOR_CONFIG_PATH")))
    data = {}
    strict_no_elements = ["Email", ".pptx", "Title not found"]
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    url_set = url.split("||")
    url_link = url_set[0].strip()
    url_type = url_set[1].strip()
    url_content = url_set[2].strip()
    try:
        await page.goto(url_link, timeout=5000)
        page_title = await page.title()
        page_title = page_title.split('|')
    except Exception as r:
        print(f"Error while accessing the {url}: {r}")
        await browser.close()

    print(f"Page Title: {page_title[0]}")
    flag = not any(element in page_title[0] for element in strict_no_elements)

    if flag and url_type == 'ShortLink':
        site_main_element = page.locator(locator_config.get(url_content))
        site_main_content = await site_main_element.inner_text()
        data['title'] = page_title[0]
        data['context'] = site_main_content.replace('\n', ' ').replace(' – ', '_')

    await browser.close()
    return data


async def browse():
    with open(os.getenv("URL_LIST_PATH"), "r") as urls:
        async with async_playwright() as playwright:
            for url in urls:
                dataset.append(await scrape(playwright, url))
    return dataset


def run():
    result = asyncio.run(browse())
    with open("ouptut.json", "w") as output:
        json.dump(result, output, indent=4)
