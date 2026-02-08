from components.base_component import BaseComponent

class LogoHeader(BaseComponent):
    '''
    Класс Логотипа в Header на сайте.
    '''
    def __init__(self, page):
        super().__init__(page, page.locator("#logo"))