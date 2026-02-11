from pages.base_page import BasePage


class PageSearchProduct(BasePage):
    """Страница с результатами поиска"""
    def __init__(self, page, url):
        super().__init__(page, url)
        self.cards_product = page.locator('.item-list li')
        self.page_title = page.locator('h1.title')

    def get_page_title(self):
        return self.page_title.text_content().strip()

    def get_url(self):
        return self.page.url

    def get_count_card_product(self):
        return self.cards_product.count()

