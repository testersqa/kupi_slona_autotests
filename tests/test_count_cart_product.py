import allure
from playwright.sync_api import expect
from pages.pens_pencils_page import WritingProductPage

@allure.title("Максимальное количество товара, которое можно указать в каталоге")
@allure.description("В количество у карточки товара вводиться только 6 символов")
def test_cart_product_count(page):
    main = WritingProductPage(page, "https://kupislona-store.ru/katalog/ruchki-karandashi-markery")
    with allure.step('Открыть страницу "Ручки, карандаши, маркеры"'):
        main.open()
    with allure.step('У товара "Автоматическая ручка «Bang cat»" ввести количество 1234567890'):
        main.fill_count('Автоматическая ручка «Bang cat»', "1234567890")

    product = main.get_product_by_title('Автоматическая ручка «Bang cat»').get_input_count().wrapper

    expect(product).to_be_editable()
    expect(product).to_have_value("123456")
