from components.base_component import BaseComponent

class LogoHeader(BaseComponent):
    def __init__(self, page):
        super().__init__(page, page.locator('//*[@id="logo"]'))