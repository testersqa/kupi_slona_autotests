from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class InputCount(BaseControl):
    '''
    Берёт инпут в каждой карточки товара
    '''
    def __init__(self, page: Page,
                 paren_wrapper: Locator):
        super().__init__(page, paren_wrapper.locator('[id*="edit-qty"]'))

