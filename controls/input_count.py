from controls.base_control import BaseControl


class InputCount(BaseControl):
    def __init__(self, page):
        super().__init__(page, page.locator('//*[contains(@id, "edit-qty")]'))

    def locator(self):
        return self.wrapper

    def get_input_value(self):
        return self.wrapper.input_value()