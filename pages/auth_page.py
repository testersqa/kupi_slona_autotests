from playwright.sync_api import Page, Locator

from controls import *
from pages.base_page import BasePage
from components.header_component import HeaderComponent
from components.auth_component import AuthComponent


class AuthPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://kupislona-store.ru/user')

    def get_header_component(self):
        return HeaderComponent(self.page)

    def get_auth_component(self):
        return AuthComponent(self.page, self.page.locator('div.column'))