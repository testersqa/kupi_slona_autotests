from components.base_component import BaseComponent


class HeaderMenu(BaseComponent):
    def __init__(self, page):
        super().__init__(page, page.locator("#header_menu"))

    def click_name_catalog(self, name: str):
        self.page.locator(f"a:has-text('{name}')").click()
