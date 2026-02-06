import re
import allure
from components.menu_component import MenuComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


@allure.title("Автотест меню")
@allure.description("Нажатие на кнопку Магазины")
def test_has_title(page: Page):
    base_page = BasePage(page, "https://kupislona-store.ru/")
    main_menu = MenuComponent(page)

    with allure.step("Открытие главной страницы"):
        page.set_default_timeout(10000)
        base_page.open()
        expect(page).to_have_title(" «Купи слона» — интернет-магазин необычных подарков и милой канцелярии. Доставка по Москве и России.")

    with allure.step("Нажатие на кнопку Магазины"):
        main_menu.click_button()
        expect(page).to_have_url("https://kupislona-store.ru/content/adresa-magazinov")