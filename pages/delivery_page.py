from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import DeliveryPageLocators


class DeliveryPage(BasePage):
    def phone_number_field_validation(self):
        phone_number_field = self.browser.find_element(*DeliveryPageLocators.PHONE_NUMBER_FIELD)
        Value_phone_number = phone_number_field.get_attribute("value")
        assert Value_phone_number == "", 'Поле номера телефона не пустое'
