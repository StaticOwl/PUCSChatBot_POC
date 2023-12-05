"""This script is going to be used to scrape the data from the webpages that are
mentioned in the urls.txt file. The data is going to be stored in the runtime folder.
I am going to use playwright async for loading the webpages, and then I am going to
use the selectors to get the data from the webpages."""
import asyncio
import json
import os
import shutil

from playwright.async_api import async_playwright, Playwright

from backend.utils.data_utils import safe_replace
from .data_preprocessor import update_json_structure, textify_data

dataset = []


async def scrape(playwright: Playwright, url: str, locator_config: dict = None):
    """
    This method is used to scrape the data from the webpages.
    :param playwright: Playwright object which is used to launch the chromium browser.
    :param url: url of the webpage along url type.
    :param locator_config: config file which contains the locator and ignore_words keys based on url type.
    :return: scrapped data in the form of a list of dictionaries.
    """
    temp_dataset = []
    data = {}
    strict_no_elements = ["Email", ".pptx", "Title not found"]
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context(
        ignore_https_errors=True,
        permissions=["geolocation"],
    )
    page = await context.new_page()
    url_set = url.split("||")
    url_link = url_set[0].strip()
    url_content = url_set[1].strip() if len(url_set) > 1 else None
    try:
        await page.goto(url_link, wait_until="domcontentloaded")
        page_title = await page.title()
        page_title = page_title.split('|')
        flag = not any(element in page_title[0] for element in strict_no_elements)
        if flag and url_content is not None and url_content in locator_config:
            print(f"Page Title: {page_title[0]}")
            config = locator_config.get(url_content)
            context_appender: str = ""
            locators = config.get('locator')
            if bool(config.get('shrink')):
                for element in await page.query_selector_all("*[aria-expanded]"):
                    await element.click()
                await asyncio.sleep(int(os.getenv("EXPAND_WAIT_TIME")))
            title_replacements = config.get('title_replacer')
            data['title'] = safe_replace(safe_replace(page_title[0]), title_replacements).strip()
            data['type'] = url_content
            ignore_words = config.get('ignore_words')
            for locator in locators:
                if len(locator.split("->")) > 1:
                    locator, context_appender = locator.split("->")
                await page.wait_for_selector(locator, timeout=int(os.getenv("PAGE_LOAD_TIMEOUT")))
                site_main_element = page.locator(locator)
                site_main_element_count = await site_main_element.count()
                if site_main_element_count > 1:
                    site_main_element_count -= int(config.get('count_subtractor', '0'))
                    data['count'] = str(site_main_element_count)
                for i in range(site_main_element_count):
                    site_main_element_ith = site_main_element.nth(i)
                    site_main_content = await site_main_element_ith.inner_text()
                    if len(ignore_words) > 0:
                        for word in ignore_words:
                            site_main_content = site_main_content.replace(word, '')
                    site_main_content = safe_replace(site_main_content, config.get('text_replacer', {}))
                    data['context'] = (context_appender +
                                       ("_" + str(i) + " " if site_main_element_count > 1 else "") +
                                       (" " if context_appender != "" else "") +
                                       safe_replace(site_main_content).strip())

                    temp_dataset.append(data.copy())
        await browser.close()
        return temp_dataset
    except Exception as r:
        print(f"Error while accessing the {url}: {r}")
        await browser.close()


async def browse(locator_config: dict = None):
    """
    This method is used to browse through the urls.txt file and scrape the data from the webpages.
    :param locator_config: config file which contains the locator and ignore_words keys based on url type.
    :return: all scrapped data from all urls in the form of a list of dictionaries.
    """
    with open(os.getenv("URL_LIST_PATH"), "r") as urls:
        async with async_playwright() as playwright:
            for url in urls:
                datas = await scrape(playwright, url, locator_config)
                if datas:
                    for data in datas:
                        dataset.append(data)
    return dataset


def run():
    """
    This method is used to run the scraper.
    :return: This writes the scrapped data in text format in the runtime folder so that it can be used for training.
    """
    # Delete the runtime folder and create a new one
    shutil.rmtree(os.getenv("RUNTIME_PATH"), ignore_errors=True)
    os.makedirs(os.getenv("RUNTIME_PATH"), exist_ok=True)

    locator_config = json.load(open(os.getenv("LOCATOR_CONFIG_PATH")))

    result = asyncio.run(browse(locator_config))
    result = update_json_structure(result)
    textify_data(result, locator_config)
