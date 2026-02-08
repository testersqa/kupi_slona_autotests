from pages.base_page import BasePage


class ProductBuePage(BasePage):
    '''
    Страница Весь каталог
    '''
    def __init__(self, page, url):
        super().__init__(page, url)

    def open(self):
        self.page.goto(self.url)

    def get_product_by_title(self, title):
        return self.page.locator("#block-system-main").get_by_role("link", name=title)

    def set_quantity(self, quantity: str):
        self.page.locator('#edit-qty--2').fill(quantity)

    def click_buy_button(self):
        self.page.locator("#edit-submit-17104").click()

