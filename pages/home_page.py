from pages.base_page import BasePage
from components.header_component import HeaderComponent


class HomePage(BasePage):
    '''
    Главная страница
    '''
    def __init__(self, page):
        self.url = "https://kupislona-store.ru/"
        super().__init__(page, self.url)
        # self.cart_button = page.locator("#block-uc-ajax-cart-delta-0")

    def open_home_page(self):
        self.page.goto(self.url)

    def get_header(self):
        return HeaderComponent(self.page)

    def click_button_cart(self):
        self.get_header().get_button_cart().click()

    def get_coun_in_cart(self):
        return self.get_header().get_cart()
