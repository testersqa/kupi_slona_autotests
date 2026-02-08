from components.base_component import BaseComponent
from controls.cart import Cart


class HeaderComponent(BaseComponent):
    '''
    Класс Компонентов Header на сайте. Это верхнее меню, логотип, строка поиска, меню с категориями
    '''
    def __init__(self, page):
        super().__init__(page, page.locator("#header"))
        self.input_search = page.locator("#edit-search")
        self.button_search = page.locator("#edit-submit-search-result")

    def get_search_input(self):
        return self.input_search

    def click_search_input(self):
        self.get_search_input().click()

    def fill_name_product(self, text: str):
        self.input_search.fill(text)

    def click_button_search(self):
        self.button_search.click()

    def get_search_input_value(self):
        return self.input_search.input_value()

    def clear_search_input(self):
        self.input_search.clear()

    def get_cart(self):
        return Cart(self.page, self.wrapper)

    def get_button_cart(self):
        return Cart(self.page, self.wrapper).get_button_cart_locator()