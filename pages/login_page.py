import allure
import pytest
from pages.header_page import HeaderPage
from config.links import Links
from elements.button import BaseElement, Button
from locators.locs_login_page import LoginPageLocators


class LoginPage(HeaderPage):
    PAGE_URL = Links.LOGIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.login_form = BaseElement(self.browser, 'Форма логина', *LoginPageLocators.LOGIN_FORM)
        self.create_account_link = Button(self.browser, 'Создать аккаунт', *LoginPageLocators.CREATE_ACCOUNT_LINK)

    def login_page_is_displayed(self):
        with allure.step('Страница логина отображается'):
            assert self.login_form.is_visible(), 'Страница логина не отображается!'

    def go_to_create_account_page(self):
        self.create_account_link.click()