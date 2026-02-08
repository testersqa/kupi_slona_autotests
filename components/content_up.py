from components.base_component import BaseComponent

class ContentUp(BaseComponent):
    def __init__(self, page, title):
        super().__init__(page, page.locator('.menu.clearfix'))
        self.title = title

    def get_menu_by_title(self):
        return self.page.get_by_role('link', name=f'{self.title}')

