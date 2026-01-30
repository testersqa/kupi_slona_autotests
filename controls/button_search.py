from controls.base_control import BaseControl


class ButtonSearch(BaseControl):
    def __init__(self, page):
        super().__init__(page)
        self.button_search = page.locator("#edit-submit-search-result")
