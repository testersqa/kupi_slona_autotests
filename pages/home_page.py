from pages.base_page import BasePage
from components.header_component import HeaderComponent


class HomePage(BasePage):
    '''
    Главная страница
    '''
    def __init__(self, page, url):
        super().__init__(page, url)

    def get_header(self):
        return HeaderComponent(self.page)

    def click_button_cart(self):
        self.get_header().get_button_cart().click()