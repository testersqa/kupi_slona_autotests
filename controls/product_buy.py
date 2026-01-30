from controls.base_control import BaseControl


class ProductBuy(BaseControl):
    def __init__(self, page, title):
        super().__init__(page)
        self.page = page
        self.title = title

    def wrapper(self):
        return self.page.get_by_role('link', name=f'{self.title}')