import allure
import pytest

from elements.input import Input
from pages.header_page import HeaderPage
from config.links import Links
from elements.base_element import BaseElement
from elements.button import Button
from locators.locs_login_page import LoginPageLocators


class LoginPage(HeaderPage):
    PAGE_URL = Links.LOGIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.login_form = BaseElement(self.browser, 'Форма логина', *LoginPageLocators.LOGIN_FORM)
        self.email_input = Input(self.browser, 'Email', *LoginPageLocators.EMAIL_INPUT)
        self.password_input = Input(self.browser, 'Пароль', *LoginPageLocators.PASSWORD_INPUT)
        self.login_button = Button(self.browser, 'Войти', *LoginPageLocators.LOGIN_BUTTON)
        self.create_account_link = Button(self.browser, 'Создать аккаунт', *LoginPageLocators.CREATE_ACCOUNT_LINK)
        self.alert = BaseElement(self.browser, 'Алерт', *LoginPageLocators.ALERT)

    def login_form_is_displayed(self):
        with allure.step(f'{self.login_form.name} отображается'):
            assert self.login_form.is_visible(), f'{self.login_form.name}не отображается!'

    def go_to_create_account_page(self):
        with allure.step('Перейти на страницу создания аккаунта'):
            self.create_account_link.click()

    def fill_email_input(self, email):
        with allure.step(f'Заполнить {self.email_input.name}'):
            self.email_input.fill_input(email)

    def fill_password_input(self, password):
        with allure.step(f'Заполнить {self.password_input.name}'):
            self.password_input.fill_input(password)

    def click_on_login_button(self):
        with allure.step(f'Кликнуть по {self.login_button.name}'):
            self.login_button.click()

    def fill_login_form(self, login, password):
        with allure.step(f'Заполнить {self.login_form.name}'):
            self.fill_email_input(login)
            self.fill_password_input(password)
            self.click_on_login_button()

    def should_be_correct_placeholders_in_login_form(self, email_placeholder, password_placeholder):
        with allure.step(f'Проверить плэйсхолдер: {self.email_input.name}'):
            self.email_input.check_placeholder(email_placeholder)
        with allure.step(f'Проверить плэйсхолдер: {self.password_input.name}'):
            self.password_input.check_placeholder(password_placeholder)

    def error_alert_is_displayed(self, exp_alert):
        with allure.step(f'{self.alert.name} отображается'):
            act_alert = self.alert.get_text_of_element().strip()

            self.base_assertions.assert_data_equal_data(act_alert, exp_alert)
