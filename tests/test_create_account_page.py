import allure
from config.base_test import BaseTest
from data_for_tests.data_for_tests import UserData, InputData, ErrorMessage, PlaceHolder
from time import sleep


@allure.suite('Страница создания аккаунта')
class TestCreateAccountPage(BaseTest):

    @allure.title('Создание аккаунта')
    def test_create_account(self):
        self.create_account_page.open()
        self.create_account_page.fill_registration_form(
            email=InputData.VALID_EMAIL,
            username=InputData.USERNAME,
            password=InputData.VALID_PASSWORD
        )
        self.account_page.is_opened()
        self.account_page.contact_information_is_displayed()

    @allure.title('Нельзя создать аккаунт, если email уже занят')
    def test_create_account_with_already_registered_email(self):
        self.create_account_page.open()
        self.create_account_page.fill_registration_form(
            email=UserData.LOGIN,
            username=InputData.USERNAME,
            password=InputData.VALID_PASSWORD
        )

        self.create_account_page.should_be_correct_alert(ErrorMessage.EMAIL_ALREADY_EXIST)

    @allure.title('Нельзя создать аккаунт, если пароли в инпутах Password и Confirm Password не идентичны')
    def test_create_account_with_already_registered_email(self):
        self.create_account_page.open()
        self.create_account_page.fill_email(InputData.VALID_EMAIL)
        self.create_account_page.fill_username(InputData.USERNAME)
        self.create_account_page.fill_password(InputData.VALID_PASSWORD)
        self.create_account_page.fill_password_confirm('qwe')
        self.create_account_page.click_sign_up()

        self.create_account_page.should_be_correct_alert(ErrorMessage.PASSWORDS_MISSMATCH)

    @allure.title('Проверка плэйсхолдеров в форме регистрации')
    def test_create_account_with_already_registered_email(self):
        self.create_account_page.open()
        self.create_account_page.should_be_correct_placeholder(PlaceHolder.CREATE_ACCOUNT_USERNAME_INPUT)

    @allure.title('Переход на страницу логина')
    def test_goto_login_page(self):
        self.create_account_page.open()
        self.header_page.go_to_login_page()
        self.login_page.is_opened()
        self.login_page.login_page_is_displayed()

    @allure.title('Переход на страницу корзины')
    def test_goto_cart_page(self):
        self.create_account_page.open()
        self.header_page.go_to_cart_page()
        self.cart_page.is_opened()
        self.cart_page.cart_page_is_displayed()
