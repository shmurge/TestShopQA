import allure
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_account_page import AccountPageLocators
from pages.header_page import HeaderPage


class AccountPage(HeaderPage):
    PAGE_URL = Links.ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.my_account_header = BaseElement(self.browser, 'Мой аккаунт', *AccountPageLocators.MY_ACCOUNT_HEADER)
        self.username_in_account = BaseElement(self.browser, 'Имя пользователя', *AccountPageLocators.USERNAME)
        self.user_email_in_account = BaseElement(self.browser, 'Email', *AccountPageLocators.USER_EMAIL)

    def account_page_is_displayed(self):
        with allure.step(f'Отображается {self.my_account_header.name}'):
            assert self.my_account_header.is_visible(), (f'Станица аккаунта не отображается\n'
                                                         f'Скриншот'
                                                         f'{self.attach_screenshot(self.my_account_header.name)}')

    def user_information_is_correct(self, username, user_email):
        with allure.step('Информация о пользователе корректна'):
            self.check_username(username)
            self.check_user_email(user_email)

    def check_username(self, exp):
        with allure.step(f'{self.username_in_account.name} в профиле корректное'):
            act = self.username_in_account.get_text_of_element()

            assert act == exp, (f'Некорректное имя пользователя в профиле\n'
                                f'ОР: {exp}\n'
                                f'ФР: {act}\n'
                                f'Скриншот {self.attach_screenshot(self.username_in_account.name)}')

    def check_user_email(self, exp):
        with allure.step(f'{self.user_email_in_account.name} в профиле корректный'):
            act = self.user_email_in_account.get_text_of_element()

            assert act == exp, (f'Некорректный Email в профиле\n'
                                f'ОР: {exp}\n'
                                f'ФР: {act}\n'
                                f'Скриншот {self.attach_screenshot(self.user_email_in_account.name)}')
