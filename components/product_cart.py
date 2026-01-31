from components.base_component import BaseComponent
from controls.input_count import InputCount


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