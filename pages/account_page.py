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

    def contact_information_is_displayed(self):
        with allure.step('Отображается контактная информация'):
            self.username.is_visible()
            self.user_email.is_visible()
