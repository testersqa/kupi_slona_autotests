from components.base_component import BaseComponent
from control.menu_content_up import MenuContent

class ContentUp(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        self.driver = page

    def wrapper(self):
        return self.page.locator('//*[@class = "menu clearfix"]')

    def get_menu_by_title(self, title):
        return MenuContent(self.page, title).wrapper()


