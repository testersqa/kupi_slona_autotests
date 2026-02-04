from controls.base_control import BaseControl


class ProductBuy(BaseControl):
    def __init__(self, page, title):
        self.title = title
        super().__init__(page, page.get_by_role('link', name=f'{self.title}'))