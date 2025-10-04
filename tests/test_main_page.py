import allure
import pytest

from config.base_test import BaseTest
from data_for_tests.data_for_tests import PlaceHolder, InputData, InfoMessage


@pytest.mark.order(2)
@allure.suite('Главная страница')
class TestMainPage(BaseTest):

    @allure.title('Перейти в аккаунт')
    def test_goto_account_page_from_main(self, pre_login):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.goto_my_account()
        self.account_page.is_opened()

    @pytest.mark.order(after="test_goto_account_page_from_main")
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

    @allure.title('Проверка плэйсхолдера в инпуте поиска товара')
    def test_check_placeholder_in_search_input(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.check_placeholder_in_search_input(PlaceHolder.MAIN_PAGE_SEARCH_INPUT)

    @allure.title('Выбор товара на главной странице')
    def test_select_product_on_main_page(self):
        self.main_page.open()
        self.main_page.is_opened()
        title, price = self.main_page.select_random_product()
        self.product_page.check_title_and_price_in_prod_page(title, price)

    @allure.title('Поиск товара на главной странице')
    @pytest.mark.xfail
    @pytest.mark.parametrize('query', InputData.PRODUCTS_SEARCH_QUERY)
    def test_search_product_on_main_page(self, query):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.search_product(query)
        self.main_page.check_searching_result(query)

    @allure.title('Поиск несуществующего товара на главной странице')
    def test_search_non_existent_product_on_main_page(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.check_message_with_no_results()
