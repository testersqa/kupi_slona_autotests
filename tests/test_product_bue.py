import allure

from playwright.sync_api import expect, Page

from conftest import page
from pages.pens_pencils_page import WritingProductPage



@allure.title("Покупка товара с количеством 0")
def test_buy_product_with_zero_quantity(page):
    hunters_notebook = WritingProductPage(page, "https://kupislona-store.ru/katalog/all")

    with allure.step("Шаг 1: Открыть сайт https://kupislona-store.ru/katalog/all"):
        hunters_notebook.open()
        expect(page).to_have_title("| Купи слона - Магазины классных вещиц")

    with allure.step("Шаг 2: Под товаром «Блокнот «Охотник»» очистить поле ввода количества товаров"):
        hunters_notebook.fill_count('Блокнот «Охотник»', "")
        locator_input = hunters_notebook.get_product_by_title('Блокнот «Охотник»').get_input_count().locator()
        expect(locator_input).to_have_value("")

    with allure.step("Шаг 3: ввести значение «0» в поле количество товаров"):
        hunters_notebook.fill_count('Блокнот «Охотник»', "0")
        locator_input = hunters_notebook.get_product_by_title('Блокнот «Охотник»').get_input_count().locator()
        expect(locator_input).to_have_value("0")

    with allure.step("Шаг 4: Нажать кнопку «купить»"):
        hunters_notebook.get_product_by_title('Блокнот «Охотник»').click_button_buy()
        page.wait_for_timeout(2000)
        error_locator = page.locator('.messages.error')
        expect(error_locator).to_contain_text('Сообщение об ошибке')

