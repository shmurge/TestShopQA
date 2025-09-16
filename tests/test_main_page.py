import allure
import pytest
from config.base_test import BaseTest

from time import sleep


@allure.suite('Главная страница')
class TestMainPage(BaseTest):

    @allure.title('Перейти в аккаунт')
    def test_goto_account_page_from_main(self, pre_login):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.goto_my_account()
        self.account_page.is_opened()

    @allure.title('Выйти из аккаунта')
    def test_exit_from_account(self, pre_login):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.logout()
        self.header_page.sign_in_button_is_displayed()

    @allure.title('Переход на страницу логина')
    def test_goto_login_page(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.goto_login_page()
        self.login_page.is_opened()
        self.login_page.login_form_is_displayed()

    @allure.title('Переход на страницу корзины')
    def test_goto_cart_page(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.goto_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()


    @allure.title('Выбор товара на главной странице')
    def test_select_product_on_main_page(self):
        self.main_page.open()
        title, price = self.main_page.select_random_product()
        self.product_page.check_title_and_price(title, price)
