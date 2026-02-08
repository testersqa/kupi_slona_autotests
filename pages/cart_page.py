from pages.base_page import BasePage


class CartPage(BasePage):
    '''
    Страница корзины
    '''
    def __init__(self, page):
        self.url = "https://kupislona-store.ru/cart"
        super().__init__(page, self.url)

    def get_title(self):
        return self.page.locator("h1")

    def get_message_empty_cart(self):
        return self.page.locator("#cart-form-pane")

    def get_product_name_in_cart(self, product_name: str):
        return self.page.locator(f"tr:has-text('{product_name}')")

    def get_product_quantity(self, product_name):
        product_date = self.get_product_name_in_cart(product_name)
        count_input = product_date.locator('input[name*="qty"]')
        return count_input.get_attribute("value")
