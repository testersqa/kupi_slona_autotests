from components.base_component import BaseComponent


class HeaderMenu(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.menu = page.locator("#header_menu")

    def click_name_catalog(self, name: str):
        name_catalog = f"a:has-text('{name}')"
        self.menu.locator(name_catalog).click()
