from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent

class ContentUp(BaseComponent):
    '''
    Класс верхнего меню на сайте. Метод получает название меню по названию
    '''
    def __init__(self, page: Page,
                 parent_wrapper: Locator,
                 title):
        self.title = title
        super().__init__(page, parent_wrapper.locator('.menu.clearfix'))


    def get_menu_by_title(self):
        return self.wrapper.get_by_role('link', name=f'{self.title}')

