import time

import allure
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.page_search_product import PageSearchProduct
from components.header_component import HeaderComponent


def test_search_input(page: Page):
    text = 'ывдмтав'
    home_page = HomePage(page, "https://kupislona-store.ru/")
    header = home_page.get_header()
    seacrh_field = header.get_search_input()

    home_page.open()
    header.click_search_input()

    expect(seacrh_field).to_be_focused()
    home_page.get_header().fill_name_product(text)

    expect(seacrh_field).to_have_value(text)
    home_page.get_header().click_button_search()
    time.sleep(1)

    expect(page.locator('#block-system-main').get_by_text('Ничего не найдено')).to_be_visible()
    expect(page.locator('#page-title')).to_have_text('Результат поиска')