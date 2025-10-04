import allure
import pytest

from config.base_test import BaseTest
from data_for_tests.data_for_tests import UserData, InputData, ErrorMessage, PlaceHolder


@pytest.mark.order(3)
@allure.suite('Страница создания аккаунта')
class TestCreateAccountPage(BaseTest):

    @pytest.mark.order(1)
    @allure.title('Создание аккаунта')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_account(self):
        self.create_account_page.open()
        self.create_account_page.is_opened()
        self.create_account_page.fill_registration_form(
            email=InputData.VALID_EMAIL,
            username=InputData.USERNAME,
            password=InputData.VALID_PASSWORD)

        self.account_page.user_information_is_correct(
            username=InputData.USERNAME,
            user_email=InputData.VALID_EMAIL
        )
        self.header_page.username_is_correct(InputData.USERNAME)

    @allure.title('Нельзя создать аккаунт, если email уже занят')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_account_with_already_registered_email(self):
        self.create_account_page.open()
        self.create_account_page.is_opened()
        self.create_account_page.fill_registration_form(
            email=UserData.LOGIN,
            username=InputData.USERNAME,
            password=InputData.VALID_PASSWORD,
            save_to_env=False
        )

        self.create_account_page.error_alert_is_displayed(ErrorMessage.EMAIL_ALREADY_EXIST)

    @allure.title('Нельзя создать аккаунт, если пароли в инпутах Password и Confirm Password не идентичны')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_account_with_different_passwords(self):
        self.create_account_page.open()
        self.create_account_page.is_opened()
        self.create_account_page.fill_email(InputData.VALID_EMAIL, save_to_env=False)
        self.create_account_page.fill_username(InputData.USERNAME, save_to_env=False)
        self.create_account_page.fill_password(InputData.VALID_PASSWORD, save_to_env=False)
        self.create_account_page.fill_password_confirm('qwe')
        self.create_account_page.click_sign_up()

        self.create_account_page.error_alert_is_displayed(ErrorMessage.PASSWORDS_MISSMATCH)

    @allure.title('Проверка плэйсхолдеров формы регистрации')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_check_placeholders_in_registration_form(self):
        self.create_account_page.open()
        self.create_account_page.is_opened()
        self.create_account_page.check_placeholders_in_registration_form(
            PlaceHolder.CREATE_ACCOUNT_FORM_USERNAME_INPUT)

    @allure.title('Переход на страницу логина')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_goto_login_page(self):
        self.create_account_page.open()
        self.create_account_page.is_opened()
        self.header_page.goto_login_page()
        self.login_page.is_opened()
        self.login_page.login_form_is_displayed()

    @allure.title('Переход на страницу корзины')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_goto_cart_page(self):
        self.create_account_page.open()
        self.create_account_page.is_opened()
        self.header_page.goto_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()

    @allure.title('Переход на главную страницу')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_goto_main_page(self):
        self.create_account_page.open()
        self.create_account_page.is_opened()
        self.header_page.goto_main_page()
        self.main_page.is_opened()
        self.main_page.main_page_is_displayed()
