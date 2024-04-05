from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators
import allure


class ProductPage(BasePage):
    def purchase_of_goods_with_delivery(self):
        with allure.step("Купить товар с доставкой"):
            try:
                button_buy_with_delivery = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located(ProductPageLocators.BUTTON_BUY_WITH_DELIVERY))
                button_buy_with_delivery.click()
            except StaleElementReferenceException:
                browser.refresh()
                button_buy_with_delivery = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located(ProductPageLocators.BUTTON_BUY_WITH_DELIVERY))
                button_buy_with_delivery.click()
