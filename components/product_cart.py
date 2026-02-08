from components.base_component import BaseComponent
from controls.input_count import InputCount
from controls.all_button import AllButton


class CartProduct(BaseComponent):
    def __init__(self, page, title):
        self.title = title
        super().__init__(page, page.locator(f'//a[contains(text(), "{self.title}")]/ancestor::li'))

    def get_input_count(self):
        return InputCount(self.page, self.wrapper)

    def fill_input_count_by_title(self, count):
        self.get_input_count().wrapper.fill(count)

    def get_button_buy(self):
        return AllButton(self.page, self.wrapper)

    def click_button_buy(self):
        self.get_button_buy().wrapper.click()
