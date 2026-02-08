from playwright.sync_api import Page, Locator

from controls.base_control import BaseControl


class Cart(BaseControl):
    def __init__(self, page: Page,
                 paren_wrapper: Locator):
        super().__init__(page, paren_wrapper.locator("#block-uc-ajax-cart-delta-0"))

    def get_button_cart_locator(self):
        return self.page.locator("img.cart_icon")

    def get_cart_count_value(self):
        return self.page.locator("label")
