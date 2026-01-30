from components.base_component import BaseComponent
from controls.button_search import ButtonSearch
from controls.input_search import InputSearch
from controls.cart import Cart


class HeaderComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.input_search = page.locator("#edit-search")
        self.button_search = page.locator("#edit-submit-search-result")
        self.header = page.locator("#header")

    def click_search_input(self):
        self.input_search.click()

    def fill_name_product(self, text: str):
        self.input_search.fill(text)

    def click_button_search(self):
        self.button_search.click()

    def get_search_input_value(self):
        return self.input_search.input_value()

    def clear_search_input(self):
        self.input_search.clear()

    def get_cart(self):
        return Cart(self.page)

    def get_button_cart(self):
        return Cart(self.page).get_button_cart_locator()