import allure

from playwright.sync_api import expect, Page

from conftest import page
from pages.product_buy_page import ProductBuePage


@allure.title("Покупка товара с количеством 0")
def test_buy_product_with_zero_quantity(page):
    product = ProductBuePage(page, "https://kupislona-store.ru/katalog/all")

    with allure.step("Открытие страницы https://kupislona-store.ru/katalog/all"):
        product.open()

    with allure.step("Установить количество товара на 0"):
        product.set_quantity("0")

    with allure.step("Нажать кнопку 'Купить'"):
        product.click_buy_button()
