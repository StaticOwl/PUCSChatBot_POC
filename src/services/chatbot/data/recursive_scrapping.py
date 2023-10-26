'''Not willing to use this file as the scrapping for the website is 
not working as expected, manily due to the cloudflare protection
and unstructured/incosistent html pages. This script, although is going to serve as
a great resource for scraping recursively later. For now I am going to use another script
that I will write in the same directory.'''

import os
import argparse
import json
import asyncio
from urllib.parse import urljoin
from playwright.async_api import async_playwright

# Initialize a set to store visited URLs
os.makedirs("runtime", exist_ok=True)
visited_urls = set()
url_that_matters = set()
content = {}


async def safe_remove_element(element):
    try:
        await element.evaluate('(element) => element.remove()')
    except Exception:
        pass


async def scrape_page(url):
    if url in visited_urls:
        return

    visited_urls.add(url)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=5000)
            page_title = await page.title()
        except Exception as r:
            print(f"Error accessing {url}: {r}")
            await browser.close()

        print(f"Page Title: {page_title}")
        page_title_main = page_title.split('|')[0]
        page_title_sub = page_title.split('|')[1] if len(page_title.split('|')) > 1 else None

        strict_no_elements = ["Email", ".pptx", "Title not found"]
        flag = not any(element in page_title_main for element in strict_no_elements)

        if "Cloudflare" != page_title_sub and flag:
            url_that_matters.add(url)
            site_main_element = page.locator("main#site-main")

            headers = await site_main_element.locator("header").all()
            for header in headers:
                if await header.is_visible():
                    await safe_remove_element(header)

            footers = await site_main_element.locator("footer").all()
            for footer in footers:
                if await footer.is_visible():
                    await safe_remove_element(footer)

            site_main_content = await site_main_element.inner_text()
            content[page_title_main] = site_main_content

            links = await site_main_element.locator("a").all()
            for link in links:
                href = await link.get_attribute("href")
                if href and not href.startswith("mailto:"):
                    if href and (href.startswith(('http://', 'https://')) or href.startswith('//')):
                        absolute_url = href
                    else:
                        absolute_url = urljoin(url, href)
                    await scrape_page(absolute_url)

        await browser.close()


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--url', '-u', type=str)
        args = parser.parse_args()
        base_url = args.url

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(scrape_page(base_url))
    except Exception as e:
        print("Exception Occurred", e)
        pass

    with open("runtime/visited_urls.txt", "w") as file:
        file.write("\n".join(visited_urls))
    with open("runtime/url_that_matters.txt", "w") as file:
        file.write("\n".join(url_that_matters))
    with open("runtime/output_data.txt", "w") as file:
        file.write(json.dumps(content, indent=2))
    print("File Written Successfully")
