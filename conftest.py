import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--browser_type")
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unknown browser: {browser_name}")

        page = browser.new_page()
        yield page
        browser.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_type",
        action="store",
        default="chromium",
        help="Browser to run tests on (chromium, firefox, webkit)"
    )
