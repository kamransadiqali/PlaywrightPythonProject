def test_type(page):
     page.goto("https://www.google.com/")
     page.locator("[aria-label=\"Search\"]").click()
     page.locator("[aria-label=\"Search\"]").type("social media")
     page.locator("[aria-label=\"Search\"]").press("Enter")