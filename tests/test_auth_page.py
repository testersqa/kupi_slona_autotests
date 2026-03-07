from playwright.sync_api import expect

from pages.auth_page import AuthPage


def test_invalid_auth(page):
    auth_page = AuthPage(page)
    auth_component = auth_page.get_auth_component()

    auth_page.open()
    auth_component.enter_username('not_exists_user')
    page.wait_for_timeout(500)
    expect(auth_component.get_username_input_wrapper()).to_have_value('not_exists_user')

    auth_component.enter_password('random_password')

    expect(auth_component.get_password_input_wrapper()).to_have_value('random_password')

    auth_component.click_login_button()
    page.wait_for_timeout(1000)

    expect(auth_component.get_login_button_wrapper()).to_be_visible()
    expect(auth_component.get_login_button_wrapper()).to_be_enabled()
    expect(auth_component.page.locator('.messages.error')).to_have_text('Извините, это имя пользователя или пароль неверны')