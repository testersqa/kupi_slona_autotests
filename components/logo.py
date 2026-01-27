from components.base_component import BaseComponent

class LogoHeader(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def wrapper(self):
        return self.page.locator('//*[@id="logo"]')