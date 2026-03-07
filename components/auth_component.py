from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.input_control import InputControl
from controls.button_control import ButtonControl


class AuthComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self.__username_input = InputControl(self.page, self.wrapper.locator('[name="name"]'))
        self.__password_input = InputControl(self.page, self.wrapper.locator('[name="pass"]'))
        self.__login_button = ButtonControl(self.page, self.wrapper.locator('[name="op"]'))

    def get_username_input_wrapper(self):
        return self.__username_input.wrapper

    def get_password_input_wrapper(self):
        return self.__password_input.wrapper

    def get_login_button_wrapper(self):
        return self.__login_button.wrapper

    def enter_username(self, username):
        self.__username_input.clear_and_fill(username)

    def enter_password(self, password):
        self.__password_input.clear_and_fill(password)

    def click_login_button(self):
        self.__login_button.click_anyway()