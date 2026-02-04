from playwright.sync_api import Page, expect

from controls.base_control import BaseControl


class Button(BaseControl):
    def __init__(self, page):
        super().__init__(page, page.locator(".menu_icon.menu-883"))

