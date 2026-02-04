from controls.base_control import BaseControl


class ButtonBuy(BaseControl):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.locator_button = page.locator('input[value="Купить"]')

    def click(self):
        self.locator_button.click()
