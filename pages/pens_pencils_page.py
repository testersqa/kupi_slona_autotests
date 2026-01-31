from pages.base_page import BasePage
from components.product_cart import CartProduct

class WritingProductPage(BasePage):
    def __init__(self, page, url):
        super().__init__(page, url)


    def get_product_by_title(self, title):
        return CartProduct(self.page, title)

    def fill_count(self, title, count):
      return self.get_product_by_title(title).fill_input_count_by_title(count)
