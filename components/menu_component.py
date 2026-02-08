from components.base_component import BaseComponent


class MenuComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page, page.locator(".menu clearfix"))
        self.button_search = page.locator(".menu_icon.menu-883")

    def click_button(self):
        self.button_search.click()

