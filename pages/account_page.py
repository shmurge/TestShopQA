import allure
from selenium.webdriver.support import expected_conditions as EC
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from pages.header_page import HeaderPage
from config.links import Links
from locators.locs_account_page import AccountPageLocators


class AccountPage(HeaderPage):
    PAGE_URL = Links.ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.username = BaseElement(self.browser, 'Имя пользователя', *AccountPageLocators.USERNAME)
        self.user_email = BaseElement(self.browser, 'Email', *AccountPageLocators.USER_EMAIL)

    def user_information_is_correct(self, username, user_email):
        with allure.step('Информация о пользователе корректна'):
            self.check_username(username)
            self.check_user_email(user_email)

    def check_username(self, exp):
        with allure.step(f'{self.username.name} соответствует'):
            act = self.username.get_text_of_element().strip()

            self.base_assertions.assert_data_equal_data(act, exp)

    def check_user_email(self, exp):
        with allure.step(f'{self.user_email.name} соответствует'):
            act = self.user_email.get_text_of_element().strip()

            self.base_assertions.assert_data_equal_data(act, exp)