from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class MenuComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.button_search = page.locator(".menu_icon.menu-883")
        self.menu = page.locator(".menu clearfix")

    def click_button(self):
        self.button_search.click()

