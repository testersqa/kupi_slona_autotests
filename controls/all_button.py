from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class AllButton(BaseControl):
    """Класс для всех кнопок"""
    def __init__(self, page: Page,
                 paren_wrapper: Locator,
                 self_wrapper_path='input[value="Купить"]'):
        super().__init__(page, paren_wrapper.locator(self_wrapper_path))
