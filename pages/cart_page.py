from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        self.url = "https://kupislona-store.ru/cart"
        super().__init__(page, self.url)

    def get_title(self):
        return self.page.locator("h1")

    def get_message_empty_cart(self):
        return self.page.locator("#cart-form-pane")