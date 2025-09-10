import allure
from pages.header_page import HeaderPage
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from config.links import Links
from locators.locs_create_account_page import CreateAccountPageLocators
# from locators.locs_account_page import AccountPageLocators
from conftest import set_env_key

from time import sleep


class CreateAccountPage(HeaderPage):
    PAGE_URL = Links.CREATE_ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.registration_form = BaseElement(
            self.browser, 'Форма регистрации', *CreateAccountPageLocators.REGISTRATION_FORM
        )
        self.email_input = Input(self.browser, 'Email', *CreateAccountPageLocators.INPUT_LOGIN)
        self.username_input = Input(self.browser, 'Имя пользователя', *CreateAccountPageLocators.INPUT_USERNAME)
        self.password_input = Input(self.browser, 'Пароль', *CreateAccountPageLocators.INPUT_PASSWORD)
        self.password_confirm_input = Input(
            self.browser, 'Подтверждение пароля', *CreateAccountPageLocators.INPUT_PASSWORD_CONFIRM
        )
        self.sign_up_button = Button(self.browser, 'Зарегистрироваться', *CreateAccountPageLocators.BUTTON_SUBMIT)
        self.alert = BaseElement(self.browser, 'Алерт', *CreateAccountPageLocators.ALERT)

    def create_account_page_is_displayed(self):
        with allure.step('Страница создания аккаунта отображается'):
            assert self.registration_form.is_visible(), 'Страница создания аккаунта не отображается!'

    def fill_email(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.email_input.name}'):
            self.email_input.fill_input(data)
            if save_to_env:
                set_env_key('LOGIN', data)

        return data

    def fill_username(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.username_input.name}'):
            self.username_input.fill_input(data)
            if save_to_env:
                set_env_key('USERNAME', data)

        return data

    def fill_password(self, data, save_to_env=True):
        with allure.step(f'Заполнить {self.password_input.name}'):
            self.password_input.fill_input(data)
            if save_to_env:
                set_env_key('PASSWORD', data)

        return data

    def fill_password_confirm(self, data):
        with allure.step(f'Заполнить {self.password_confirm_input.name}'):
            self.password_confirm_input.fill_input(data)

    def click_sign_up(self):
        self.sign_up_button.click()

    def fill_registration_form(self,
                               email,
                               username,
                               password
                               ):
        with allure.step(f'Заполнить {self.registration_form.name}'):
            self.registration_form.is_visible()
            self.fill_email(email)
            self.fill_username(username)
            self.fill_password(password)
            self.fill_password_confirm(password)
            self.sign_up_button.click()

    def should_be_correct_alert(self, exp_alert):
        with allure.step('Проверка алерта с ошибкой'):
            act_alert = self.alert.get_text_of_element().strip()

            self.base_assertions.assert_data_equal_data(act_alert, exp_alert)

    def should_be_correct_placeholder(self, exp_placeholder):
        with allure.step(f'{self.username_input.name}: проверка плэйсхолдера'):
            act_placeholder = self.username_input.get_placeholder().strip()

            self.base_assertions.assert_data_equal_data(act_placeholder, exp_placeholder)
