import allure
import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.page_search_product import PageSearchProduct
from components.header_component import HeaderComponent


@allure.title("Тестирование поля поиска")
@allure.description("Поиск товара с корректным названием")
def test_search_product(page: Page):
    base_page = BasePage(page, "https://kupislona-store.ru/")
    page_search_product = PageSearchProduct(page, "https://kupislona-store.ru/search-result?search=%D0%91%D0%BB%D0%BE"
                                                  "%D0%BA%D0%BD%D0%BE%D1%82%20green")
    header = HeaderComponent(page)
    product_name = "Блокнот green"

    with allure.step("Открытие главной страницы сайта."):
        base_page.open()

    with allure.step("Клик по полю ввода"):
        header.click_search_input()

    with allure.step("Ввод названия продукта"):
        header.fill_name_product(product_name)
        page.wait_for_timeout(2000)
        expect(header.input_search).to_have_value(product_name)

    with allure.step("Нажатие кнопки поиска"):
        header.click_button_search()
        page.wait_for_timeout(2000)

    with allure.step("Проверка изменения URL"):
        search_pattern = re.compile(r'search', re.IGNORECASE)
        green_pattern = re.compile(r'green', re.IGNORECASE)

        expect(page).to_have_url(search_pattern)
        expect(page).to_have_url(green_pattern)

        page.wait_for_timeout(2000)
        page.mouse.wheel(0, 250)
        page.wait_for_timeout(1000)

    with allure.step("Получение карточки товаров"):
        page_search_product.get_count_card_product()

    with allure.step("Проверка заголовка страницы"):
        actual_title = "Результат поиска"
        assert page_search_product.get_page_title() == actual_title


# pytest --alluredir test_results
# allure serve test_results
# allure generate
