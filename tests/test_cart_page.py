import allure
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.home_page import HomePage


@allure.title("Тестирование корзины")
@allure.description("Проверка отображения пустой корзины и перехода на страницу корзины")
def test_cart_page(page):
    home_page = HomePage(page, "https://kupislona-store.ru/")
    cart_page = CartPage(page, "https://kupislona-store.ru/cart")

    with allure.step("Открыть сайт https://kupislona-store.ru"):
        home_page.open()

        expect(home_page.get_header().get_quantity_in_cart()).to_have_text("0")

    with allure.step("В хедере нажать на иконку корзины"):
        home_page.click_button_cart()

        expect(page).to_have_url("https://kupislona-store.ru/cart")
        expect(cart_page.get_title()).to_have_text("Корзина")
        expect(cart_page.get_message_empty_cart()).to_have_text("В Вашей корзине нет товаров.")