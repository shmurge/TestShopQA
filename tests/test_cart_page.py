import allure
import pytest

from config.base_test import BaseTest


@allure.suite('Корзина')
class TestCartPage(BaseTest):

    @allure.title('Итоговая стоимость одной единицы товара без комиссии должна быть корректной')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subtotal_price_for_one_product_should_be_correct(self, pre_add_random_product_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_subtotal_price()

    @allure.title('Комиссия (налог) на один товар должна составлять 15 процентов от общей стоимости')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_taxes_for_one_product_should_be_correct(self, pre_add_random_product_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.tax_should_be_15_percent()

    @allure.title('Итоговая стоимость одного товара с учетом комиссии должна быть корректной')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_price_with_tax_for_one_product_should_be_correct(self, pre_add_random_product_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_total_price_with_tax()

    @allure.title('Итоговая стоимость нескольких товаров без комиссии должна быть корректной')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subtotal_price_for_several_products_should_be_correct(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_subtotal_price()

    @allure.title('Комиссия (налог) на несколько товаров должна составлять 15 процентов от общей стоимости')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_taxes_for_several_products_should_be_correct(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.tax_should_be_15_percent()

    @allure.title('Итоговая стоимость нескольких товаров с учетом комиссии должна быть корректной')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_price_with_tax_for_several_products_should_be_correct(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.check_total_price_with_tax()

    @allure.title('Отображается сообщение "Корзина пуста" после удаления единственного товара из козины')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_only_one_product_from_cart(self, pre_add_random_product_to_cart):
        product_title = self.product_page.get_prod_title_on_page()

        self.cart_page.open()
        self.cart_page.is_opened()
        self.cart_page.remove_product_from_cart(product_title)

        self.cart_page.should_be_message_if_cart_is_empty()

    @allure.title('Удаленный товар не должен отображаться в списке товаров')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_random_product_from_cart(self, pre_add_several_random_products_to_cart):
        self.cart_page.open()
        self.cart_page.is_opened()
        prod_title = self.cart_page.remove_random_product_from_cart()

        self.cart_page.product_should_not_be_on_order_overview(prod_title)

    @allure.title('Если корзина пуста, пользователь увидит сообщение')
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_see_message_if_cart_is_empty(self):
        self.cart_page.open()
        self.cart_page.is_opened()

        self.cart_page.should_be_message_if_cart_is_empty()

    @allure.title('Переход на страницу логина')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_goto_login_page(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.header_page.goto_login_page()
        self.login_page.is_opened()
        self.login_page.login_form_is_displayed()

    @allure.title('Переход на главную страницу')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_goto_main_page(self):
        self.login_page.open()
        self.header_page.goto_main_page()
        self.main_page.is_opened()
        self.main_page.main_page_is_displayed()
