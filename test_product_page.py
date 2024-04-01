import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.delivery_page import DeliveryPage


def test_check_phone_number(browser):
    link = "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1"
    page = CatalogPage(browser, link)
    page.open()
    page.user_authorization()
    page.product_selection()
    all_windows = browser.window_handles
    # Переключаемся на новую вкладку
    browser.switch_to.window(all_windows[1])
    page = ProductPage(browser, browser.current_url)
    page.purchase_of_goods_with_delivery()
    page = DeliveryPage(browser, browser.current_url)
    page.phone_number_field_validation()
