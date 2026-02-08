from components.base_component import BaseComponent
from controls.input_count import InputCount
from controls.button_buy import ButtonBuy


class CartProduct(BaseComponent):
    def __init__(self, page: Page, title: str):
        self.title: str = title
        super().__init__(page, page.locator(f'//a[contains(text(), "{self.title}")]/ancestor::li'))

    # def wrapper(self):
    #     return self.page.locator(f'//a[contains(text(), "{self.title}")]/ancestor::li')

    def get_input_count(self):
        return InputCount(self.wrapper)

    def fill_input_count_by_title(self, count):
        return self.get_input_count().wrapper.fill(count)

    def get_button_buy(self):
        return ButtonBuy(self.wrapper)

    def click_button_buy(self):
        self.get_button_buy().wrapper.click()
