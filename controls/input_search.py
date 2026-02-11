from controls.base_control import BaseControl


class InputSearch(BaseControl):
    """Ввод поиска товара"""
    def __init__(self, page):
        super().__init__(page, page.locator("#edit-search"))
