from controls.base_control import BaseControl


class ButtonBuy(BaseControl):
    def __init__(self, page):
        super().__init__(page, page.locator('input[value="Купить"]'))
