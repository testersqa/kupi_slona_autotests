from pages.base_page import BasePage
from components.product_cart import CartProduct


class PageAllCategory(BasePage):
    """ Страница весь каталог ищет товар на странице по названию """
    def __init__(self, page, url):
        super().__init__(page, url)
        self.page_title = page.locator("#page-title")

    def get_title_text(self):
        return self.page_title.text_content()

    def get_product_by_title(self, name_product):
        return CartProduct(self.page, name_product)

    def click_button_buy(self, name_product):
        product = self.get_product_by_title(name_product)
        product.click_button_buy()
