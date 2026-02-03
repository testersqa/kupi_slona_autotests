from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from controls.product_buy import ProductBuy


class ProductComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.driver = page

    def wrapper(self):
        return self.page.locator('//*[@class = "block block-system"]')

    def get_product_by_title(self, title):
        return ProductBuy(self.page, title).wrapper()