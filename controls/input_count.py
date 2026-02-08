from controls.base_control import BaseControl


class InputCount(BaseControl):
    def __init__(self, page):
        super().__init__(page, page.locator('[id*="edit-qty"]'))

