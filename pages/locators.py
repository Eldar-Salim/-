from selenium.webdriver.common.by import By


class CatalogPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a.index-module-login-K8jzD")
    LOGIN = (By.CSS_SELECTOR, "[name='login']")
    PASSWORD = (By.CSS_SELECTOR, "[name='password']")
    CHECKBOX_REMEMBER_USER = (By.CSS_SELECTOR, "[name='checkbox-checked']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "[name='submit']")
    PRODUCT_SELECTION = (By.XPATH, "//div[contains(@class, 'delivery-root-LFKPq')]/ancestor::div[contains(@class, 'styles-responsive-m3Vnz')]")


class ProductPageLocators():
    BUTTON_BUY_WITH_DELIVERY = (By.CSS_SELECTOR, "[data-marker='delivery-item-button-main']")


class DeliveryPageLocators():
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, " [name='phone'] ")
