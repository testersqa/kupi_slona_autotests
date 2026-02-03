from components.product_component import ProductComponent
from pages.base_page import BasePage


class ProductBuePage(BasePage):
    def __init__(self, page, url):
        super().__init__(page, url)
        self.page = page
        self.url = url


    def open(self):
        self.page.goto(self.url)

    def get_product_by_title(self, title):
        return self.page.locator('//*[@id="block-system-main"]').get_by_role("link", name=title)

    def set_quantity(self):
        qty_input_locator = self.page.locator('#edit-qty--2')
        qty_input_locator.fill("")

    def set_quantity0(self, quantity: str):
        qty_input_locator = self.page.locator('#edit-qty--2')
        qty_input_locator.fill(quantity)

    def click_buy_button(self):
        buy_button_locator = self.page.locator("#edit-submit-17091")
        buy_button_locator.click()

