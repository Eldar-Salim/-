import pytest
from selenium import webdriver
import allure


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        with allure.step("Открыть страницу"):
            self.browser.get(self.url)
