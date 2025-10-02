import allure
import pytest
from time import sleep

from config.links import Links
from elements.input import Input
from elements.base_element import BaseElement
from elements.button import Button
from locators.locs_login_page import LoginPageLocators
from pages.header_page import HeaderPage


class LoginPage(HeaderPage):
    PAGE_URL = Links.LOGIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.login_form = BaseElement(self.browser, 'Форма авторизации', *LoginPageLocators.LOGIN_FORM)
        self.email_input = Input(self.browser, 'Email', *LoginPageLocators.EMAIL_INPUT)
        self.password_input = Input(self.browser, 'Пароль', *LoginPageLocators.PASSWORD_INPUT)
        self.login_button = Button(self.browser, 'Войти', *LoginPageLocators.LOGIN_BUTTON)
        self.create_account_link = Button(self.browser, 'Создать аккаунт', *LoginPageLocators.CREATE_ACCOUNT_LINK)
        self.alert = BaseElement(self.browser, 'Алерт', *LoginPageLocators.ALERT)

    def login_form_is_displayed(self):
        with allure.step(f'{self.login_form.name} отображается'):
            assert self.login_form.is_visible(), (f'{self.login_form.name} не отображается!\n'
                                                  f'Скриншот {self.attach_screenshot(self.login_form.name)}')

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

    def should_be_correct_placeholders_in_login_form(self, exp_email_placeholder, exp_password_placeholder):
        with allure.step(f'Проверить плэйсхолдеры в {self.login_form.name}'):
            act_email_placeholder = self.email_input.get_placeholder()
            act_password_placeholder = self.password_input.get_placeholder()

            self.assert_data_equal_data(
                act_res=act_email_placeholder,
                exp_res=exp_email_placeholder,
                message=f'Некорректный плейсхолдер в {self.email_input.name}'
            )
            self.assert_data_equal_data(
                act_res=act_password_placeholder,
                exp_res=exp_password_placeholder,
                message=f'Некорректный плейсхолдер в {self.password_input.name}'
            )

    def error_alert_is_displayed(self, exp_alert):
        with allure.step(f'{self.alert.name} отображается'):
            act_alert = self.alert.get_text_of_element()

            self.assert_data_equal_data(
                act_res=act_alert,
                exp_res=exp_alert,
                message=f'Некорректный {self.alert.name}'
            )
