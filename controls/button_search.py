from controls.base_control import BaseControl


class ButtonSearch(BaseControl):
    """Контрол- лупа для поиска товара"""
    def __init__(self, page):
        super().__init__(page, page.locator("#edit-submit-search-result"))
