import allure
import pytest
from config.base_test import BaseTest
from time import sleep


class TestLoginPage(BaseTest):

    def test_first_test(self):
        self.login_page.open()
        self.login_page.go_to_create_account_page()
        self.create_account_page.is_opened()
        sleep(5)