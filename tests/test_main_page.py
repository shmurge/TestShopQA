import allure
from config.base_test import BaseTest
from time import sleep


@allure.suite('Главная страница')
class TestMainPage(BaseTest):

    @allure.title('Переход на страницу логина')
    def test_goto_login_page(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.go_to_login_page()
        self.login_page.is_opened()
        self.login_page.login_form_is_displayed()

    @allure.title('Переход на страницу корзины')
    def test_goto_cart_page(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.go_to_cart_page()
        self.cart_page.is_opened()
        self.cart_page.order_overview_is_displayed()

    @allure.title('Выбор товара на главной странице')
    def test_select_product_on_main_page(self):
        self.main_page.open()
        title, price = self.main_page.select_random_product()
        self.product_page.check_title_and_price(title, price)
