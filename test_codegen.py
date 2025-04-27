import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.pause()
    page.get_by_role("link", name="English 6,974,000+ articles").click()
    page.get_by_role("searchbox", name="Search Wikipedia").click()
    page.get_by_role("combobox", name="Search Wikipedia").fill("water")
    page.get_by_role("combobox", name="Search Wikipedia").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
