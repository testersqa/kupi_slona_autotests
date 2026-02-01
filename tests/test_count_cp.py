import allure
from playwright.sync_api import expect
from pages.pens_pencils_page import WritingProductPage


def test_cart_product(page):
    main = WritingProductPage(page, "https://kupislona-store.ru/katalog/ruchki-karandashi-markery")
    main.open()
    main.fill_count('Автоматическая ручка «Bang cat»', "1234567890")

    product = main.get_product_by_title('Автоматическая ручка «Bang cat»').get_input_count().wrapper()
    expect(product).to_be_editable()
    expect(product).to_have_value("123456")







