import allure
from playwright.sync_api import expect
from pages.element_page import ElemPage

@allure.title("Верный переход по разделам в верхнего меню хэдере")
def test_transfer_menu_up(page):
    menu = ElemPage(page, "https://kupislona-store.ru/")

    with allure.step("Открытие страницы https://kupislona-store.ru/"):
        menu.open()

    with allure.step("Нажать на раздел «Контакты» в верхнем меню"):
        menu.click_menu_up_by_title("Контакты")

    expect(page).to_have_url("https://kupislona-store.ru/content/kontakty")
    expect(page.locator("h1")).to_have_text("Контакты")

    with allure.step("Нажать на логотип «Купи слона»"):
        menu.click_by_logo()

    expect(page).to_have_url("https://kupislona-store.ru/")
    expect(page.get_by_text("прикольный подарок для девушки или своего друга")).to_be_visible()

