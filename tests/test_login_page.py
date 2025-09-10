import allure
import pytest
from config.base_test import BaseTest
from time import sleep


class TestLoginPage(BaseTest):

    @allure.title('Переход на страницу создания аккаунта')
    def test_goto_create_account_page(self):
        self.login_page.open()
        self.login_page.go_to_create_account_page()
        self.create_account_page.is_opened()
        self.create_account_page.create_account_page_is_displayed()

    @allure.title('Переход на страницу корзины')
    def test_goto_cart_page(self):
        self.login_page.open()
        self.header_page.go_to_cart_page()
        self.cart_page.is_opened()
        self.cart_page.cart_page_is_displayed()

    @allure.title('Переход на главную страницу')
    def test_goto_main_page(self):
        self.login_page.open()
        self.header_page.go_to_main_page()
        self.main_page.is_opened()
        self.main_page.main_page_is_displayed()
        sleep(4)
