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
