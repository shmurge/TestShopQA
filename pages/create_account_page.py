import os

import allure
from dotenv import load_dotenv, set_key
from time import sleep

from config.links import Links
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from locators.locs_create_account_page import CreateAccountPageLocators
from pages.header_page import HeaderPage


class CreateAccountPage(HeaderPage):
    PAGE_URL = Links.CREATE_ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.registration_form = BaseElement(
            self.browser, 'Форма регистрации', *CreateAccountPageLocators.REGISTRATION_FORM
        )
        self.email_input = Input(self.browser, 'Ваш Email', *CreateAccountPageLocators.INPUT_LOGIN)
        self.username_input = Input(self.browser, 'Ваше имя', *CreateAccountPageLocators.INPUT_USERNAME)
        self.password_input = Input(self.browser, 'Пароль', *CreateAccountPageLocators.INPUT_PASSWORD)
        self.password_confirm_input = Input(
            self.browser, 'Подтверждение пароля', *CreateAccountPageLocators.INPUT_PASSWORD_CONFIRM
        )
        self.sign_up_button = Button(self.browser, 'Зарегистрироваться', *CreateAccountPageLocators.BUTTON_SUBMIT)
        self.alert = BaseElement(self.browser, 'Алерт', *CreateAccountPageLocators.ALERT)

    def registration_form_is_displayed(self):
        with allure.step(f'{self.registration_form.name} отображается'):
            assert self.registration_form.is_visible(), (f'{self.registration_form.name} не отображается!\n'
                                                         f'Скриншот {self.attach_screenshot(self.registration_form.name)}')

    def fill_email(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.email_input.name}'):
            self.email_input.fill_input(data)
            if save_to_env:
                self.set_env_key('LOGIN', data)

        return data

    def fill_username(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.username_input.name}'):
            self.username_input.fill_input(data)
            if save_to_env:
                self.set_env_key('USERNAME', data)

        return data

    def fill_password(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.password_input.name}'):
            self.password_input.fill_input(data)
            if save_to_env:
                self.set_env_key('PASSWORD', data)

        return data

    def fill_password_confirm(self, data):
        with allure.step(f'Заполнить {self.password_confirm_input.name}'):
            self.password_confirm_input.fill_input(data)

    def click_sign_up(self):
        self.sign_up_button.click()

    def fill_registration_form(self,
                               email,
                               username,
                               password,
                               save_to_env=True):
        with allure.step(f'Заполнить {self.registration_form.name}'):
            self.registration_form.is_visible()
            self.fill_email(email, save_to_env)
            self.fill_username(username, save_to_env)
            self.fill_password(password, save_to_env)
            self.fill_password_confirm(password)
            self.sign_up_button.click()

    def error_alert_is_displayed(self, exp):
        with allure.step(f'{self.alert.name} отображается'):
            act = self.alert.get_text_of_element()

            assert act == exp, (f'Некорректный имя {self.alert.name}\n'
                                f'ОР: {exp}\n'
                                f'ФР: {act}\n'
                                f'Скриншот {self.attach_screenshot(self.alert.name)}')

    def check_placeholders_in_registration_form(self, exp):
        with allure.step(f'Проверить плэйсхолдер в {self.username_input.name}'):
            act = self.username_input.get_placeholder()
            assert act == exp, (f'Некорректный плейсхолдер в {self.username_input.name}\n'
                                f'ОР: {exp}\n'
                                f'ФР: {act}\n'
                                f'Скриншот {self.attach_screenshot(self.username_input.name)}')

    @staticmethod
    def set_env_key(key, value):
        load_dotenv('.env')
        os.environ[key] = value
        set_key('.env', key, value)
