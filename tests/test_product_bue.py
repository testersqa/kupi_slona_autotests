import allure

from playwright.sync_api import expect, Page

from conftest import page
from pages.product_buy_page import ProductBuePage


@allure.title("Покупка товара с количеством 0")
def test_buy_product_with_zero_quantity(page):
    product = ProductBuePage(page, "https://kupislona-store.ru/katalog/all")

    with allure.step("Шаг 1: Открыть сайт https://kupislona-store.ru/katalog/all"):
        product.open()
        expect(page).to_have_title("| Купи слона - Магазины классных вещиц")

    with allure.step("Шаг 2: Под товаром «Блокнот «Охотник»» очистить поле ввода количества товаров"):
        product.set_quantity()
        locator = page.locator("#edit-qty--2")
        expect(locator).to_have_value("")

    with allure.step("Шаг 3: ввести значение «0» в поле количество товаров"):
        product.set_quantity0("0")
        locator = page.locator("#edit-qty--2")
        expect(locator).to_have_value("0")

    with allure.step("Шаг 4: Нажать кнопку «купить»"):
        product.click_buy_button()
        locator = page.locator(".messages.error")
        expect(locator).to_be_visible(timeout=5000)
        expect(locator).to_contain_text("Сообщение об ошибке")
