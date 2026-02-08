from pages.base_page import BasePage
from components.content_up import ContentUp
from components.logo import LogoHeader


class ElemPage(BasePage):
    def __init__(self, page, url):
        super().__init__(page, url)
        self.page = page
        self.url = url

    def header(self):
        self.page.locator("#header")

    def get_header_menu_by_title(self, title):
        return self.page.locator("#superfish-1").get_by_role("link", name=title)

    def get_menu_up_by_title(self, title):
        return ContentUp(self.page, title)

    def click_menu_up_by_title(self, title):
        self.get_menu_up_by_title(title).get_menu_by_title().click()

    def get_logo(self):
        return LogoHeader(self.page)

    def click_by_logo(self):
        self.get_logo().click()

    def footer(self):
        self.page.locator("#footer-wrapper")
