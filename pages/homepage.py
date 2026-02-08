# from pages.base_page import BasePage
#
#
# class HomePage(BasePage):
#     def __init__(self, page):
#         super().__init__(page)
#         self.menu = page.locator('.menu_icon.menu-883')
#         self.page_title = page.locator('.h2.title')
#
#     def get_page_title(self):
#         return self.page_title.text_content().strip()
#
#     def get_url(self):
#         return self.page.url
#
#     def get_count_menu(self):
#         return self.menu.count()
#
#
#
#
