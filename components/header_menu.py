from playwright.sync_api import Locator
from components.base_component import BaseComponent


class HeaderMenu(BaseComponent):
    def __init__(self, page):
        super().__init__(page, page.locator("#header_menu"))

    def get_menu_link(self, title: str,) -> Locator:
        return self.page.locator(f"a:has-text('{title}')")

    def click_name_catalog(self, title: str):
        self.get_menu_link(title).click()
