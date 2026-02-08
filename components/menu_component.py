# from components.base_component import BaseComponent
#
#
# class MenuComponent(BaseComponent):
#     '''
#     Класс меню с разделами категорий на сайте. Метод получает название меню по названию
#     '''
#     def __init__(self, page):
#         super().__init__(page, page.locator(".menu clearfix"))
#         self.button_search = page.locator(".menu_icon.menu-883")
#
#     def click_button(self):
#         self.button_search.click()
#
