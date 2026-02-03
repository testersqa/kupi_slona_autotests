from controls.base_control import BaseControl


class Cart(BaseControl):
    def __init__(self, page):
        super().__init__(page)
        self.cart_locator = page.locator("#block-uc-ajax-cart-delta-0")

    def get_button_cart_locator(self):
        return self.cart_locator.locator("img.cart_icon")

    def get_cart_count_value(self):
        return self.cart_locator.locator("label")

    # def get_product_in_cart(self, product_name: str):
    #     return self.page.locator(f".cart-item:has-text('{product_name}')")
