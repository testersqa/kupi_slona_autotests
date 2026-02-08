from playwright.sync_api import Page, Locator, expect


class BaseControl:
    def __init__(self, page: Page, wrapper: Locator):
        self.page: Page = page
        self.wrapper: Locator = wrapper

    def click(self):
        self.wrapper.click()


