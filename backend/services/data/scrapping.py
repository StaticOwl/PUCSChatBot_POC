"""This script is going to be used to scrape the data from the webpages that are
mentioned in the urls.txt file. The data is going to be stored in the runtime folder.
I am going to use playwright async for loading the webpages, and then I am going to
use the selectors to get the data from the webpages."""
import asyncio
import json
import os
import shutil

from playwright.async_api import async_playwright, Playwright

from .data_preprocessor import update_json_structure, textify_data
from backend.utils.data_utils import safe_replace

dataset = []

replacements = {
    "\n": " ",
    " – ": "-",
    "—": "-",
    "●": "*",
    "–": "-",
    "“": "\"",
    "’": "'",
    "”": "\"",
    "‘": "'",
    "é": "e",
    "™": "",
    " ": "",

}


async def scrape(playwright: Playwright, url: str, locator_config: dict = None):
    temp_dataset = []
    data = {}
    strict_no_elements = ["Email", ".pptx", "Title not found"]
    browser = await playwright.chromium.launch(headless=True)
    page = await browser.new_page()
    url_set = url.split("||")
    url_link = url_set[0].strip()
    url_content = url_set[1].strip() if len(url_set) > 1 else None
    try:
        await page.goto(url_link, timeout=50000)
        await page.evaluate('''
            document.querySelectorAll('[x-data]').forEach((element) => {
                element.removeAttribute('x-data');
            });
        ''')
        page_title = await page.title()
        page_title = page_title.split('|')
        flag = not any(element in page_title[0] for element in strict_no_elements)
        if flag and url_content is not None and url_content in locator_config:
            print(f"Page Title: {page_title[0]}")
            config = locator_config.get(url_content)
            context_appender: str = ""
            locators = config.get('locator')
            title_replacements = config.get('title_replacer')
            data['title'] = safe_replace(safe_replace(page_title[0], replacements), title_replacements).strip()
            data['type'] = url_content
            ignore_words = config.get('ignore_words')
            for locator in locators:
                if len(locator.split("->")) > 1:
                    locator, context_appender = locator.split("->")
                site_main_element = page.locator(locator)
                site_main_element_count = await site_main_element.count()
                if site_main_element_count > 1:
                    data['count'] = str(site_main_element_count)
                for i in range(site_main_element_count):
                    site_main_element_ith = site_main_element.nth(i)
                    site_main_content = await site_main_element_ith.inner_text()
                    if len(ignore_words) > 0:
                        for word in ignore_words:
                            site_main_content = site_main_content.replace(word, '')
                    data['context'] = (context_appender +
                                       ("_" + str(i) + " " if site_main_element_count > 1 else "") +
                                       (" " if context_appender != "" else "") +
                                       safe_replace(site_main_content, replacements).strip())

                    temp_dataset.append(data.copy())
        await browser.close()
        return temp_dataset
    except Exception as r:
        print(f"Error while accessing the {url}: {r}")
        await browser.close()


async def browse(locator_config: dict = None):
    with open(os.getenv("URL_LIST_PATH"), "r") as urls:
        async with async_playwright() as playwright:
            for url in urls:
                datas = await scrape(playwright, url, locator_config)
                if datas:
                    for data in datas:
                        dataset.append(data)
    return dataset


def run():
    # Delete the runtime folder and create a new one
    shutil.rmtree(os.getenv("RUNTIME_PATH"), ignore_errors=True)
    os.makedirs(os.getenv("RUNTIME_PATH"), exist_ok=True)

    # Load the locator config
    locator_config = json.load(open(os.getenv("LOCATOR_CONFIG_PATH")))

    # Run the scraper
    result = asyncio.run(browse(locator_config))

    # Save the result (Temporary)
    with open(os.getenv("SCRAPPING_PATH"), "w") as output:
        json.dump(result, output, indent=4)

    # Update the json structure
    result = update_json_structure(result)
    with open(os.getenv("SCRAPPING_PATH_NEW"), "w") as output:
        json.dump(result, output, indent=4)

    textify_data(result, locator_config)  # Not fully Implemented
