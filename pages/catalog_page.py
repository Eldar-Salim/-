import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import CatalogPageLocators
from .personal_data import *


class CatalogPage(BasePage):
    def user_authorization(self):
        login_button = self.browser.find_element(*CatalogPageLocators.LOGIN_BUTTON)
        login_button.click()
        login = self.browser.find_element(*CatalogPageLocators.LOGIN)
        login.send_keys(Login)
        password = self.browser.find_element(*CatalogPageLocators.PASSWORD)
        password.send_keys(Password)
        checkbox_remember_password = self.browser.find_element(*CatalogPageLocators.CHECKBOX_REMEMBER_USER)
        checkbox_remember_password.click()
        button_submit = self.browser.find_element(*CatalogPageLocators.BUTTON_SUBMIT)
        button_submit.click()
        # Пауза для ручного ввода капчи/кода из смс
        time.sleep(30)

    def product_selection(self):
        product_selection = self.browser.find_element(*CatalogPageLocators.PRODUCT_SELECTION)
        product_selection.click()
