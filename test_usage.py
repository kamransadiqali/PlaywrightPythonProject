import pytest

@pytest.mark.only_browser("chromium")
def test_visit_youtube(page, browser_type):
    page.goto("https://youtube.com")