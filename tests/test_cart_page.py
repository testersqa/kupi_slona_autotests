import allure
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.home_page import HomePage


@allure.title("Тестирование корзины")
@allure.description("Проверка отображения пустой корзины и перехода на страницу корзины")
def test_cart_page(page):
    home_page = HomePage(page)
    cart_page = CartPage(page)

    with allure.step("Открыть сайт https://kupislona-store.ru"):
        home_page.open_home_page()

    expect(home_page.get_header().get_cart().get_cart_count_value()).to_have_value("0")

    with allure.step("В хедере нажать на иконку корзины"):
        home_page.click_button_cart()

    expect(page).to_have_url("https://kupislona-store.ru/cart")
    expect(cart_page.get_title()).to_have_text("Корзина")
    expect(cart_page.get_message_empty_cart()).to_have_text("В Вашей корзине нет товаров.")