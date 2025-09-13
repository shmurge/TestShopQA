import allure
import pytest
from dotenv import load_dotenv
from config.base_test import BaseTest
from data_for_tests.data_for_tests import PlaceHolder, UserData, ErrorMessage
from time import sleep

load_dotenv()


@allure.suite('Страница логина')
class TestLoginPage(BaseTest):

    @allure.title('Переход на страницу создания аккаунта')
    def test_goto_create_account_page(self):
        self.login_page.open()
        self.login_page.go_to_create_account_page()
        self.create_account_page.is_opened()
        self.create_account_page.registration_form_is_displayed()

    @allure.title('Переход на страницу корзины')
    def test_goto_cart_page(self):
        self.login_page.open()
        self.header_page.go_to_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()

    @allure.title('Переход на главную страницу')
    def test_goto_main_page(self):
        self.login_page.open()
        self.header_page.go_to_main_page()
        self.main_page.is_opened()
        self.main_page.main_page_is_displayed()

    @allure.title('Авторизация пользователя')
    def test_user_authorization(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.fill_login_form(
            login=UserData.LOGIN,
            password=UserData.PASSWORD)

        self.account_page.is_opened()
        self.account_page.user_information_is_correct(
            username=UserData.USERNAME,
            user_email=UserData.LOGIN
        )
        self.header_page.username_is_correct(UserData.USERNAME)

    @allure.title('Нельзя авторизоваться, незарегистрированным пользователем')
    def test_unregistered_user_can_not_login(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.fill_email_input('qweqweqwe')
        self.login_page.fill_password_input('12345')
        self.login_page.click_on_login_button()

        self.login_page.error_alert_is_displayed(ErrorMessage.WRONG_LOGIN_OR_PASSWORD)

    @allure.title('Проверка плэйсхолдеров формы авторизации')
    def test_check_placeholders_in_login_form(self):
        self.login_page.open()
        self.login_page.is_opened()

        self.login_page.should_be_correct_placeholders_in_login_form(
            PlaceHolder.LOGIN_FORM_EMAIL_INPUT,
            PlaceHolder.LOGIN_FORM_PASSWORD_INPUT
        )
