from components.base_component import BaseComponent
from controls.input_count import InputCount
from controls.button_buy import ButtonBuy


class CartProduct(BaseComponent):
    def __init__(self, page, title):
        super().__init__(page)
        self.title = title
        self.locator = page.locator(f'//a[contains(text(), "{self.title}")]/ancestor::li')

    # def wrapper(self):
    #     return self.page.locator(f'//a[contains(text(), "{self.title}")]/ancestor::li')

    def get_input_count(self):
        return InputCount(self.locator)

    def fill_input_count_by_title(self, count):
        self.get_input_count().locator_count.fill(count)

    def get_button_buy(self):
        return ButtonBuy(self.locator)

    def click_button_buy(self):
        self.get_button_buy().locator_button.click()
