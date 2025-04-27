from playwright.sync_api import Page, expect

def test_submitted(page: Page) -> None:
    page.goto("https://www.google.com")
    page.locator("div[role=\"button\"]:has-text(\"Settings\")").click()
    expect(page.locator("text=Search settings")).to_have_text("Search settings")