from components.base_component import BaseComponent
from controls.menu_content_up import MenuContent

class ContentUp(BaseComponent):
    def __init__(self, page):
        super().__init__(page, page.locator('.menu.clearfix'))

    def get_menu_by_title(self, title):
        return MenuContent(self.page, title)

    # f"a:has-text('{title}')"


