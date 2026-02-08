import allure
from playwright.sync_api import expect, Page
from pages.element_page import ElemPage

@allure.title("Верный переход по разделам в верхнего меню хэдере")
def test_transfer_menu_up(page: Page):
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

@allure.title("Автотест меню")
@allure.description("Нажатие на кнопку Магазины")
def test_has_title(page: Page):
    menu = ElemPage(page, "https://kupislona-store.ru/")

    with allure.step("Открытие главной страницы"):
        menu.open()
        expect(page).to_have_title(" «Купи слона» — интернет-магазин необычных подарков и милой канцелярии. Доставка по Москве и России.")

    with allure.step("Нажатие на кнопку Магазины"):
        menu.click_menu_up_by_title("Магазины")
        expect(page).to_have_url("https://kupislona-store.ru/content/adresa-magazinov")
