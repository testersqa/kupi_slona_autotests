from components.base_component import BaseComponent
from controls.product_buy import ProductBuy


class ProductComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page, page.locator('.block block-system'))

    def get_product_by_title(self, title):
        return ProductBuy(self.page, title)