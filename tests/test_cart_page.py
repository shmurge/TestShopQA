import allure
import pytest
from time import sleep

from config.base_test import BaseTest


@allure.suite('Корзина')
class TestCartPage(BaseTest):
    @allure.title('Если корзина пуста, пользователь увидит сообщение')
    def test_user_see_message_if_cart_is_empty(self):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.should_be_message_if_cart_is_empty()
