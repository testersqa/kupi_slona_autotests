import allure
from playwright.sync_api import Page, expect
from pages.page_all_catalog import PageAllCategory
from pages.base_page import BasePage
from components.header_menu import HeaderMenu
from pages.cart_page import CartPage


@allure.title("Тестирование кнопки Купить")
@allure.description("Успешное добавление товара Блокнот 'Охотник' в корзину")
def test_click_button_buy(page: Page):
    base_page = BasePage(page, "https://kupislona-store.ru/")
    page_all_catalog = PageAllCategory(page, "https://kupislona-store.ru/katalog/all")
    cart_page = CartPage(page, "https://kupislona-store.ru/cart")
    header_menu = HeaderMenu(page, )
    name_category = "Весь каталог"
    name_product = 'Блокнот «Охотник»'

    with allure.step("Открытие главной страницы сайта."):
        base_page.open()
        expect(page).to_have_url("https://kupislona-store.ru/")

    with allure.step("Клик по категории в каталоге"):
        header_menu.click_name_catalog(name_category)
        expect(page).to_have_url("https://kupislona-store.ru/katalog/all")

        assert page_all_catalog.get_title_text() == "Весь каталог"
        page.wait_for_timeout(2000)

        page.mouse.wheel(0, 250)
        page.wait_for_timeout(1000)

    with allure.step("Клик по кнопке Купить, в карточке товара: Блокнот 'Охотник'"):
        page_all_catalog.click_button_buy(name_product)
        page.wait_for_timeout(2000)
        message = page.locator('.messages.status')
        expect(message).to_contain_text("добавлен в корзину")

    with allure.step("Переход в корзину "):
        page.goto("https://kupislona-store.ru/cart")
        expect(page).to_have_url("https://kupislona-store.ru/cart")
        expect(cart_page.get_title()).to_have_text("Корзина")
        page.wait_for_timeout(1000)

    with allure.step("Проверка добавленного товара"):
        product_in_cart = cart_page.get_product_name_in_cart(name_product)
        expect(product_in_cart).to_be_visible()

        quantity = cart_page.get_product_quantity(name_product)
        assert quantity == "1", f"Ожидалось количество 1, но было {quantity}"
