from controls.base_control import BaseControl


class InputSearch(BaseControl):
    def __init__(self, page):
        super().__init__(page)
        self.locator_input = page.locator("#edit-search")
