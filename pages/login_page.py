import allure
import pytest
from pages.base_page import BasePage
from config.links import Links
from elements.button import BaseElement, Button
from locators.locs_login_page import LoginPageLocators


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.create_account_link = Button(self.browser, 'Создать аккаунт', *LoginPageLocators.CREATE_ACCOUNT_LINK)

    def go_to_create_account_page(self):
        self.create_account_link.click()